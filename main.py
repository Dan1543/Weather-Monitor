import time
import json
import network
import ssl
import ntptime
import secrets
import BME280 #Library to manipulate the sensor if you are using another one you may need another library
from machine import Pin, I2C, reset
from umqtt.simple import MQTTClient

KEY_PATH = "certs/private.pem.key"
CERT_PATH = "certs/cert.pem.crt"

# ESP32 - Pin assignment
i2c = I2C(scl=Pin(22), sda=Pin(21), freq=10000)

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Connecting to WiFi...')
        wlan.connect(secrets.WIFI_SSID, secrets.WIFI_PASS)
        while not wlan.isconnected():
            pass
    print('WiFi Connected! IP:', wlan.ifconfig()[0])

def set_time():
    try:
        ntptime.settime()
        # Imprimir la fecha actual para verificar (Año/Mes/Dia ...)
        print("Actual time:", time.localtime()) 
    except Exception as e:
        print("Error while synchronizing hour", e)
        
def read_file(filename):
    with open(filename, 'rb') as f:
        return f.read()

def run():
    bme = BME280.BME280(i2c=i2c)

    connect_wifi()
    set_time()

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
        client_id=secrets.CLIENT_ID,
        server=secrets.AWS_ENDPOINT,
        port=8883,
        keepalive=1200,
        ssl=True,
        ssl_params=ssl_params
    )
    
    try:
        client.connect()
        print("Connected to AWS IoT!")
        
        while True:
            temp = bme.temperature
            hum = bme.humidity
            pres = bme.pressure
            data = {
                "temperature": temp,
                "humidity": hum,
                "pressure": pres
            }
            msg = json.dumps(data)
            client.publish(secrets.TOPIC, msg)
            print("Enviado:", msg)
            time.sleep(10)
            
    except Exception as e:
        print("Error:", e)
        time.sleep(10)
        reset()

# Execute
run()