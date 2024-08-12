import cv2 as cv
import time

video = cv.VideoCapture(0)
subtractor = cv.createBackgroundSubtractorMOG2(20, 50)

# Set the maximum duration for processing frames (in seconds)
max_duration = 6  # Example: 6 seconds

start_time = time.time()

while True:
    ret, frame = video.read()

    if ret:
        mask = subtractor.apply(frame)
        cv.imshow('Mask', mask)

    # Update current_time within the loop
    current_time = time.time()
    # Check if the maximum duration has been exceeded
    if current_time - start_time > max_duration:
        break

    # Add a delay to limit the frame rate (optional)
    # This is just for visualization purposes, you can adjust the delay as needed
    cv.waitKey(30)  # Waits for 30 milliseconds before processing the next frame

cv.destroyAllWindows()
video.release()
