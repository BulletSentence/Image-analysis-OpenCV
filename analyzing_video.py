import matplotlib.pyplot as plt
import cv2
import numpy as np


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
print('pixel at (0,0) (B,G,R)', frame[0, 0, :])


# Displaying a frame without color fix
plt.imshow(frame)
plt.show()

# Display a frame with color fix
fix_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
print('Pixel at (0,0) ', fix_frame[0,0,:])
plt.imshow(fix_frame)
plt.show()

# For FIX Errors (Run on Bash)
# export QT_DEVICE_PIXEL_RATIO = 0
# export QT_AUTO_SCREEN_SCALE_FACTOR = 1
# export QT_SCREEN_SCALE_FACTORS = 1
# export QT_SCALE_FACTOR = 1

# CROP video frame
plt.imshow(fix_frame[240:480, 320:640])
plt.show()

# Adjusting britghtness
darker = 0.2 * fix_frame
darker = darker.astype(np.uint8)
plt.imshow(darker)
plt.show()

# Drawing figures into a frame
