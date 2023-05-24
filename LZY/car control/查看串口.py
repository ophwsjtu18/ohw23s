import serial
import serial.tools.list_ports
#查看端口列表
port_list = list(serial.tools.list_ports.comports())
if len(port_list)<=0:
    print("无可用端口")
else :
    for comports in port_list:
        print(list(comports)[0],list(comports)[1])
