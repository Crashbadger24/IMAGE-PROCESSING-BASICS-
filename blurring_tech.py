import cv2 as cv
import numpy as np

def frame_scaler(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread(r"D:\python\Learning_ML\Imageprocessing\ImagesandVideos\laura-college-K_Na5gCmh38-unsplash.jpg")

#Average blur
blur_average = cv.blur(frame_scaler(img,scale=0.2),(7,7))
cv.imshow('Average blur',blur_average)
cv.waitKey(0)

#Gaussian blur
blur_gauss = cv.GaussianBlur(frame_scaler(img,scale=0.2), (7,7),0)
cv.imshow('Gaussian Blur',blur_gauss)
cv.waitKey(0)

#Median blur
median = cv.medianBlur(frame_scaler(img,scale=0.2),7)
cv.imshow('Median blur',median)
cv.waitKey(0)

#bilateral blur
bilateral = cv.bilateralFilter(frame_scaler(img,scale=0.2),7,15,15)
cv.imshow('Bilateral',bilateral)
cv.waitKey(0)