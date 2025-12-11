import network
import socket
import time
import json
import machine
import ubinascii
import select

CONFIG_FILE = 'wifi.json'
AP_SSID = "ESP32-Config"
AP_PASS = "12345678"

def load_config():
    try:
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    except:
        return None

def save_config(ssid, password):
    try:
        data = {'ssid': ssid, 'password': password}
        with open(CONFIG_FILE, 'w') as f:
            json.dump(data, f)
        return True
    except:
        return False

def web_page():
    html = """<!DOCTYPE html>
    <html>
    <head> <title>ESP32 Config</title> <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
    body{font-family:sans-serif; text-align:center; margin-top:50px;}
    input{padding:10px; width:80%; margin:10px 0;}
    button{padding:10px 20px; background:#007BFF; color:white; border:none; border-radius:5px; cursor:pointer;}
    h1{color:#333;}
    p{color:#666; font-size: 12px;}
    </style>
    </head>
    <body>
    <h1>Configuracion WiFi</h1>
    <form action="/" method="post">
        <input type="text" name="ssid" placeholder="Network name (SSID)" required><br>
        <input type="password" name="password" placeholder="Password" required><br>
        <button type="submit">Save and restart</button>
    </form>
    </body>
    </html>
    """
    return html

def parse_request(request):
    try:
        req_str = request.decode()
        if "POST" in req_str and "ssid=" in req_str and "password=" in req_str:
            body = req_str.split('\r\n\r\n')[-1]
            params = body.split('&')
            ssid = params[0].split('=')[1].replace('+', ' ').replace('%20', ' ')
            password = params[1].split('=')[1].replace('+', ' ').replace('%20', ' ')
            return ssid, password
    except:
        pass
    return None, None

class DNSServer:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.setblocking(False)
        self.socket.bind(('', 53)) 

    def handle_dns(self):
        try:
            data, addr = self.socket.recvfrom(1024)
            packet = data[:2] + b'\x81\x80\x00\x01\x00\x01\x00\x00\x00\x00'   
            j = 12
            while data[j] != 0:
                j += 1
            question_section = data[12:j+5]
            packet += question_section
            
            packet += b'\xC0\x0C\x00\x01\x00\x01\x00\x00\x00\x3C\x00\x04'
            
            # Ip to redirect
            packet += bytes([192, 168, 4, 1])
            
            self.socket.sendto(packet, addr)
        except:
            pass

def start_ap_mode():
    print("Initializing soft ap...")
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.ifconfig(('192.168.4.1', '255.255.255.0', '192.168.4.1', '192.168.4.1'))
    ap.config(essid=AP_SSID, password=AP_PASS, authmode=3)

    print(f"Connect to Wifi: {AP_SSID}")
    
    # Web Server (HTTP)
    s_http = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_http.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s_http.bind(('', 80))
    s_http.listen(5)
    s_http.setblocking(False)

    # DNS
    dns_server = DNSServer()

    poller = select.poll()
    poller.register(s_http, select.POLLIN)
    poller.register(dns_server.socket, select.POLLIN)

    while True:
        responses = poller.poll(500)
        for sock, event in responses:
            if sock == s_http:
                # Manage web petitions
                try:
                    conn, addr = s_http.accept()
                    conn.setblocking(True) 
                    request = conn.recv(1024)
                    ssid, password = parse_request(request)
                    
                    if ssid and password:
                        print(f"Guardando: {ssid}")
                        save_config(ssid, password)
                        res = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<h1>Saved! restarting...</h1>"
                        conn.send(res.encode())
                        conn.close()
                        time.sleep(2)
                        machine.reset()
                    else:
                        res = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n" + web_page()
                        conn.send(res.encode())
                        conn.close()
                except Exception as e:
                    print(e)
            
            elif sock == dns_server.socket:
                dns_server.handle_dns()
    
def get_connection():
    error_count = 10
    config = load_config()
    print(f"ssid: {config['ssid']} pass: {config['password']}")
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    mac_bytes = wlan.config('mac')
    mac_str = ubinascii.hexlify(mac_bytes).decode().upper()
    CLIENT_ID = f"WeatherStation{mac_str}"

    if config:
        if not wlan.isconnected():
            print('Connecting to WiFi...')
            wlan.connect(config['ssid'], config['password'])
            
            while not wlan.isconnected():
                status = wlan.status()
                print(f"Status: {status}")
                if status == network.STAT_WRONG_PASSWORD or status == network.STAT_NO_AP_FOUND or status == network.STAT_CONNECT_FAIL:
                    error_count -= 1
                    print(f"Failed detected with status {status}")
                    if error_count == 0:
                        print("Error: Incorrect password or network not found.")
                        break 
                time.sleep(1)
                pass
            if wlan.isconnected():
                print("Connected with IP:", wlan.ifconfig()[0])
                return CLIENT_ID
    start_ap_mode()