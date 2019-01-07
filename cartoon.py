import cv2
import numpy as np


img = cv2.imread("tree.jpg")
img = cv2.resize(img,(600,600))
cv2.imshow("Before",img)
for i in range(0,50):
    img = cv2.bilateralFilter(img,5,20,20)
cv2.imshow("After",img)
cv2.waitKey(0)
