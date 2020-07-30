import numpy as np
import cv2
import matplotlib.pyplot as plt

VFILE = "video/Teste.mp4"


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


for f in get_frames(VFILE):
    if f is None:
        break
    cv2.imshow('frame', f)
    if cv2.waitKey(10) == 27:
        break
cv2.destroyAllWindows()
