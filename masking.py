import cv2 as cv
import numpy as np

def frame_scaler(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

image = cv.imread(r"D:\python\Learning_ML\Imageprocessing\ImagesandVideos\laura-college-K_Na5gCmh38-unsplash.jpg")
img = frame_scaler(image,scale=0.2)

blank = np.zeros(img.shape[:2],dtype = 'uint8')

mask1 =cv.circle(blank.copy(),(img.shape[1]//2+200 ,img.shape[0]//2+200),200,255,-1)
mask2 = cv.rectangle(blank.copy(),(img.shape[1]//2,img.shape[0]//2),(400,400),255,-1)
mask3 = cv.bitwise_and(mask1,mask2)
cv.imshow('Mask3 ',mask3)
masked = cv.bitwise_and(img,img,mask=mask3)
cv.imshow('Masked',masked)
cv.waitKey(0)