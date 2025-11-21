import time
import machine
import network
import ssl
import ntptime # <--- Necesario para la hora
from umqtt.simple import MQTTClient

# Nombres de los archivos que subiste
KEY_PATH = "/private.pem.key"
CERT_PATH = "/cert.pem.crt"
# Nota: MicroPython a veces no necesita el Root CA explícitamente si no verificas el servidor rigurosamente, 
# pero es buena práctica tenerlo. Para simplificar este ejemplo, usaremos los dos principales.

# --- CONEXIÓN WIFI ---
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Conectando a WiFi...')
        wlan.connect(WIFI_SSID, WIFI_PASS)
        while not wlan.isconnected():
            pass
    print('¡WiFi Conectado! IP:', wlan.ifconfig()[0])

def set_time():
    print("Sincronizando hora con NTP...")
    try:
        ntptime.settime()
        # Imprimir la fecha actual para verificar (Año/Mes/Dia ...)
        print("Hora actual:", time.localtime()) 
    except Exception as e:
        print("Error sincronizando hora, reintentando...", e)
        
# --- LEER CERTIFICADOS ---
def read_file(filename):
    with open(filename, 'rb') as f:
        return f.read()

# --- PROGRAMA PRINCIPAL ---
def run():
    connect_wifi()
    set_time()
    # Leer claves
    print("Leyendo certificados...")
    key_data = read_file(KEY_PATH)
    cert_data = read_file(CERT_PATH)
    
    # --- AGREGA ESTO ---
    print("Tamaño Clave:", len(key_data))
    print("Tamaño Certificado:", len(cert_data))
    
    # Configurar SSL
    ssl_params = {
        "key": key_data,
        "cert": cert_data,
        "server_side": False,
        "server_hostname": AWS_ENDPOINT
    }
    
    # Conectar a AWS MQTT
    print("Conectando a AWS...")
    client = MQTTClient(
        client_id=CLIENT_ID,
        server=AWS_ENDPOINT,
        port=8883,
        keepalive=1200,
        ssl=True,
        ssl_params=ssl_params
    )
    
    try:
        client.connect()
        print("¡Conectado a AWS IoT!")
        
        while True:
            msg = '{"temperatura": 23.5, "estado": "funcionando"}'
            client.publish(TOPIC, msg)
            print("Enviado:", msg)
            time.sleep(10)
            
    except Exception as e:
        print("Error:", e)
        # Reiniciar si falla
        time.sleep(10)
        machine.reset()

# Ejecutar
run()