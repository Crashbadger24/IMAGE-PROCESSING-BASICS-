import cv2 as cv
import numpy as np

def frame_scaler(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread(r"D:\python\Learning_ML\Imageprocessing\ImagesandVideos\WhatsApp Image 2024-05-28 at 16.21.06_4b37df10.jpg")

blank = np.zeros(img.shape[:2],dtype= 'uint8')  # Creating blank arrays with the same dimensions as the input image

b, g, r = cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow("Blue", blue) # if b,g and r are displayed you would get intenristy variations in the three different images displaying black and white images 
cv.imshow("Green", green)
cv.imshow("Red", red)
cv.waitKey(0)
