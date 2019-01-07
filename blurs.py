#Import The necessary libraries
import cv2
import numpy as np

#Start video capture
vd = cv2.VideoCapture(0)

#Forever Loop
while True:
    #Read video input
    ret, Frame = vd.read()

    #Check to make sure that there is video input
    if ret == False:
        print("Error: No Input")
        exit()

    #Resize the frame
    Frame = cv2.resize(Frame,(440,240))

    #Make a grayscale image
    gray = cv2.cvtColor(Frame, cv2.COLOR_BGR2GRAY)

    #Make a Regularly Blurred Image
    blur = cv2.blur(Frame,(5,5))

    #Make a Median Blur Image
    med = cv2.medianBlur(Frame,5)

    #Make a Gaussian Blur Image
    gaussian = cv2.GaussianBlur(Frame,(5,5),0)
    
    #Make a Bilateral Blur Image
    bil = cv2.bilateralFilter(Frame,5,5,5)

    cv2.imshow("Input",Frame)
    cv2.imshow("Grayscale Image",gray)
    cv2.imshow("Regular Blur",blur)
    cv2.imshow("Median Blur",med)
    cv2.imshow("Gaussian Blur",gaussian)
    cv2.imshow("Bilateral Blur",bil)
    cv2.waitKey(1)
