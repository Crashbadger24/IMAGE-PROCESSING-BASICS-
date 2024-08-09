import cv2 as cv
import matplotlib.pyplot as plt
def frame_scaler(frame,scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)
    return cv.resize(frame , dimensions , interpolation=cv.INTER_AREA)
img = cv.imread(r"D:\python\Learning_ML\Imageprocessing\ImagesandVideos\WhatsApp Image 2024-05-28 at 16.21.06_4b37df10.jpg")

plt.imshow(frame_scaler(img,scale=0.5))
plt.show()

#Grayscale
#grayscale = cv.cvtColor(frame_scaler(img,scale=0.5),cv.COLOR_BGR2GRAY)
#cv.imshow('Grayscale',grayscale)
#cv.waitKey(0)

#BGR TO HSV (HUE SATURATION VALUE)
#hsv = cv.cvtColor(frame_scaler(img,scale=0.5), cv.COLOR_BGR2HSV)
#cv.imshow('HSV',hsv)
#cv.waitKey(0)

#BGR TO LAB
#lab = cv.cvtColor(frame_scaler(img,scale=0.5), cv.COLOR_BGR2LAB)
#cv.imshow('HSV',lab)
#cv.waitKey(0)


#BGR TO RGB
rgb = cv.cvtColor(frame_scaler(img,scale=0.5),cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)
plt.imshow(rgb)
plt.show()
cv.waitkey(0)

# for reverse from HSV TO BGROR RGB TO BGR TO LAB TO BGR JUST USE COLOR_RGB2BGR OR COLOR_HSV2BGR OR LAB2BGR  appropriately with the correct image 