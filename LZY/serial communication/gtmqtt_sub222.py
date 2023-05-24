import random
import time
from paho.mqtt import client as mqtt_client

broker = 'mqtt.16302.com'
port = 1883
topic = "ZHS2023"
client_id = f'python-mqtt-{random.randint(0, 1000)}'


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!",client,userdata)
    else:
        print("Failed to connect, return code %d\n", rc)

client = mqtt_client.Client(client_id)
client.on_connect = on_connect
client.connect(broker, port)


def on_message(client, userdata, msg):
    print("Received from topic",topic,msg.payload.decode())
    

client.subscribe(topic)
client.on_message = on_message
client.loop_forever()
