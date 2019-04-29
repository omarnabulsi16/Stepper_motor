import roslibpy
#sets IP address and port number used
client = roslibpy.Ros(host='192.168.1.2', port=9090)\
#tells the program what ROS topic it should be listening to
listener = roslibpy.Topic(client, '/gnss','fake_sensor_test/gps')

# a function to begin listening and subscribe to the topic listed above
def start_listening():
    listener.subscribe(receive_message)
#prints out the message
def receive_message(message):
    #print('Heard talking: ' + message)
    print(message['roverLat'],message['roverLon'],message['baseLat'],message['baseLon'])
   # pass
# starts listening and returning values
client.on_ready(start_listening)
# runs the program forever
client.run_forever()
