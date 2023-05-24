import paho.mqtt.client as mqtt
from mpython import *
import time
# 设置MQTT服务器地址和端口号
mqtt_server = "mqtt.eclipse.org"
mqtt_port = 1883
# 设置mCookie的设备ID和订阅主题
device_id = "mcookie-1234"
topic = "mcookie/{}/buzzer".format(device_id)
# 设置小星星音乐数据
notes = [262, 262, 392, 392, 440, 440, 392,
         349, 349, 330, 330, 294, 294, 262]
durations = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1,
             0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1]
# 连接MQTT服务器
client = mqtt.Client()
client.connect(mqtt_server, mqtt_port, 60)
client.loop_start()
# 初始化mCookie的蜂鸣器
buzzer = Buzzer("D4")
# 发送小星星音乐数据到mCookie
for i in range(len(notes)):
    buzzer.play(notes[i])
    time.sleep(durations[i])
    buzzer.stop()
    time.sleep(0.1)
# 断开MQTT连接
client.loop_stop()
client.disconnect()