# 因为本人电脑上双击事件好像失效了，用单击代替，可以取消第32行注释，并将第33行注释以使用双击功能
# import packages
import cv2
# import numpy as np
import random
import time

# initialize variables
imgOriginal = cv2.imread('rabbit.png')
posX = 700
posY = 100
width = 100
height = 200
textX = 300
textY = 800
# imgOriginal = cv2.imread('rabbit2.png')
# posX = 450
# posY = 50
# width = 100
# height = 200
# textX = 350
# textY = 550
font=cv2.FONT_HERSHEY_SIMPLEX

# game logic
mode = 1
points = 0
fullMarks = 100
pos = (10000,10000)
clicked = False
interval = 1
# targetEvent = cv2.EVENT_LBUTTONDBLCLK              # 鼠标双击事件
targetEvent = cv2.EVENT_LBUTTONDOWN              # 鼠标单击事件

# functions
def show(name,image,waitTime):
	cv2.imshow(name,image)
	cv2.waitKey(waitTime)
	cv2.destroyAllWindows()

def mouseClick(event,x,y,flags,params):
	global pos,clicked
	if event == targetEvent:
		pos = (x,y)
		clicked = True


# initialize picture
img = imgOriginal.copy()
for i in range(0,3):
	for j in range(0,3):
		cv2.rectangle(img,(i*width,j*height),(i*width+width,j*height+height),(255,0,0),5)
# show('rabbit',img,0)

# initialize window
cv2.namedWindow('rabbit')
cv2.setMouseCallback('rabbit',mouseClick)

# set mode
imgtool = imgOriginal.copy()
cv2.putText(imgtool,'Which mode to play?',(50,300),font,3,(200,0,255),5)
cv2.putText(imgtool,'enter 1 for mode 1',(500,500),font,2,(100,50,255),3)
cv2.putText(imgtool,'enter 2 for mode 2',(500,600),font,2,(100,50,255),3)
cv2.imshow('rabbit',imgtool)
k = cv2.waitKey(0)
if k == ord('1'):
	mode = 1
elif k == ord('2'):
	mode = 2
else:
	imgtool = imgOriginal.copy()
	cv2.putText(imgtool,'wrong input, use default mode')
	show('rabbit',imgtool,1000)
	mode = 2
	
# game loop
while points < fullMarks:
	start = time.time()
	img2 = img.copy()
	chessboard = [[0,0,0],[0,0,0],[0,0,0]]
	# initialize game picture and chessboard
	for i in range(0,3):
		for j in range(0,3):
			num = random.randint(1,10)
			if num>5:
				chessboard[i][j]=1
				if mode == 1:
					img2[height*i:height*i+height,width*j:width*j+width] = img2[posY:posY+height,posX:posX+width]

	img3 = img2.copy()
	while time.time() - start < interval:
		# render
		if mode == 2:
			for i in range(0,3):
				for j in range(0,3):
					if chessboard[i][j] == 1:
						img2[height*i:height*i+height,width*j:width*j+width] = img2[posY:posY+height,posX:posX+width]
		cv2.putText(img2,'points: '+str(points),(textX,textY),font,4,(255,255,255),5)
		cv2.imshow('rabbit',img2)
		cv2.waitKey(1)
		x,y = pos
		# print(y//height,x//width)

		# update
		if clicked == True:
			if y<=3*height and x<=3*width and chessboard[y//height][x//width] == 1:
				points += 10
				pos = (10000,10000)
				clicked = False
				img2 = img3.copy()
				if mode == 2:
					chessboard[y//height][x//width] = 0
			else:
				points -= 2
				pos = (10000,10000)
				clicked = False
				img2 = img3.copy()

# game over
if points >=fullMarks:
	cv2.putText(imgOriginal,'success',(300,500), font, 5,(153, 22, 245),9)
	cv2.putText(imgOriginal,'press any key to exit',(700,700), font,1,(255,255,255),2)
	show('rabbit',imgOriginal,0)
