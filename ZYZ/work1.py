import cv2
import random
#读入背景图(600x600) 状态图200x200
img = cv2.imread('source/work1/back.jpg')
ds = cv2.imread('source/work1/ds.jpg')
ds = cv2.resize(ds,(200,200))
Nds = cv2.imread('source/work1/noD.jpg')
Nds = cv2.resize(Nds,(200,200))

#初始化状态列表
sit = [[0]*3 for i in range(3)]

#得分

score =0

#结果
result="none"

#鼠标事件
def click(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        if sit[x//200][y//200] == 1:
            global score
            score += 10
        else:
            score -= 20


#循环
while True:
    #更新状态列表
    for i in range(3):
        for j in range(3):
                rand = random.randint(0,1)
                sit[i][j] = rand
                #判断并更改图片
                if sit[i][j] == 1:
                   img[0+200*j:200+200*j,0+200*i:200+200*i] = ds
                else:
                    img[0 + 200 * j:200 + 200 * j, 0 + 200 * i:200 + 200 * i] = Nds

    # 更新图片
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, "SCORE:" + str(score), (5, 50), font, 1, (0, 0, 255), 3)
    winname='game'
    cv2.namedWindow(winname)
    # 绑定
    cv2.setMouseCallback(winname,click)
    # 计分
    if score == 100:
        cv2.putText(img, "SUCCESS!", (100, 300), font, 3, (0, 0, 255), 10)
        result = "SUCCESS"

    cv2.imshow(winname, img)
    cv2.waitKey(1000)

    if result == "SUCCESS":
        break


cv2.destroyALlWindows()


