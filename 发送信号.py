import serial

ser = serial.Serial("COM8",9600)
#打开蓝牙端口
if ser.isOpen():
    print("打开成功")
    print(ser.name)
else :
    print("打开失败")

import numpy as np
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while(True):
 # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces: # y轴从上往下，x轴从左往右
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        if (x+w)/2 <100 and 100<(y+h)/2<200:
            ser.write('l'.encode("utf-8"))
        elif (x+w)/2 > 200 and 100<(y+h)/2<200:
            ser.write('r'.encode("utf-8"))
        elif (y+h)/2 < 100: 
            ser.write('g'.encode("utf-8"))
        elif (y+h)/2 >200:
            ser.write('b'.encode("utf-8"))


    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



 # When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

# while(True):
#     pub = input("运行指令：")
#     ser.write(pub.encode("utf-8"))
