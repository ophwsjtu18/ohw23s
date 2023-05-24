import numpy as np
import cv2
from mcpi.minecraft import Minecraft
import time

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while(True):
 # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    mc=Minecraft.create()
    pos = mc.player.getTilePos()

    for (x,y,w,h) in faces: # y轴从上往下，x轴从左往右
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        if (x+w)/2 <100 and 100<(y+h)/2<200:
            mc.postToChat("left")
            mc.player.setPos(pos.x-1,pos.y,pos.z)
        elif (x+w)/2 > 200 and 100<(y+h)/2<200:
            mc.postToChat("right")
            mc.player.setPos(pos.x+1,pos.y,pos.z)
        elif (y+h)/2 < 100: 
            mc.postToChat("go")
            mc.player.setPos(pos.x,pos.y,pos.z-1)
        elif (y+h)/2 >200:
            mc.postToChat("back")
            mc.player.setPos(pos.x,pos.y,pos.z+1)
        elif 100<(x+w)/2 <200 and 100<(y+h)/2<200:
            if (y+h)/2 > 150:
                mc.postToChat("down")
                mc.player.setPos(pos.x,pos.y-1,pos.z)
            elif (y+h)/2 < 150:
                mc.postToChat("up")
                mc.player.setPos(pos.x,pos.y+1,pos.z)
        time.sleep(0.1)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



 # When everything done, release the capture
cap.release()
cv2.destroyAllWindows()