import cv2
import numpy as np
import random

# 初始化棋盘
chessboard = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# 初始化分数
score = 0

# 创建窗口
cv2.namedWindow('image')

# 鼠标回调函数
def on_mouse(event, x, y, flags, param):
    global score
    if event == cv2.EVENT_LBUTTONDBLCLK:
        # 计算点击位置对应的棋盘坐标
        x = x // 100
        y = y // 100

        # 判断是否击中地鼠
        if chessboard[x][y] == 1:
            score += 10
            print('Hit! Score: ', score)
        else:
            score -= 2
            print('Miss! Score: ', score)

# 设置鼠标回调函数
cv2.setMouseCallback('image', on_mouse)

while True:
    # 每秒更新一次地鼠位置
    cv2.waitKey(1000)

    # 随机生成地鼠位置
    for i in range(3):
        for j in range(3):
            chessboard[i][j] = random.choice([0, int(random.random() > 0.5)])

    # 显示棋盘
    img = np.zeros((300, 300), dtype=np.uint8)
    for i in range(3):
        for j in range(3):
            if chessboard[i][j] == 1:
                cv2.circle(img, (i * 100 + 50, j * 100 + 50), 30, (255), -1)
    cv2.imshow('image', img)

    # 判断是否达到100分
    if score >= 100:
        print('Success!')
        break

cv2.destroyAllWindows()