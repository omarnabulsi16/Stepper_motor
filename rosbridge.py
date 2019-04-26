import roslibpy

client = roslibpy.Ros(host='192.168.1.2', port=9090)
listener = roslibpy.Topic(client, '/gnss','fake_sensor_test/gps')


def start_listening():
    listener.subscribe(receive_message)

def receive_message(message):
    #print('Heard talking: ' + message)
    print(message['roverLat'],message['roverLon'],message['baseLat'],message['baseLon'])
   # pass

client.on_ready(start_listening)
client.run_forever()
