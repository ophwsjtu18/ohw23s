import cv2
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
while(True):
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    print(frame.shape)
    img = frame
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces :
      #  print(x,y,w,h)
        if (x+w/2<213):
            print('LEFT')
  
        elif (x+w/2>426):
            print('RIGHT')

        elif (y+h/2<160):
            print('TOP')

        elif (y+h/2>320):
            print('DOWN')

        elif(x+w/2>213 and x+w/2<426 and y+h>160 and y+h<320):
            if (w>200 and h>200):
                print('forward')
            elif (w<100 and h<100):
                print('backward')
            else :
                print('stand by')

        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = img[y:y+h,x:x+w] 
    cv2.imshow('frame',img)
    if cv2.waitKey(10)& 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()