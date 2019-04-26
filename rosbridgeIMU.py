import roslibpy

client = roslibpy.Ros(host='192.168.1.2', port=9090)
listener2 = roslibpy.Topic(client, '/baseIMU','std_msgs/String')


def start_listening2():
    listener2.subscribe(receive_message)

def receive_message(message):
    #print('Heard talking: ' + message['data'])
    #print(message['roverLat'],message['roverLon'])
    pass

client.on_ready(start_listening2)
client.run_forever()
