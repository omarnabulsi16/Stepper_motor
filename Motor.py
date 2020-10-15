#######################################################
#    	 	   LOVE_DEATH_ROBOTS			 	      #
#######################################################
import RPi.GPIO as GPIO
import time
import threading
import roslibpy
# Haversine gives the GPS coords of the base station
from Haversine import setTargetHeading as Haversine
client = roslibpy.Ros(host='192.168.1.2', port=9090)
#tells the program what ROS topic it should be listening to
listener = roslibpy.Topic(client, '/gnss','fake_sensor_test/gps')
#sets IP address and port number used
listener2 = roslibpy.Topic(client, '/baseIMU','std_msgs/String')
# a function to begin listening and subscribe to the topic listed above
def start_listening():
    listener.subscribe(receive_message)
def start_listening2():
    listener2.subscribe(receive_message2)
#prints out the message and sets variables (both recieve_message functions)
def receive_message(message):
    print("start receive message")
    global roverLat, roverLon, baseLon, baseLat
    print(message['roverLat'],message['roverLon'])
    roverLat = message['roverLat']
    roverLon = message['roverLon']
    baseLon = message['baseLon']
    baseLat = message['baseLat']
    print ("end receive message")
def receive_message2(message): 
    global data
    data = message['data']
#runs the motor
def main():
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
# Initialize variables
data = baseLat = roverLat = baseLon = roverLon = 0
# converts the Haversine((lat1, lon1), (lat2, lon2)) function to be called by "Have" instead of the entire function
Have = Haversine((baseLat,baseLon), (roverLat,roverLon))
client.run()
# starts listening and returning values
client.on_ready(start_listening())
#sets IP address and port number used
client.on_ready(start_listening2())
#thread to run main while rosbridge collect data
threading.Thread(target=main).start()
GPIO.cleanup()
