import cv2

low = ()
high = ()

vd = cv2.VideoCapture(0)

while True :
    try :
        ret, frame = vd.read()
        if ret == False:
            print("error")
            exit()
        
        frame = cv2.resize(frame,(440,240))
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        
        frame = cv2.inRange(frame,low,high)
        
        cv2.imshow("colorblind",frame)
        cv2.waitKey(1)
    except OSError:
        print("error")
        pass