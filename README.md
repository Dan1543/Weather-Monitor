# ESP32 AWS IoT Weather Station

![Platform](https://img.shields.io/badge/Platform-ESP32-blue)
![Language](https://img.shields.io/badge/Language-MicroPython-green)
![Cloud](https://img.shields.io/badge/Cloud-AWS_IoT_Core-232F3E)

A concept of an end to end application that streams environmental telemetry (Temperature, Humidity, Pressure) from an ESP32 microcontroller to the AWS Cloud using MQTT over SSL/TLS.

## Project Overview

This project demonstrates a complete IoT pipeline, focusing on security and cloud integration. It reads real time data from a **BME280** sensor and transmits it to **AWS IoT Core**.

The system is designed to be:
* **Secure:** Uses MQTT mutual authentication.
* **Efficient:** Runs on MicroPython for rapid development and JSON data formatting.
* **Scalable:** Leverages AWS serverless infrastructure.

### Hardware
* **Microcontroller:** ESP32 DevKit V1
* **Sensor:** Bosch BME280 (Temperature, Humidity, Barometric Pressure)
* **Protocol:** I2C

### Software & Cloud Stack
* **Firmware:** MicroPython (v1.20+)
* **Cloud Service:** AWS IoT Core (MQTT Broker)
* **Security:** AWS IAM Policies & X.509 Certificates

---

## Installation & Setup

Follow these steps to replicate this project.

### 1. Hardware Wiring
Connect the BME280 to the ESP32:
* **VCC** -> 3.3V
* **GND** -> GND
* **SDA** -> GPIO 21
* **SCL** -> GPIO 22

### 2. AWS Configuration
1.  Log in to **AWS IoT Core Console**.
2.  Create a new **Thing** (Device).
3.  **Important:** Download the certificates immediately during creation:
    * Device Certificate (`.crt`)
    * Private Key (`.key`)
    * Amazon Root CA 1 (`.pem`)
4.  Create and attach a Policy allowing `iot:Connect` and `iot:Publish`.
5.  Put your certificates on the `esp32/certs` folder

### 3. Firmware Setup
1.  Flash the latest **MicroPython** firmware onto your ESP32.
2.  Install the required libraries (via Thonny or pip):
    * `umqtt.simple`
    * `bme280` driver
3. Upload all the files on the `esp32` folder

### 4. Project Configuration (Securing Credentials)
This project uses a local `secrets.py` file to keep credentials safe. This file is ignored by Git.

1.  Clone this repository.
3.  Locate the file `esp32/secrets.py`.
4.  Fill in your specific data:

```python
# secrets.py
AWS_ENDPOINT = "your-endpoint.iot.us-east-1.amazonaws.com"
AWS_CLIENT_ID = "YOUR_THING_NAME"
```

### 5. Run
Reset the board. The ESP32 will create a network to connect, once you connect to the access point via a phone or computer fill the SSID and password of your desired 2.4Ghz network and saved them to start streaming the payloads to the MQTT topic of the last step.

##  Security Note
This repository does not contain actual private keys or Wi-Fi passwords. The secrets.py file is listed in .gitignore to prevent accidental exposure.

## License
This project is open-source and available under the MIT License.