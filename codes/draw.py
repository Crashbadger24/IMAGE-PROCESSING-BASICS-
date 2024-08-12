import cv2 as cv
import numpy as np

#Blank canvas/image makig
blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)
#Coloring a portion of the image using RGB coding
blank[100:300 ,200:400] = 125,125,125
cv.imshow('colored',blank)
#Rectangle
#Thickness=-1 implies fill the rectangle
#instead of 300,300 for half filling or rectangle scaled down to half we can use blank.shape[1]//2 and blank.shape[0]//2 for width and height respectively
cv.rectangle(blank, (0,0),(300,300),(0,125,125),thickness=-1)
cv.imshow('shape',blank)
#Circle
blank1 = np.zeros((500,500,3),dtype='uint8')
cv.circle(blank1,(250,250),100,(125,125,125),thickness=-1)
cv.imshow('circle',blank1)
#Line
#Thickness cannot be -1
cv.line(blank1,(0,0),(400,400),(125,125,125),thickness=3)
cv.imshow('line',blank1)
#Text on a image
cv.putText(blank1 , 'ಎಲ್ಲರಿಗೂ ನಮಸ್ಕಾರ',(400,400),cv.FONT_HERSHEY_SCRIPT_SIMPLEX,1.0,(0,255,0),3)
cv.imshow('Text',blank1)



img = cv.imread(r"D:\python\Learning_ML\Imageprocessing\ImagesandVideos\WhatsApp Image 2024-05-28 at 16.21.05_4d8c4238.jpg")
cv.imshow('PHOTO',img)
cv.waitKey(0)