import numpy as np
from mcpi.minecraft import Minecraft
import pynput
import os
import time
import cv2

yolo_dir = 'D:\\New_minecraft_m3_all\\face_capture\\yolov3\\yolov3'  # YOLO文件路径一定不能有中文在路径里面
weightsPath = os.path.join(yolo_dir, 'yolov3.weights')  # 权重文件
configPath = os.path.join(yolo_dir, 'yolov3.cfg')  # 配置文件
labelsPath = os.path.join(yolo_dir, 'coco.names')  # label名称
with open(labelsPath, 'rt') as f:
    labels = f.read().rstrip('\n').split('\n')
net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)  ## 利用下载的文件
CONFIDENCE = 0.5  # 过滤弱检测的最小概率
THRESHOLD = 0.4  # 非最大值抑制阈值

#mc = Minecraft.create()
ctr = pynput.keyboard.Controller()
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('D:\\New_minecraft_m3_all\\face_capture\\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('D:\\New_minecraft_m3_all\\face_capture\\haarcascade_eye.xml')
while(True):
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    start = time.time()
    img = frame#测试图像
    (H, W) = img.shape[:2]
    blobImg = cv2.dnn.blobFromImage(img, 1.0 / 255.0, (416, 416), None, True,
                                    False)  ## net需要的输入是blob格式的，用blobFromImage这个函数来转格式
    net.setInput(blobImg)  ## 调用setInput函数将图片送入输入层
    # net.setPreferableBackend(cv2.dnn.DNN_BACKEND_INFERENCE_ENGINE)
    # net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
    outInfo = net.getUnconnectedOutLayersNames()  ## 前面的yolov3架构也讲了，yolo在每个scale都有输出，outInfo是每个scale的名字信息，供net.forward使用
    layerOutputs = net.forward(outInfo)  # 得到各个输出层的、各个检测框等信息，是二维结构。
    boxes = []  # 所有边界框（各层结果放一起）
    confidences = []  # 所有置信度
    classIDs = []  # 所有分类ID
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
    # 应用非最大值抑制(non-maxima suppression，nms)进一步筛掉
    idxs = cv2.dnn.NMSBoxes(boxes, confidences, CONFIDENCE, THRESHOLD)  # boxes中，保留的box的索引index存入idxs
    # 应用检测结果
    np.random.seed(42)
    COLORS = np.random.randint(0, 255, size=(len(labels), 3),
                               dtype="uint8")  # 框框显示颜色，每一类有不同的颜色，每种颜色都是由RGB三个值组成的，所以size为(len(labels), 3)
    if len(idxs) > 0:
        for i in idxs.flatten():  # indxs是二维的，第0维是输出层，所以这里把它展平成1维
            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])
            color = [int(c) for c in COLORS[classIDs[i]]]
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)  # 线条粗细为2px
            text = "{}: {:.4f}".format(labels[classIDs[i]], confidences[i])
            if(labels[classIDs[i]]=='book'):
                if (x + w / 2 < 213):
                    ctr.release('a')
                    ctr.release('d')
                    ctr.release('w')
                    ctr.release('s')
                    ctr.press('a')
                    print('a')
                # right
                elif(x + w/2>426):
                    ctr.release('a')
                    ctr.release('d')
                    ctr.release('w')
                    ctr.release('s')
                    ctr.press('d')
                    print('d')
                # top
                elif(y+h/2<160):
                    ctr.release('a')
                    ctr.release('d')
                    ctr.release('w')
                    ctr.release('s')
                    ctr.press('w')
                    print('w')
                # down
                elif(y+h/2>320):
                    ctr.release('a')
                    ctr.release('d')
                    ctr.release('w')
                    ctr.release('s')
                    ctr.press('s')
                    print('s')
                # stand by
                else:
                    ctr.release('a')
                    ctr.release('d')
                    ctr.release('w')
                    ctr.release('s')
                    print('stand by')
            cv2.putText(img, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color,
                        2)  # cv.FONT_HERSHEY_SIMPLEX字体风格、0.5字体大小、粗细2px
    end = time.time()
    print("YOLO1 took {:.6f} seconds".format(end - start))
    cv2.imshow('target detect result1', img)
    cv2.waitKey(1)
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    # for (x,y,w,h) in faces:
    #     # left
    #     # print("x:",x,"y:",y,"w",w,"h",h)
    #     if(x + w/2<213):
    #         ctr.release('a')
    #         ctr.release('d')
    #         ctr.release('w')
    #         ctr.release('s')
    #         ctr.press('a')
    #         print('a')
    #     # right
    #     elif(x + w/2>426):
    #         ctr.release('a')
    #         ctr.release('d')
    #         ctr.release('w')
    #         ctr.release('s')
    #         ctr.press('d')
    #         print('d')
    #     # top
    #     elif(y+h/2<160):
    #         ctr.release('a')
    #         ctr.release('d')
    #         ctr.release('w')
    #         ctr.release('s')
    #         ctr.press('w')
    #         print('w')
    #     # down
    #     elif(y+h/2>320):
    #         ctr.release('a')
    #         ctr.release('d')
    #         ctr.release('w')
    #         ctr.release('s')
    #         ctr.press('s')
    
    #         print('s')
    #     # stand by
    #     else:
    #         ctr.release('a')
    #         ctr.release('d')
    #         ctr.release('w')
    #         ctr.release('s')
    #         print('stand by')
    #
    #     img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    #     roi_gray = gray[y:y+h, x:x+w]
    #     roi_color = img[y:y+h, x:x+w]
    #     eyes = eye_cascade.detectMultiScale(roi_gray)
    #     for (ex,ey,ew,eh) in eyes:
    #         cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    # cv2.imshow('frame',img)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break
cap.release()
cv2.destroyAllWindows()
