import cv2 as cv
import numpy as np

cnt = 0
isRecording = False
save = None
fourcc = cv.VideoWriter_fourcc(*'XVID')
fps = 30.0
frame_size = (640, 480)
red_dot_position = (590, 240)
video_file = 0
video = cv.VideoCapture(video_file)
assert video is not None, 'Cannot open camera!!!'

while True:
    eval, frame = video.read()
    if not eval:
        break
    
    display_frame = frame.copy()
    if isRecording:
         cv.circle(display_frame, red_dot_position, radius=5, color=(0, 0, 255), thickness=-1)
    
    cv.imshow('Video Recording', display_frame)
    
    key = cv.waitKey(1)
    
    if key == ord(' '):
        if not isRecording:
            print("Recording started...")
            filename = f'output{cnt}.avi'
            save = cv.VideoWriter(filename, fourcc, fps, frame_size)
            isRecording = True
        else:
            print("Recording stopped and saved as output" + str(cnt) + ".avi")
            save.release()
            isRecording = False
            cnt += 1
    
    if isRecording and save is not None:
        save.write(frame)
    
    if key == 27:
        break

video.release()
if save is not None:
    save.release()
cv.destroyAllWindows()