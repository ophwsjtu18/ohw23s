# import time
import numpy as np
import cv2
import random
import numpy as np

get = 0
score = 0
def draw_circle(event,x,y,flags,param):
    global score
    get = 0
    if event==cv2.EVENT_LBUTTONDBLCLK:
        cv2.rectangle(img,(x-10,y-10),(x+10,y+10),(0,255,0),3)
        for i in range(3):
            for j in range(3):
                if random.randint(1,10)>5:
                    cv2.rectangle(img,(20+j*100,20+i*100),(40+(j)*100,40+(i)*100),(0,255,0),1)
                    if y< (i+1)*100 and y> (i)*100 and x> (j)*100 and x< (j+1)*100 :
                        get +=1
        if get >= 1:
            score +=10
            font=cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img,'get it',(10,400), font, 4,(255,255,255),2)
        else:
            font=cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img,"miss",(10,400), font, 4,(255,255,255),2)
            score -=2            
# 创建图像与窗口并将窗口与回调函数绑定
img=np.zeros((512,512,3),np.uint8)
while(1):
    for i in range(3):
        for j in range(3):
            cv2.rectangle(img,(j*100,i*100),((j+1)*100,(1+i)*100),(0,255,0),5)
    cv2.imshow('image',img)
    cv2.setMouseCallback('image',draw_circle)
    img=np.zeros((512,512,3),np.uint8)
    if cv2.waitKey(1000)&0xFF==27:
        break
    #print("success")
    cv2.destroyWindow('image')
    print("您当前的得分为:",score)
    if score >=100:
        print("success")
        break


