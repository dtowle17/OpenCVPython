import cv2
import numpy as np
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import time

#I2C address setup
mh = Adafruit_MotorHAT(addr=0x60)

f = Adafruit_MotorHAT.FORWARD
r = Adafruit_MotorHAT.RELEASE
b = Adafruit_MotorHAT.BACKWARD

def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

right = mh.getMotor(2)
left = mh.getMotor(1)
right.run(f)
left.run(f)

#values
#goal = int(input("What goal is the scoreing goal? 1 = Blue, 2 = Yellow "))
ballLow=(0,144,106)
ballHigh=(9,228,255)

goalBlueLow=(100,0,0)
goalBlueHigh=(114,187,255)
goalYellowLow=(22,56,68)
goalYellowHigh=(39,187,188)

split = int(440/3)

y = 0

vd = cv2.VideoCapture(0)
while True:
    try:
        ret, Frame = vd.read()
        #print("dflsk")
        if ret == False:
            print("error")
            exit()
        Frame = cv2.flip(Frame,1)
        Frame = cv2.flip(Frame,0)
        Frame = cv2.resize(Frame,(440,240))
        Frame = cv2.cvtColor(Frame,cv2.COLOR_BGR2HSV)
        Frame = cv2.GaussianBlur(Frame,(5, 5),0)
        '''
        g = cv2.inRange(Frame,goalBlueLow,goalBlueHigh)
        g2 = cv2.inRange(Frame,goalBlueLow,goalYellowHigh)
        '''
    
        Frame = cv2.inRange(Frame,ballLow,ballHigh)
        
        (rets, contours, h) = cv2.findContours(Frame.copy(),cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
        '''
        (retz, contourg, h) = cv2.findContours(g,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
        (retz2, contourg2, h) = cv2.findContours(g2,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
        '''
    
        contourColor = (255,0,0)
        
        if len(contours)<1 or cv2.contourArea(max(contours,key=cv2.contourArea))<20:
            print("Scanning")
            if y < 25:
                left.run(b)
                right.run(f)
                left.setSpeed(30)
                right.setSpeed(30)
                y=y+1
            else:
                left.run(f)
                right.run(f)
                left.setSpeed(60)
                right.setSpeed(60)
                time.sleep(0.5)
                y = 0
        else:
            left.run(f)
            right.run(f)
            c = max(contours,key=cv2.contourArea)
            
            cv2.drawContours(Frame,contours,-2,contourColor,3)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            cv2.drawContours(Frame,c,-2,contourColor,3)
            center = (int(x), int(y))
            if int(x)<split:
                print("Left")
                left.setSpeed(40)
                right.setSpeed(90)
            elif int(x)>(2*split):
                print("Right")
                right.setSpeed(40)
                left.setSpeed(90)
            elif ((2*split)+1)>int(x)>(split-1):
                print("Middle")
                left.setSpeed(100)
                right.setSpeed(100)
               
    
            
           # cv2.imshow("Ball",Frame)
           # cv2.waitKey(1)
    except OSError:
        print("error")
        pass
    '''
    finally:
        turnOffMotors()
        vd.release()
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    '''
