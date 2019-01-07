import cv2
import numpy as np

#Read an image in
#img = cv2.imread("tpot.png")

#Print it's dimensions and stuff
'''
print(img.shape)
print(img.size)
print(H,W)
'''

#img = cv2.resize(img,(600,600))
#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#H=img.shape[0]
#W=img.shape[1]
#px=img[H//2,W//2]

#(b,g,r) = px
'''
img[90:500, 18:293]=img[90:500,550:275:-1]
img[320:490, 18:550]=img[320:150:-1, 18:550]
'''

'''
cv2.imshow("dksdf",cv2.flip(img,0))
cv2.imshow("sdkfls",cv2.flip(img,1))
cv2.imshow("sdklfjs",cv2.flip(img,-1))
cv2.circle(img,(300,300),30,(255,0,0),-1,lineType=8,shift=0)
'''
#Take a selection from the middle and make it the four corners
'''
i = img[275:325,275:325]
img[0:50, 0:50]=i
img[550:600, 550:600] = i
img[550:600, 0:50] = i
img[0:50, 550:600] = i
'''

#Open screen with a selection of another photo
'''
i = img[123:344,23:256]
cv2.imshow("sdklf",i)
'''

#And/Or/Nor?xor/Not operators for combining with bitwise
'''
img2 = np.zeros((400,400), dtype="uint8")

img = np.zeros((400,400), dtype = "uint8")

img[150:250,150:250]=255

cv2.circle(img2,(200,200),30,(255,0,0),-1,lineType=8,shift=0)
#change the not to any of the above operators(and,or,etc.)
img3 = cv2.bitwise_not(img,img2)

cv2.imshow("tpet",img2)

cv2.imshow("tpot",img)

cv2.imshow("sdot",img3)

#Save image to a file
#cv2.imwrite("/home/pi/Desktop/OpenCV/TPOT2.png",img)
'''

#Key Pressed Wait For
'''
if cv2.waitKey(0) == ord('a'):
   print ("pressed a")
'''

#Control intensity
'''
#Add
m = np.ones(img.shape,np.uint8)*100
added = cv2.add(img,m)
cv2.imshow("Added",added)

#Subtract
subbed = cv2.subtract(img,m)
cv2.imshow("subbed",subbed)
'''

#inRange() setup
#redLower = (0,0,90)
#redUpper = (50,50,255)
#0r
#redLower = np.array([0, 0, 40], dtype = "uint8")
#redUpper = np.array([90, 60, 255], dtype = "uint8")


#'''
#Video Stuff
vd = cv2.VideoCapture(0)
while True:
    #Read video input,resize,convert to gray,blur,threshold
    ret, Frame = vd.read()
    if ret == False:
        print("error")
        exit()
    Frame = cv2.resize(Frame,(440,240))
    #Frame = cv2.cvtColor(Frame, cv2.COLOR_BGR2GRAY)
    #Frame = cv2.bilateralFilter(Frame,5,5,5)
    #Frame = cv2.adaptiveThreshold(Frame,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
    #'''
    #Create a target with black background and yellow rings
    '''
    image = np.zeros((300,300,3), dtype="uint8")
    cv2.circle(image,(150,150),130,(0,255,255),15)
    cv2.circle(image,(150,150),90,(0,255,255),15)
    cv2.circle(image,(150,150),40,(0,255,255),-1)
    '''

    #Convert to grayscale
    #image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    #make a simple binary black and white threshold
    #ret,thresh = cv2.threshold(image,127,255,cv2.THRESH_BINARY)

    #make inRange Threshold
    threshImage=cv2.inRange(Frame,redLower,redUpper)
    cv2.imshow("inRange Image",threshImage)

    #contour practice
    '''
    (ret, contours, h) = cv2.findContours(thresh.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    imagecopy = image.copy()

    imagecopy = cv2.cvtColor(imagecopy,cv2.COLOR_GRAY2BGR)

    contourcolor=(255,0,0)

    cv2.drawContours(imagecopy,contours,-1,contourcolor,3)


    cv2.imshow("RETR_TREE",imagecopy)

    #for i in contours:
    #    print(cv2.contourArea(i))


    cv2.imshow("img",image)
    '''
    #'''
    cv2.imshow("Vid",Frame)
    cv2.waitKey(1)
vd.release()
#'''
cv2.waitKey(0)
cv2.destroyAllWindows()
