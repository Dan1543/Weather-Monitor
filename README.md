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

## Key Features

* **Smart Wi-Fi Provisioning (Captive Portal):** If the device cannot connect to Wi-Fi (or on first boot), it automatically launches an Access Point named **`ESP32-Config`**. Connect to it to configure your Wi-Fi credentials via a simple web interface.
* **Deep Sleep Power Saving:** The device wakes up, reads sensors, transmits data, and immediately enters Deep Sleep for 1 hour to conserve energy.
* **Edge Computing:** Calculates **Dew Point** and **Delta variations** (changes since the last hour) locally on the device before transmission.
* **State Persistence:** Uses local flash memory to store the previous hour's readings, ensuring accurate delta calculations even after power cycles.

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
The `aws/` folder in this repository contains the necessary code to process and store the telemetry data in the cloud.

```text
aws/
├── lambda_function.py   # Python script to parse MQTT payloads and insert into DB
└── model.json           # Data schema/definition for the DynamoDB table
```

1.  Log in to **AWS IoT Core Console**.
2.  Create a new **Thing** (Device).
3.  **Important:** Download the certificates immediately during creation:
    * Device Certificate (`.crt`)
    * Private Key (`.key`)
    * Amazon Root CA 1 (`.pem`)
4.  Create and attach a Policy allowing `iot:Connect` and `iot:Publish`.
5.  Put your certificates on the `esp32/certs` folder
6. **DynamoDB**: Create a table (e.g., `WeatherStation`) (Partition key: `device_id`, Sort key: `timestamp`)
7. **Lambda**: Create a python function using both aws folder files and grant it IAM permision to write to DynamoDB
8. **IoT Rule**: Create a rule in the IoT Core to forward MQTT messages from the topic to the DynamoDB table

### 3. Firmware Setup
1.  Flash the latest **MicroPython** firmware onto your ESP32.
2.  Install the required libraries (via Thonny or pip):
    * `umqtt.simple`
    * `bme280` driver
3. Upload all the files from the esp32 folder to the device (including `main.py`, `wifi_manager.py`, and the `certs` folder).

### 4. Project Configuration (Securing Credentials)
This project uses a local `secrets.py` file to keep credentials safe. This file is ignored by Git.

1.  Locate the file `esp32/secrets.py`.
2.  Update the `AWS_ENDPOINT` variable with your specific AWS IoT Core endpoint URL.
3.  Update the `TOPIC` variable with your desired MQTT topic.

### 5. Run
1.  Reset the board or plug it into a power source.
2.  Since it is the first run, the ESP32 will not find a known network. It will create a WiFi Access Point named `ESP32-Config`.
3.  Connect to this network using your phone or computer (Password: 12345678 or as defined in code).
4.  A portal should open automatically (or go to 192.168.4.1).
5.  Enter your home Wi-Fi SSID and Password.
6.  The device will save the credentials, restart, and begin streaming data to AWS.

##  Security Note
This repository does not contain actual private keys or Wi-Fi passwords. The secrets.py file is listed in .gitignore to prevent accidental exposure.

## License
This project is open-source and available under the MIT License.