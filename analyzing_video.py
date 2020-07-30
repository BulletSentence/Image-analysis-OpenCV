import numpy as np
import cv2
import matplotlib.pyplot as plt

VFILE = "video/Teste.mp4"


# GET MULTIPLES FRAMES
def get_frames(filename):
    video = cv2.VideoCapture(filename)
    while video.isOpened():
        ret, frame = video.read()
        if ret:
            yield frame
        else:
            break
    video.release()
    yield None


# WORK WITH FRAMES
for f in get_frames(VFILE):
    if f is None:
        break
    cv2.imshow('frame', f)
    if cv2.waitKey(10) == 27:
        break
cv2.destroyAllWindows()


# GET ONE FRAME
def get_frame(filename, index):
    counter = 0
    video = cv2.VideoCapture(filename)
    while video.isOpened():
        ret, frame = video.read()
        if ret:
            if counter == index:
                return frame
            counter += 1
        else:
            break
    video.release()
    return None


# Examining Pixels
frame = get_frame(VFILE, 80)
print('shape ', frame.shape)
# Pixel top-left corner
print('pixel at (0,0)', frame[0, 0, :])
