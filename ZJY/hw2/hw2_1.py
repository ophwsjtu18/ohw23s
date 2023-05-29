import random
import time
from paho.mqtt import client as mqtt_client

broker = 'mqtt.16302.com'       #服务器网址
port = 1883                     #连接端口
topic = "shanshangzhusun"               #订阅频道
client_id = f'python-mqtt-{random.randint(0, 1000)}'

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)

client = mqtt_client.Client(client_id)
client.on_connect = on_connect
client.connect(broker, port)
client.loop_start()
list=[1,1,5,5,6,6,5,4,4,3,2,2,1]
while True:
    for i in range(0,13):
        x=list[i]
        result = client.publish(topic, x)       #发送数据
        print("hello")
        time.sleep(1)
