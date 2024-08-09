import cv2 as cv
import time as time
import numpy as np

video = cv.VideoCapture(0)
start_time = time.time()
max_duration = 15
while True:
    ret,frame= video.read()
    laplace = cv.Laplacian(frame,cv.CV_64F)
    laplace = np.uint8(np.absolute(laplace))
    cv.imshow('Laplace',laplace)
    canned = cv.Canny(frame,250,250) #more threshold more rough ig have somwhere between 50 and 120 
    cv.imshow('canny',canned)
    current_time = time.time()
    if current_time-start_time>max_duration:
        break
    cv.waitKey(30)
    
cv.destroyAllWindows()
video.release()