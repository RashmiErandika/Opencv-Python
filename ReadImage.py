import cv2 as cv
import numpy as np

image = cv.imread('parrots.jpg',0); #Load an Color Image as Gray Image
print(image); #Print None if the image path is Incorrect
cv.namedWindow('Parrot', cv.WINDOW_NORMAL); #Resize window to show image
cv.imshow('Parrot',image); #Show Image
cv.waitKey(0); #Wait for any keyboard Action
cv.imwrite('parrotgray.jpeg',image); #Write the image
cv.destroyAllWindows(); #Destroys all the windows we created
