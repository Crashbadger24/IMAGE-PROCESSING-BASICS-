import cv2 as cv
import numpy as np

img = cv.imread(r"D:\python\Learning_ML\Imageprocessing\ImagesandVideos\Screenshot 2024-05-31 231818.png")
blank = np.zeros(img.shape ,dtype = 'uint8')
#contouring 
#first blur then canny then contour finding
#blur = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
#canny = cv.Canny(blur,125,175)
#cv.imshow('CANNY',canny)

#using threshold function it takes only gray images imp
grayscale = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',grayscale)
cv.waitKey(0)

ret, thresh = cv.threshold(grayscale,125,255,cv.THRESH_BINARY)
cv.imshow('thresh',thresh)
cv.waitKey(0)

contour,hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
#RETR_LIST ALL CONTOURS ARE RETURNED
#RETR_TREE ALL HIERARCHY CONTOURS ARE RETURNED 
#SIMPLE FOR ALL CONTOURS 
print(f'{len(contour)} is the total number of contours')
cv.drawContours(blank,contour,-1,(125,125,125),1)
cv.imshow('DRAWN CONTOUR',blank)
cv.waitKey(0)