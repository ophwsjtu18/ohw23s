import numpy as np
import cv2
import os
import time
from mcpi.minecraft import Minecraft

yolo_dir = 'C:\Desktop\LZY\hw3'   # YOLO文件路径一定不能有中文在路径里面
weightsPath = os.path.join(yolo_dir, 'yolov3.weights')  # 权重文件
configPath = os.path.join(yolo_dir, 'yolov3.cfg')  # 配置文件
labelsPath = os.path.join(yolo_dir, 'coco.names')  # label名称
CONFIDENCE = 0.5  # 过滤弱检测的最小概率
THRESHOLD = 0.4  # 非最大值抑制阈值

with open(labelsPath, 'rt') as f:
    labels = f.read().rstrip('\n').split('\n')
# 加载网络、配置权重
net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)  ## 利用下载的文件
ln = net.getLayerNames()
ln = [ln[i-1] for i in net.getUnconnectedOutLayers()]

vs = cv2.VideoCapture(0)
time.sleep(2.0)
writer = None
(W, H) = (None, None)
while True:
    (grabbed, frame) = vs.read()
    if not grabbed:
        break
    print('ok')
    if W is None or H is None:
        (H, W) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416),swapRB=True, crop=False)
    net.setInput(blob)
    start = time.time()
    layerOutputs = net.forward(ln)
    end = time.time()
    boxes = [] # 所有边界框（各层结果放一起）
    confidences = [] # 所有置信度
    classIDs = [] # 所有分类ID
    for out in layerOutputs:  # 各个输出层
        for detection in out:  # 各个框框
            # 拿到置信度
            scores = detection[5:]  # 各个类别的置信度
            classID = np.argmax(scores)  # 最高置信度的id即为分类id
            confidence = scores[classID]  # 拿到置信度
            # 根据置信度筛查
            if confidence > CONFIDENCE:
                box = detection[0:4] * np.array([W, H, W, H])  # 将边界框放会图片尺寸
                (centerX, centerY, width, height) = box.astype("int")
                x = int(centerX - (width / 2))
                y = int(centerY - (height / 2))
                boxes.append([x, y, int(width), int(height)])
                confidences.append(float(confidence))
                classIDs.append(classID)
    #应用非最大值抑制(non-maxima suppression，nms)进一步筛掉
    idxs = cv2.dnn.NMSBoxes(boxes, confidences, CONFIDENCE, THRESHOLD) # boxes中，保留的box的索引index存入idxs
    # 应用检测结果
    np.random.seed(42)
    COLORS = np.random.randint(0, 255, size=(len(labels), 3), dtype="uint8")  # 框框显示颜色，每一类有不同的颜色，每种颜色都是由RGB三个值组成的，所以size为(len(labels), 3)
    if len(idxs) > 0:
        for i in idxs.flatten(): # indxs是二维的，第0维是输出层，所以这里把它展平成1维
            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])
            color = [int(c) for c in COLORS[classIDs[i]]]
            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)  # 线条粗细为2px
            text = "{}: {:.4f}".format(labels[classIDs[i]], confidences[i])
            cv2.putText(frame, text, (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)  # cv.FONT_HERSHEY_SIMPLEX字体风格、0.5字体大小、粗细2px
    mc=Minecraft.create()
    pos = mc.player.getTilePos()

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
    cv2.imshow("Image", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

vs.release()
cv2.destroyAllWindows()