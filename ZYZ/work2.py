import serial
import time

ser = serial.Serial("/dev/ttyUSB0",9600)

if ser.isOpen():
    print("打开成功")
    time.sleep(2)
    a = [1,1,5,5,6,6,5,4,4,3,3,2,2,1]
    for i in range(0,12):
        write_len = ser.write(str(a[i]).encode("utf-8"))
        print(write_len)
        time.sleep(1)
else:
    print("打开失败")
ser.close()
