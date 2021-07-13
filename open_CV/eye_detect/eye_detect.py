import cv2


cam = cv2.VideoCapture(0)

while cam.isOpened():
    thresh , frame = cam.read()
    #cv2.imshow("frame",frame)

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    haar = cv2.CascadeClassifier('eye.xml')
    face = haar.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=7)
    
    for (x,y,w,h) in face:
        cv2.rectangle( frame , (x,y) , (x+w,y+h) , (0,255,0) , thickness=2 )

    cv2.imshow("frame",frame)

    if cv2.waitKey(10)==ord("q"):
        break



