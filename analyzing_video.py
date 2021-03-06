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
# for f in get_frames(VFILE):
#     if f is None:
#         break
#     cv2.imshow('frame', f)
#     if cv2.waitKey(10) == 27:
#         break
# cv2.destroyAllWindows()


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
# plt.imshow(frame)
# plt.show()

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
frame = get_frame(VFILE, 200)
cv2.circle(
    frame,
    center=(830,200),
    radius=50,
    color=(0,0,255),
    thickness=8)
fixed_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
plt.imshow(fixed_frame)
plt.show()


# Processing the video
fourcc = cv2.VideoWriter_fourcc('M', 'P', '4', 'V')
video_out = cv2.VideoWriter("new_vid.mp4", fourcc, 30, (640, 480))

counter = 0
for frame in get_frames(VFILE):
    if frame is None:
        break
    cv2.putText(frame, text=str(counter),
                org=(100, 100), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=1, color=(0, 255, 0), thickness=2)
#    cv2.imshow('Video Render', frame)
#    if cv2.waitKey(10) == 27:
#        break
    video_out.write(frame)
    counter += 1
video_out.release()
print("Render Completed")

# Finding the total video frames
video = cv2.VideoCapture(VFILE)
count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
video.release()
print('frame count: ', count)

# Collage
skip_frames = count // 15
frames = []
counter = 0
for f in get_frames(VFILE):
    if counter % skip_frames == 0:
        frames.append(f)
    counter += 1

row1 = np.concatenate(frames[0:5], axis=1)
row2 = np.concatenate(frames[5:10], axis=1)
row3 = np.concatenate(frames[10:15], axis=1)
collage = np.concatenate((row1, row2, row3), axis=0)
collage = cv2.cvtColor(collage, cv2.COLOR_BGR2RGB)
plt.imshow(collage)
plt.show()