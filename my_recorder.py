import cv2 as cv
import numpy as np

video_file = 0
video = cv.VideoCapture(video_file)

if video.isOpened():
    fps = video.get(cv.CAP_PROP_FPS)
    wait_msec = int(1 / fps * 1000)
    while True:
        valid, img = video.read()
        if not valid:
            break
        cv.imshow('Video Player', img)
        key = cv.waitKey(wait_msec)
        if key == 27:
            break
    cv.destroyAllWindows()