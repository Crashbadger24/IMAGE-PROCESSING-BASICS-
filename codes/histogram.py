
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def frame_scaler(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread(r"D:\python\Learning_ML\Imageprocessing\ImagesandVideos\laura-college-K_Na5gCmh38-unsplash.jpg")

gray = cv.cvtColor(frame_scaler(img,scale=0.2),cv.COLOR_BGR2GRAY)
blank = np.zeros(gray.shape[:2],dtype='uint8')
circle = cv.circle(blank,(gray.shape[1]//2,gray.shape[0]//2),100,255,-1)
cv.imshow('Masker',circle)
masked_img = cv.bitwise_and(gray,gray,mask=circle)
cv.imshow('masked',masked_img)


histogram = cv.calcHist([gray],[0],None,[256],[0,256])
plt.figure()
plt.title('Grayscale Histrogram')
plt.xlabel('Bins')
plt.ylabel('No of pixels')
plt.plot(histogram)
plt.xlim([0,255])
plt.show()
 



cv.waitKey(0)
