import json
import math
from datetime import datetime
import time
import model

CLASSES = {0: 'Clear', 1: 'Cloudy', 2: 'Rain', 3: 'Storm'} 

def softmax(scores):
    e_x = [math.exp(s - max(scores)) for s in scores]
    suma = sum(e_x)
    return [x / suma for x in e_x]

def calculate_dew_point(temp, rhum):
        a = 17.27
        b = 237.7
        alpha = ((a * temp) / (b + temp)) + math.log(rhum / 100.0)
        dew_point = (b * alpha) / (a - alpha)
        return dew_point

def model_logic(data):
    # Call the model to get the prediction
    raw_scores = model.score(data)
    probs = softmax(raw_scores)
    results = []
    for i, prob in enumerate(probs):
        results.append({'class': CLASSES[i], 'prob': (prob*100)})

    return results

def lambda_handler(event, context):
    print("Received:", event)
    # Extract ESP32 data
    try:
        temp = float(event['temp'])
        rhum = float(event['rhum'])
        pres = float(event['press']) 
        delta_pres = float(event['delta_press'])
        delta_temp = float(event['delta_temp'])
        delta_rhum = float(event['delta_rhum'])
        
    except KeyError as e:
        return {
            'statusCode': 400,
            'body': json.dumps(f"Error: The field {str(e)} is missing!")
        }

    # Month and hour are calculated on the server
    ahora = datetime.now()
    month = ahora.month
    
    # Adjust to Tijuana (UTC - 8 aprox)
    hour = (ahora.hour - 8) % 24 

    # Calculate dew point
    
    dew = calculate_dew_point(temp, rhum)

    # Call the model
    #features = ['temp', 'rhum', 'pres', 'delta_pres', 'delta_temp', 'delta_rhum', 'dew_point', 'month', 'hour']
    data = [temp, rhum, pres, delta_pres, delta_temp, delta_rhum, dew, month, hour]
    results = model_logic(data)
    
    print(f"The probabilities are as the following: {results}")

    # 5. Retornar el resultado
    return {
        'statusCode': 200,
        'body': json.dumps({
            'prediccion': results,
            'inputs': {
                'dew_point': round(dew, 2),
                'hora_usada': hour
            }
        })
    }