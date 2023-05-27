import numpy as np
import cv2
import time

cnt = 0

ar = []

def callback(event,x,y,flags,param):
    if(event==cv2.EVENT_LBUTTONDBLCLK):
        global cnt
        i=0
        flag=0
        while(i<len(ar)):
            if(x>=ar[i] and x<=ar[i]+50 and y>=ar[i+1] and y<=ar[i+1]+100):
                cnt+=10
                flag=1
                break
            i+=2
        if(flag==0):
            cnt-=2



cv2.namedWindow('image')
cv2.setMouseCallback('image',callback)

time2 = time.time()
while True:
 time1 = time.time()
 if time1-time2>1:
     ar = []
     time2 = time1
     img = cv2.imread('rabbitgrass.jpeg')
     imgdup = img[20:120,350:400]
     for i in range(0,3):
      for j in range(0,3):
        rand = np.random.randint(1,9)
        if(rand>5):
          img[i*100:(i+1)*100,j*50:(j+1)*50] = imgdup
          ar.append(j*50)
          ar.append(i*50)
        cv2.rectangle(img, (j*50, i*100), ((j+1)*50, (i+1)*100), (255, 0, 0), 5)
     cv2.putText(img, str(cnt), (350, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 2)
     cv2.imshow('image', img)

     if cv2.waitKey(20)&0xFF==27:
         break
     elif cnt >= 100:
         img = cv2.imread('rabbitgrass.jpeg')
         cv2.putText(img, str(cnt), (325, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2)
         cv2.putText(img,'Success!',(150,200),cv2.FONT_HERSHEY_SIMPLEX,3,(0,0,255),2)
         cv2.imshow('image', img)
         cv2.waitKey(0)
         break
cv2.destroyAllWindows()



