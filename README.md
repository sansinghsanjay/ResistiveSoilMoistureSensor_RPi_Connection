# Intro Project: Connecting Resistive Soil Moisture Sensor with Raspberry Pi
This is a basic, intro project, explaining that how to connect Raspberry Pi with Resistive Soil Moisture Sensor.

## Raspberry Pi (RPi)
In this intro project, I have used "Raspberry Pi 3 Model B V1.2" board. 

OS is "Raspbian - Jessie (8)"

Python installed in this OS: Python 2.7.9

|![Raspberry Pi 3 Model B V1.2](https://github.com/sansinghsanjay/ResistiveSoilMoistureSensor_RPi_Connection/blob/master/images/RPi_modelName.jpg) | 
|:--:| 
| *Raspberry Pi 3 Model B V1.2* |

## Resistive Soil Moisture Sensor
Resistive Soil Moisture Sensor, available on Amazon. Several blogs are live on Internet for the details of this sensor. Hence, I am sharing few crucial details about this sensor:
1. Two output modes are available:
	i. Digital output: It gives output in two classes, "Moisture" or "No / Less Moisture".
	ii. Analog output: It gives output in the form of integer values, varies from 50 (approx) to 1000 (approx). In this case, user has to figure out the threshold values for their desired classes, like:
		a. Moisture, No Moisture
		b. High Moisture, Medium Moisture, Low Moisture, No Moisture
		c. Etc.
2. Power Required: 3.3V to 5V

Following is the picture of PIR Motion Sensor used here:

|![Resistive Soil Moisture Sensor 1](https://github.com/sansinghsanjay/ResistiveSoilMoistureSensor_RPi_Connection/blob/master/images/ResistiveSoilMoistureSensor_1.jpg) |![Resistive Soil Moisture Sensor 2](https://github.com/sansinghsanjay/ResistiveSoilMoistureSensor_RPi_Connection/blob/master/images/ResistiveSoilMoistureSensor_2.jpg) |
|:--:|:--:|
| *Resistive Soil Moisture Sensor - 1* | *Resistive Soil Moisture Sensor - 2* |

Resistive Soil Moisture Sensor have four pins:
1. VCC: For power to Sensor
2. GND: Ground
3. DO: Digital output
4. AO: Analog output

## Resistive Soil Moisture Sensor and Raspberry Pi (RPi) connections for Digital Output mode:
Connections should be in following manner:
1. VCC pin of Resistive Soil Moisture Sensor -> Pin 2 (+5V) of RPi
2. GND pin of Resistive Soil Moisture Sensor -> Pin 6 (GND) of RPi 
3. DO pin of Resistive Soil Moisture Sensor -> Pin 21 (GPIO) of RPi

|![Resistive Soil Moisture Sensor and RPi Connection](https://github.com/sansinghsanjay/ResistiveSoilMoistureSensor_RPi_Connection/blob/master/images/ResistiveSoilMoistureSensor_RPi_Connection.jpg) |
|:--:|
| *Resistive Soil Moisture Sensor and RPi Connection* |
