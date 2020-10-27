import numpy as np

import cv2 as cv

capture = cv.VideoCapture('SampleVideo.mp4')

while(capture.isOpened()):
    ret,frame = capture.read()
    
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    
    cv.imshow('frame', gray)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    
capture.read()
cv.destroyAllWindows()
    

    
