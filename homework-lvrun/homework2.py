# use python as serial port
import serial
import time

ser = serial.Serial('/dev/tty.usbserial-1120',9600)
if ser.isOpen():
	print('打开成功')
	time.sleep(2)           # note: is a must. wait for 2 seconds
	song = '1155665443221'
	for i in range(13):
		ser.write(song[i].encode('utf-8'))
		time.sleep(1)           # wait for the buzzer to play the music
else:
	print('打开失败')

ser.close()