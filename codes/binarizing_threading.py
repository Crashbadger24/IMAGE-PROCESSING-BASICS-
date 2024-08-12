import cv2 as cv
import numpy as np

def frame_scaler(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread(r"D:\python\Learning_ML\Imageprocessing\ImagesandVideos\laura-college-K_Na5gCmh38-unsplash.jpg")

img2 = frame_scaler(img,scale=0.2)

gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)

#Simple thresholding
threshold,simple_thresholding = cv.threshold(gray,150,255,cv.THRESH_BINARY)
threshold2,inverse_thresholding =  cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
zeros = np.zeros_like(simple_thresholding)
merged = cv.merge([simple_thresholding,inverse_thresholding,zeros])
cv.imshow('simple version',simple_thresholding)
cv.imshow('inverse simple thresholding',inverse_thresholding)
cv.imshow('Merger',merged)

#Adaptive thresholding
adaptive_thresholding = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,11,3)
cv.imshow('adaptive thresholding',adaptive_thresholding)
cv.waitKey(0)
