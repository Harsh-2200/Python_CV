import cv2
import numpy as np
from numpy.matrixlib.defmatrix import matrix

img = cv2.imread('re.png')

cv2.imshow("img",img)

width , height = 250,350

pts1 = np.float32([[200,5],[423,68],[12,340],[317,465]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)
output = cv2.warpPerspective(img ,matrix,(width,height))

print(pts1[0])
for x in range(0,4):
    cv2.circle( img ,  ( int(pts1[x][0]) , int(pts1[x][1]) ) , 5 , (0,255,0) , cv2.FILLED)



cv2.imshow("img",img)
cv2.imshow("img_output",output)









cv2.waitKey(0)