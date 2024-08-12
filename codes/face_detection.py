import cv2 as cv
import numpy as np
def frame_scaler(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
img = cv.imread("D:\python\Learning_ML\Imageprocessing\ImagesandVideos\Screenshot 2024-06-06 200248.png")
cv.imshow('image',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

haar_cascade = cv.CascadeClassifier("D:\python\Learning_ML\Imageprocessing\haar_face.xml")
faces_count = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=6)
print(f'no of faces are {len(faces_count)}')

for (x,y,w,h) in faces_count:
    cv.rectangle(img,(x,y),(x+h,y+h),(0,255,0),thickness=1)
cv.imshow('faces',img)
cv.waitKey(0)