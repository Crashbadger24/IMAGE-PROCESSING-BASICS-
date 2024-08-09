import cv2 as cv
import numpy as np


def frame_scaler(frame,scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)
    return cv.resize(frame , dimensions , interpolation=cv.INTER_AREA)

def translator(img ,x,y):
    translateMatrix = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,translateMatrix,dimensions)

def rotator(img , angle, rotpoint=None): #Giving the angle value in -ve implies its in clockwise direction
    (height, width) = img.shape[:2]  # corrected line to get image dimensions
    
    if rotpoint is None:  # corrected condition to check if rotpoint is None
        rotpoint = (width//2, height//2)
        
    rotmat = cv.getRotationMatrix2D(rotpoint, angle, 2.0) #2.0 refers to scaling in this  1.0 refers to no scaling
    dimensions = (width, height)
    
    return cv.warpAffine(img, rotmat, dimensions)

img = cv.imread(r"D:\python\Learning_ML\Imageprocessing\ImagesandVideos\WhatsApp Image 2024-05-28 at 16.21.06_4b37df10.jpg")

#x -> >=0 towards right
# x -> <0 towards left
#y >0 down
#y<0 up
translated_matrix = translator(img,100,200)
cv.imshow('translatedimage',translated_matrix)
cv.waitKey(0)
rotated_image = rotator(img , 45)
cv.imshow('Rotated',rotated_image)
cv.waitKey(0)
resized = cv.resize(img ,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)
cv.waitKey(0)

flipped = cv.flip(img,0)#0 is vertical flip ,1 is horizontal , -1 is ulta
cv.imshow('flipped',flipped)
cv.waitKey(0)

cropped = img[200:300 , 200:400]
cv.imshow('Cropped',cropped)
cv.waitKey(0)