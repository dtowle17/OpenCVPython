import cv2
import numpy as np

cap = cv2.VideoCapture(0)


def nothing(x):
    pass


# Creating a window for later use
cv2.namedWindow('result')

# Starting with 100's to prevent error while masking
r, g, b = 100, 100, 100

# Creating track bar
cv2.createTrackbar('rl', 'result', 0, 255, nothing)
cv2.createTrackbar('rh', 'result', 255, 255, nothing)
cv2.createTrackbar('gl', 'result', 0, 255, nothing)
cv2.createTrackbar('gh', 'result', 255, 255, nothing)
cv2.createTrackbar('bl', 'result', 0, 255, nothing)
cv2.createTrackbar('bh', 'result', 255, 255, nothing)

while (1):

    _, frame = cap.read()

    # converting to HSV
    rgb = frame

    # get info from track bar and appy to result
    rl = cv2.getTrackbarPos('rl', 'result')
    rh = cv2.getTrackbarPos('rh', 'result')

    gl = cv2.getTrackbarPos('gl', 'result')
    gh = cv2.getTrackbarPos('gh', 'result')

    bl = cv2.getTrackbarPos('bl', 'result')
    bh = cv2.getTrackbarPos('bh', 'result')

    # Normal masking algorithm
    lower_blue = np.array([rl, gl, bl])
    upper_blue = np.array([rh, gh, bh])

    mask = cv2.inRange(rgb, lower_blue, upper_blue)

    maskedimage = cv2.bitwise_and(frame, frame, mask=mask)
    blank = np.zeros_like(maskedimage)
    cv2.imshow('result', blank)

    cv2.imshow('result2', maskedimage)

    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()
