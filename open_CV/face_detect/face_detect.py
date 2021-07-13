import cv2

'''
org = cv2.imread("img.jpg")

img = cv2.resize(org  ,  (350,400))
cv2.imshow("frame",img)


gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)

haar = cv2.CascadeClassifier('haar_face.xml')

face = haar.detectMultiScale(gray , scaleFactor=1.1 , minNeighbors = 3)                         # increse minNeighbors detect more acurate

print(f'no of faces found =  {len(face)}')

for (x,y,w,h) in face:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),1)

cv2.imshow('detected',img)

'''



cam = cv2.VideoCapture(0)

while True:
    thresh , frame = cam.read()
    #cv2.imshow("frame",frame)

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    haar = cv2.CascadeClassifier('haar_face.xml')
    face = haar.detectMultiScale(gray, scaleFactor=1.1 ,minNeighbors = 4)
    
    for (x,y,w,h) in face:
        cv2.rectangle( frame , (x,y) , (x+w,y+h) , (0,255,0) , thickness=2 )

    cv2.imshow("frame",frame)

    if cv2.waitKey(1)==ord("q"):
        break




















cv2.waitKey(0)