# libraries
import RPi.GPIO as GPIO
import time

# pin configuration
soilMoisture_input_pin = 21

# board configuration
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(soilMoisture_input_pin, GPIO.IN)

# vars
scan_count = 0

# when there is moisture print "Moisture"
while(True):
	i = GPIO.input(soilMoisture_input_pin)
	if(i == 0):
		scan_count += 1
		print(scan_count, "Moisture")
	if(i == 1):
		scan_count += 1
		print(scan_count, "No / Less Moisture")
	time.sleep(1) # sleep for 1 second
