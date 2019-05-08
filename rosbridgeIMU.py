import roslibpy
#sets IP address and port number used
client = roslibpy.Ros(host='192.168.1.2', port=9090)
#sets IP address and port number used
listener2 = roslibpy.Topic(client, '/baseIMU','std_msgs/String')

#sets IP address and port number used
def start_listening2():
    listener2.subscribe(receive_message)
#sets IP address and port number used
def receive_message(message):
    #print('Heard talking: ' + message['data'])
    #print(message['roverLat'],message['roverLon'])
    pass
#sets IP address and port number used
client.on_ready(start_listening2)
#sets IP address and port number used
client.run_forever()
