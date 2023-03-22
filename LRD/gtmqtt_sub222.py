import random
import time
from paho.mqtt import client as mqtt_client
import serial

ser=serial.Serial('com3',9600)
broker = 'mqtt.16302.com'       #服务器网址
port = 1883                     #连接端口
topic = "LRD2023"               #订阅频道
client_id = f'python-mqtt-{random.randint(0, 1000)}'

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)

client = mqtt_client.Client(client_id)
client.on_connect = on_connect
client.connect(broker, port)

def on_message(client,userdata,msg):
    print("Received from topic",topic,msg.payload.decode())
    if ser.isOpen():
        write_len=ser.write(msg.payload.decode().encode("utf-8"))

client.subscribe(topic)
client.on_message = on_message
client.loop_forever()
