import serial
import time


ser = serial.Serial("COM3",9600)

song = ("1","1","5","5","6","6","5","4","4","3","3","2","2","1","5","5","4","4","3","3","2","5","5","4","4","3","3","2","1","1","5","5","6","6","5","4","4","3","3","2","2","1")

if ser.isOpen():
    print("成功")
    time.sleep(1)
    for i in song:
        ser.write(i.encode("utf-8"))
        time.sleep(1)
else:
    print("失败")
ser.close()