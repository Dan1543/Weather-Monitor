from sklearn.tree import _tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

# 1. Cargar tus datos (Asegúrate de tener el CSV generado anteriormente)
print("Cargando datos...")
df = pd.read_csv('weather_dataset.csv') # O el nombre de tu archivo final

# Definir Features (X) y Target (y)
features = ['temp', 'rhum', 'pres', 'month', 'hour', 'latitude'] # Ajusta si no calculaste dew_point
target = 'weather_label'

# Si no tienes dew_point en el CSV, quítalo de la lista features o calcúlalo aquí rápido:
if 'dew_point' not in df.columns:
    print("Calculando Dew Point...")
    b = 17.625
    c = 243.04
    gamma = (b * df['temp'] / (c + df['temp'])) + np.log(df['rhum'] / 100.0)
    df['dew_point'] = (c * gamma) / (b - gamma)
    features.append('dew_point')

X = df[features]
y = df[target]

# 2. Entrenar un Árbol de Decisión "Exportable"
# Limitamos max_depth para que el código if/else no sea infinito (max 10-15 niveles es bueno)
print("Entrenando modelo para exportación...")
clf = DecisionTreeClassifier(max_depth=12, class_weight='balanced', random_state=42)
clf.fit(X, y)

# 3. La Función Mágica: Convertir Árbol a Código Python
def tree_to_code(tree, feature_names):
    tree_ = tree.tree_
    feature_name = [
        feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
        for i in tree_.feature
    ]
    
    # Iniciar el buffer de código
    code = []
    code.append("def predecir_clima_logica(temp, rhum, pres, month, hour, latitude, dew_point):")
    
    def recurse(node, depth):
        indent = "    " * (depth + 1)
        if tree_.feature[node] != _tree.TREE_UNDEFINED:
            name = feature_name[node]
            threshold = tree_.threshold[node]
            
            # Escribir la rama IF
            code.append(f"{indent}if {name} <= {threshold:.2f}:")
            recurse(tree_.children_left[node], depth + 1)
            
            # Escribir la rama ELSE
            code.append(f"{indent}else:  # {name} > {threshold:.2f}")
            recurse(tree_.children_right[node], depth + 1)
        else:
            # Llegamos a una hoja (Una predicción)
            # Obtenemos la clase más probable
            class_idx = np.argmax(tree_.value[node])
            class_name = clf.classes_[class_idx]
            code.append(f"{indent}return '{class_name}'")

    recurse(0, 0)
    return "\n".join(code)

# 4. Generar y Guardar
print("Generando código Python...")
codigo_lambda = tree_to_code(clf, features)

# Guardar en un archivo .py para que puedas copiarlo
with open("logica_clima.py", "w", encoding="utf-8") as f:
    f.write("# Copia esta función dentro de tu AWS Lambda\n")
    f.write(codigo_lambda)

print("¡LISTO! Abre el archivo 'logica_clima.py'.")
print("Contiene una función gigante con toda la inteligencia de tu IA.")