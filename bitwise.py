import cv2 as cv
import numpy as np

blank = np.zeros((500,500),dtype='uint8')

rectangle = cv.rectangle(blank.copy(),(30,30),(380,380),(125,125,125),-1)
circle = cv.circle(blank.copy(),(250,250),300,(125,125,125),-1)
bitwise = cv.bitwise_and(rectangle,circle)
or_bitwise = cv.bitwise_or(rectangle,circle)
not_bitwise = cv.bitwise_not(rectangle)
xor_bitwise = cv.bitwise_xor(rectangle,circle)
cv.imshow('Rectangle',rectangle)
cv.imshow('Circle',circle)
cv.imshow('AND BINARY',bitwise)
cv.imshow('Bitwise_not',not_bitwise)
cv.imshow('Bitwise Or',or_bitwise)
cv.imshow('Bitwise XOR',xor_bitwise)

cv.waitKey(0)