import cv2
import numpy as np

# 初始化游戏得分和棋盘状态
score = 0
chessboard = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# 定义地鼠图片、背景图片
Background = cv2.imread("Background.jpg")
mouse=cv2.imread("mouse.jpg")
# 用于还原背景图片
Background_1 = cv2.imread("Background_1.jpg")

# 定义鼠标回调函数
def mouse_callback(event, m, n, flags, param):
    global score
    if event == cv2.EVENT_LBUTTONDBLCLK:
        row = n // 150
        col = m // 225
        if chessboard[row][col] == 1:
            score += 10
        else:
            score -= 2


cv2.namedWindow("game")
cv2.setMouseCallback("game", mouse_callback)
while score<100:
    for i in range(3):
        for j in range(3):
            if np.random.rand() < 0.5:
                chessboard[j][i] = 1
                Background[150 * j:150 + 150 * j, 37 + 225 * i:187 + 225 * i] = mouse[490:640, 0:150]#根据随机数显示地鼠
            else:
                chessboard[j][i] = 0
                Background[150 * j:150 + 150 * j, 37 + 225 * i:187 + 225 * i] = Background_1[150 * j:150 + 150 * j, 37 + 225 * i:187 + 225 * i]#还原背景图片

    cv2.imshow("game", Background)

# 设置快捷键“q”用来退出
    key = cv2.waitKey(1000)
    if key == ord("q"):
        break

# 游戏结束，显示结果
if score >= 100:
    print("You win!")
else:
    print("Game over. Final score:", score)

cv2.destroyAllWindows()

