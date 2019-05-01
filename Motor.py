#######################################################
#    	 	   LOVE_DEATH_ROBOTS			 	      #
#######################################################
import RPi.GPIO as GPIO
import time
import roslibpy
# Haversine gives the GPS coords of the base station
from Haversine import setTargetHeading as Haversine

# Initialize variables
data = baseLat = roverLat = baseLon = roverLon = 0
# converts the Haversine((lat1, lon1), (lat2, lon2)) function to be called by "Have" instead of the entire function
Have = Haversine((baseLat,baseLon), (roverLat,roverLon))
while (True):
    GPIO.setmode(GPIO.BCM)
    # these are the pins in use and MUST BE USED to control the motor on the base station
    control_pins = [4,17,11]

    # sets up the pins for the raspberry pi
    for pin in control_pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 0)
    timestamp = time.time()

    #Target = Have.setTargetHeading((lat1,lon1), (x,y))
    Have = Haversine((baseLat, baseLon), (roverLat,roverLon))
    # if the degree of the rover is higher than the IMU the below function will run
    if (Have > float(data)):
        GPIO.output(4,1)
    # The while function adds a tolerance of 3 to the IMU to prevent constant movement
        while(int(Have) not in range(int(float(data) - 5),int(float(data) + 5))):
            for x in range(30):
                GPIO.output(11,1)
                time.sleep(.00005)
                GPIO.output(11,0)
                time.sleep(.00005)
    # if the degree of the Rover is lower than the IMU the below function will run
    else:
        GPIO.output(4,0)
    # The while function adds a tolerance of 3 to the IMU to prevent constant movement
        while(int(Have) not in range(int(float(data) - 5), int(float(data) + 5))):
            for x in range(30):
                GPIO.output(11,1)
                time.sleep(.00005)
                GPIO.output(11,0)
                time.sleep(.00005)
    

GPIO.cleanup()