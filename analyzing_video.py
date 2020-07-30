import numpy as np
import cv2
import matplotlib.pyplot as plt

VFILE = "video/Teste.mp4"


def get_frames(filename):
    video = cv2.VideoCapture(filename)
    while video.isOpened():
        ret, frame = video.read()
