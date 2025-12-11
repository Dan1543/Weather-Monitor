import pandas as pd
import numpy as np
import m2cgen as m2c
from xgboost import XGBClassifier
from xgboost import XGBRFClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE

import os

print("Loading dataset...")
df = pd.read_csv('weather_dataset.csv')

df = df.dropna()

b = 17.625
c = 243.04
gamma = (b * df['temp'] / (c + df['temp'])) + np.log(df['rhum'] / 100.0)
df['dew_point'] = (c * gamma) / (b - gamma)

le = LabelEncoder()
df = df.sort_values(by=['latitude', 'longitude', 'month', 'day', 'hour'])

# Calculate deltas
df['delta_pres'] = df.groupby(['latitude', 'longitude'])['pres'].diff()
df['delta_temp'] = df.groupby(['latitude', 'longitude'])['temp'].diff()
df['delta_rhum'] = df.groupby(['latitude', 'longitude'])['rhum'].diff()

# You can change FUTURE_HOURS to predict further ahead RECOMMENDED: 1 to more accuracy
FUTURE_HOURS = 1
df['future_weather'] = df.groupby(['latitude', 'longitude'])['weather_label'].shift(-FUTURE_HOURS)

df = df.dropna() 

X = df[['temp', 'rhum', 'pres', 'delta_pres','delta_temp','delta_rhum', 'dew_point', 'month', 'hour']]

y = le.fit_transform(df['future_weather'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

classes = dict(zip(le.transform(le.classes_), le.classes_))
print(f"   Classes: {classes}")

temp_file = "temp_model.json"     
if os.path.exists(temp_file) == False:    
    print("3. Entrenando XGBOOST...")
    #Ideal to lambda free tier < mb (50 estimators, depth 7) 0.58 score
    #Ideal to best accuracy (75 estimators, depth 25) 0.78 score but larger size
    model = XGBClassifier(
        n_estimators=50,   
        max_depth=7,       
        learning_rate=0.1,
        num_parallel_tree=1,
        n_jobs=-1
    )

    model.fit(X_train, y_train)
    print("Score:", model.score(X_test, y_test))
    model.save_model(temp_file)
else:
    print("Using cached model...")
patched_model = XGBClassifier()
patched_model.load_model(temp_file)
patched_model.base_score = 0.0
patched_model.num_parallel_tree = 1

print("Trying to export using m2cgen...")

try:
    py_code = m2c.export_to_python(patched_model)
    
    nombre_archivo = "modelo_xgboost_lambda.py"
    with open(nombre_archivo, "w") as f:
        f.write(f"# CLASSES: {classes}\n\n")
        f.write(py_code)
        
    print(f"Code on '{nombre_archivo}'")
    # If you are constantly re-running the script to train different models, uncomment the next line
    #os.remove(temp_file)

except Exception as e:
    print(f"\nFailes: {e}")
    print("Verify version of m2cgen.")