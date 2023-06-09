import numpy as np
import cv2
import random

chessboard=[[0,0,0],[0,0,0],[0,0,0]]
score = 0
def hit(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        p=0
        q=0
        global score
        for p in [0,1,2]:
            for q in [0,1,2]:
                if x>0+50*p and x<50+50*p and y>0+100*q and y<100+100*q:
                    if chessboard[p][q]==1:score+=10
                    else: score-=2
while True:
    img = cv2.imread('rabbit.jpg',1)
    cnt=-1
    for i in [0,100,200]:
        for j in [0,50,100]:
            cnt+=1
            for m in [0,50,100]:
                for n in [0,100,200]:
                    cv2.rectangle(img,(0+m,0+n),(50+m,100+n),(255,0,0),5)
            a = random.randint(1,9)
            if (a>5):
                x0=cnt//3
                y0=cnt%3
                chessboard[x0][y0]=1
                img[0+i:100+i,0+j:50+j]=img[50:150,250:300]
    cv2.imshow('image',img)
    cv2.namedWindow('image')
    cv2.setMouseCallback('image',hit)
    #while(1):
        #cv2.imshow('image',img)
        #if cv2.waitKey(20)&0xFF==27:
            #break
    #四行注释代码没有用到
    if score==100 or score>100:
        cv2.destroyWindow('image')
        print ("success")
        print("您的得分为:")
        print(score)
        break
    cv2.waitKey(1000)
cv2.destroyAllWindows()
