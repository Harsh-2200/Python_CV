import cv2
import numpy as np
#Contours --> outline 

cam = cv2.VideoCapture(0)

kernal = np.ones((5,5))

def empty():
    pass

cv2.namedWindow("Parameter")
cv2.resizeWindow("Parameter",640,240)
cv2.createTrackbar("threshold1","Parameter",0,255 , empty)
cv2.createTrackbar("threshold2","Parameter",0,255 , empty)
cv2.createTrackbar("Area_min","Parameter",1000,30000 , empty)



def getContours(img,imgContour):
    contours , hierarchies = cv2.findContours(img , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_NONE)         

    
    for cnt in contours:
        area = cv2.contourArea(cnt)
        area_min = cv2.getTrackbarPos("Area_min","Parameter")
        if area > area_min :
            cv2.drawContours(imgContour,cnt , -1 , (255,0,0) , 2)
            peri = cv2.arcLength(cnt , True)
            approx = cv2.approxPolyDP(cnt,0.02 * peri ,True)
            print(len(approx))
            x , y , w , h = cv2.boundingRect(approx)
            cv2.putText(imgContour,f'Point = {len(approx)}' , (x+w +20 , y +20) , cv2.FONT_HERSHEY_COMPLEX, 0.7 ,(0,255,0),2 )
            cv2.putText(imgContour,f'Area = {str(int(area))}' , (x+w +20 , y +40) , cv2.FONT_HERSHEY_COMPLEX, 0.7 ,(0,255,0),2 )






while cam.isOpened():
    isTrue , img = cam.read()
    cv2.imshow("cam",img)

    imgContour = img.copy()

    imgBlur = cv2.GaussianBlur(img, (7,7) , 1 )
    imgGray = cv2.cvtColor(imgBlur , cv2.COLOR_BGR2GRAY)

    threshold1 = cv2.getTrackbarPos("threshold1","Parameter")
    threshold2 = cv2.getTrackbarPos("threshold2","Parameter")
    imgCanny = cv2.Canny(imgGray , threshold1 , threshold2  )
    imgdil = cv2.dilate(imgCanny,kernal,iterations=1)

    getContours(imgdil,imgContour)


    cv2.imshow("imgContour",imgContour)

    cv2.imshow("Canny",imgCanny)
    cv2.imshow("Gray",imgGray)
    if cv2.waitKey(1)==ord("q"):
        break

