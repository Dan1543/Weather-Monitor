import time
import json
import network
import ssl
import ntptime
import ubinascii
import math
import secrets
import BME280 #Library to manipulate the sensor if you are using another one you may need another library
from machine import Pin, I2C, reset, deepsleep
from umqtt.simple import MQTTClient
import wifi_manager

KEY_PATH = "certs/private.pem.key"
CERT_PATH = "certs/cert.pem.crt"
# ESP32 - Pin assignment
i2c = I2C(scl=Pin(22), sda=Pin(21), freq=10000)
STATE_FILE = "last_reading.json"

led = Pin(2, Pin.OUT)
led.on()

print("Initializing...")
time.sleep(5)
led.off()

def flash_led(times):
    for _ in range(times):
        led.on()
        time.sleep(0.2)
        led.off()
        time.sleep(0.2)
    
def set_time():
    try:
        ntptime.settime()
        # Imprimir la fecha actual para verificar (Año/Mes/Dia ...)
        print("Actual time:", time.localtime()) 
    except Exception as e:
        print("Error while synchronizing hour", e)

def load_state():
    try:
        with open(STATE_FILE, "r") as f:
            data = json.load(f)
            return data["temp"], data["hum"], data["pres"]
    except Exception:
        return 0, 0, 0
def save_state(temp, hum, pres):
    try:
        data = {"temp": temp, "hum": hum, "pres": pres}
        with open(STATE_FILE, "w") as f:
            json.dump(data, f)
        print("State saved on flash.")
    except Exception as e:
        print("Error while saving state:", e)
        
def read_file(filename):
    with open(filename, 'rb') as f:
        return f.read()

def calculate_dew_point(temp, rhum):
    b, c = 17.625, 243.04
    gamma = (b * temp / (c + temp)) + math.log(rhum / 100.0)
    return (c * gamma) / (b - gamma)

def run():
    CLIENT_ID = wifi_manager.get_connection()
    flash_led(1)
    set_time()

    #Load if exists the last data
    last_temp, last_rhum, last_pres = load_state()    
    bme = BME280.BME280(i2c=i2c)

    # Reading keys
    key_data = read_file(KEY_PATH)
    cert_data = read_file(CERT_PATH)    
   
   # SSL
    ssl_params = {
        "key": key_data,
        "cert": cert_data,
        "server_side": False,
        "server_hostname": secrets.AWS_ENDPOINT
    }
    
    # Connect to AWS MQTT
    print("Connecting to AWS...")
    client = MQTTClient(
        client_id=CLIENT_ID,
        server=secrets.AWS_ENDPOINT,
        port=8883,
        keepalive=1200,
        ssl=True,
        ssl_params=ssl_params
    )
    
    try:
        client.connect()
        print("Connected to AWS IoT!")
        flash_led(3)
        #while True:
        temp = bme.temperature
        hum = bme.humidity
        pres = bme.pressure
        delta_temp = (temp-last_temp) if last_temp!= 0 else 0
        delta_rhum = (hum-last_rhum) if last_rhum!= 0 else 0
        delta_pres = (pres-last_pres) if last_pres!= 0 else 0
        last_temp = temp
        last_rhum = hum
        last_pres = pres
        
        dew = calculate_dew_point(temp,hum)
        data = {
            "device_id": CLIENT_ID,  
            "temp": temp,
            "rhum": hum,
            "pres": pres,
            "delta_pres": delta_pres,
            "delta_temp": delta_temp,
            "delta_rhum": delta_rhum,
            "dew": dew
        }
        msg = json.dumps(data)
        client.publish(secrets.TOPIC, msg)
        print("Sended:", msg)
        save_state(temp,hum,pres)
        flash_led(5)
        time.sleep(2)
        client.disconnect()
        
        print("Sleeping for 1 hour")
        deepsleep(3598000) #Sleep for 1 hour
            
    except Exception as e:
        print("Error:", e)
        time.sleep(10)
        reset()

# Execute
run()