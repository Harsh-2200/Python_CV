import cv2
import numpy as np
from numpy.matrixlib.defmatrix import matrix

circles = np.zeros((4,2),np.int)
counter = 0


def mousePoints(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONUP:
        global counter

        circles[counter] = x,y
        counter = counter + 1
        print("circles")



img = cv2.imread('re.png')

while True:
    if counter == 4:
        width , height = 250,350
        pts1 = np.float32([circles[0],circles[1],circles[2],circles[3]])                #Z patten
        pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
        matrix = cv2.getPerspectiveTransform(pts1,pts2)
        output = cv2.warpPerspective(img ,matrix,(width,height))
        cv2.imshow("output",output)


    for x in range(0,4):
        cv2.circle( img ,  ( int(circles[x][0]) , int(circles[x][1]) ) , 5 , (0,255,0) , cv2.FILLED)



    cv2.imshow("img",img)
    cv2.setMouseCallback("img",mousePoints)


    if cv2.waitKey(1)==ord("q"):
        
        break

"""
1       2
                                #selecting format

3       4
"""

