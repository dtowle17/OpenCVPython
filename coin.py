import cv2
import numpy as np

vd = cv2.VideoCapture(0)
while True:
    coin = 0
    ret, Frame = vd.read()
    if ret == False:
        print("error")
        exit()
    Frame = cv2.resize(Frame,(440,240))
    Frame = cv2.cvtColor(Frame,cv2.COLOR_BGR2GRAY)
    Frame = cv2.bilateralFilter(Frame,5,5,5)
    ret, Frame = cv2.threshold(Frame,195,255,cv2.THRESH_BINARY)
    (ret, contours, h) = cv2.findContours(Frame.copy(),cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
    imagecopy = cv2.cvtColor(Frame,cv2.COLOR_GRAY2BGR)
    contourColor = (255,0,0)
    
    cv2.drawContours(imagecopy,contours,-2,contourColor,3)
    
    for i in contours:
        ((x, y), radius) = cv2.minEnclosingCircle(i)
        center = (int(x), int(y))
        h = cv2.contourArea(i)
        print(h)
        if(4000>h>3250):
            print("There Is a Quarter!")
            cv2.putText(imagecopy,"25",center,cv2.FONT_HERSHEY_SIMPLEX,1.0,(255,0,0))
            coin+=25
        elif(3168>h>2450):
            print("There Is a Nickel!")
            cv2.putText(imagecopy,"5",center,cv2.FONT_HERSHEY_SIMPLEX,1.0,(255,0,0))
            coin+=5
        elif(2450>h>2105):
            print("There Is a Penny!")
            cv2.putText(imagecopy,"1",center,cv2.FONT_HERSHEY_SIMPLEX,1.0,(255,0,0))
            coin+=1
        elif(2105>h>250):
            print("There Is a Dime!")
            cv2.putText(imagecopy,"10",center,cv2.FONT_HERSHEY_SIMPLEX,1.0,(255,0,0))
            coin+=10
    cv2.putText(imagecopy,str(coin),(30,30),cv2.FONT_HERSHEY_SIMPLEX,1.0,(255,0,0))
    cv2.imshow("RETR_EXTERNAL",imagecopy)
    cv2.waitKey(1)
vd.release()

cv2.waitKey(0)
cv2.destroyAllWindows()
