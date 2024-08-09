import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def frame_scaler(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread(r"D:\python\Learning_ML\Imageprocessing\ImagesandVideos\laura-college-K_Na5gCmh38-unsplash.jpg")

img2 = frame_scaler(img,scale=0.2)
blank = np.zeros(img2.shape[:2],dtype='uint8')
circle = cv.circle(blank,(img2.shape[1]//2,img2.shape[0]//2),100,255,-1)
cv.imshow('Masker',circle)
masked_img = cv.bitwise_and(img2,img2,mask=circle)
cv.imshow('masked',masked_img)

plt.figure()
plt.title('Grayscale Histrogram')
plt.xlabel('Bins')
plt.ylabel('No of pixels')

colors = ('b','g','r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img2],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
    
plt.show()
cv.waitKey(0)