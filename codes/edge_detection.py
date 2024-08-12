import cv2 as cv
import numpy as np
def frame_scaler(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread(r"D:\python\Learning_ML\Imageprocessing\ImagesandVideos\laura-college-K_Na5gCmh38-unsplash.jpg")

img2 = frame_scaler(img,scale=0.2)

#LAPLACE METHOD

gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)

laplace = cv.Laplacian(gray , cv.CV_64F)

laplace = np.uint8(np.absolute(laplace))

cv.imshow('EDGES',laplace)


#SOBEL METHOD
sobelx = cv.Sobel(gray,cv.CV_64F,1,0)
sobely = cv.Sobel(gray,cv.CV_64F,0,1)
combined_sobel = cv.bitwise_or(sobelx,sobely)
cv.imshow('combined',combined_sobel)
cv.imshow('sobelx',sobelx)
cv.imshow('sobely',sobely)
cv.waitKey(0)