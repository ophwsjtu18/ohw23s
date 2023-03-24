import random
import time
from paho.mqtt import client as mqtt_client

broker = 'mqtt.16302.com'
port = 1883
topic = "LRD2023"
client_id = f'python-mqtt-{random.randint(0, 1000)}'


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!",client,userdata)
    else:
        print("Failed to connect, return code %d\n", rc)

client = mqtt_client.Client(client_id)
client.on_connect = on_connect
client.connect(broker, port)
client.loop_start()

while True:
    for i in [1,1,5,5,6,6,5,4,4,3,3,2,2,1]:
        result = client.publish(topic,i)       #发送数据
        print(i)
        time.sleep(1)
