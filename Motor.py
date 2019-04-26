######################################################
#        Love_Death_Robots					         #
######################################################
import RPi.GPIO as GPIO
import time
# Using older IMU software as a placeholder for ROS
from calAndRunImu.py import IMU12345 as imu
print imu()
# converts the IMU() function to be called "imuV" instead of the entire function
def location():
     global imuV
	 while True:
	 imuV = imu()
# The lat and longitude of the base station and the rover
#lat1 = 33.882224
#lat2 = 33.880883
#lon1 = -117.882679
#lon2 = -117.882647
# converts the Haversine((lat1, lon1), (lat2, lon2)) function to be called by "Have" 
#		instead of the entire function; Preparation for when Haversine is ready
# Using arbitrary variable in the mean time
Have = 180
#print Have	
GPIO.setmode(GPIO.BCM)
# these are the pins in use and MUST BE USED to control the motor on the base station
control_pins = [4,17,11]
# sets up the pins for the raspberry pi
for pin in control_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)
timestamp = time.time()
# if the degree of the rover is higher than the IMU the below function will run
if (Have > imu()):
    GPIO.output(4,1)
# The while function adds a tolerance of 3 to the IMU to prevent constant movement
    while(int(Have) not in range(int(imu() - 3),int(imu() + 3))):
        for x in range(500):
        for x in range(65):
            GPIO.output(11,1)
            time.sleep(.00005)
            GPIO.output(11,0)
    GPIO.output(4,0)
# The while function adds a tolerance of 3 to the IMU to prevent constant movement
    while(int(Have) not in range(int(imu() - 3), int(imu() + 3))):
        for x in range(500):
        for x in range(65):
            GPIO.output(11,1)
            time.sleep(.00005)
            GPIO.output(11,0)
			time.sleep(.00005)
GPIO.cleanup()