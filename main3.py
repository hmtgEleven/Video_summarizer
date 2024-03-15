# VIDEO SUMMARIZATION
#Project by Himanshu Mittal

# importing the libraries required
import cv2
import numpy as np

# reading the input file
video = cv2.VideoCapture('demo3_input.mp4')

# checking for an exception if video does not open
if not video.isOpened():
    print("Error: Could not open video file.")
    exit()

# storing the dimensions of the frames in video
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
# setting the threshold value of difference in pixels of frames
threshold = 38.0

# defining about the output video
writer = cv2.VideoWriter(
    'OUTPUT_Three.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (width, height))

# reading the frames from video
ret, frame1 = video.read()

# checking for an error if unable to read frames
if not ret:
    print("Error: Could not read the first frame.")
    exit()

prev_frame = frame1

# defining variables to keep the count of unique,common and total frames respectively
uf = 0
cf = 0
tf = 0

# loop to read all the frames
while True:
    ret, frame = video.read()

    if not ret:
        break  # breaking the loop if there are no more frames

    # calculating the diff in pixels of adjcent frames
    difference = np.sum(np.abs(frame - prev_frame)) / np.size(frame)

    if difference > threshold:  # if the diff is more than the threshold than write that frame to the output video
        writer.write(frame)
        prev_frame = frame
        uf += 1
    else:  # if the diff is not more than threshold than just make this frame the prev_frame
        prev_frame = frame
        cf += 1

    # displaying the frames while working on this loop
    cv2.imshow('frame', frame)
    tf += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):  # press q to quit the process in between
        break


print("Unique frames: ", uf)
print("Common frames: ", cf)
print("Total frames: ", tf)

# closing all the processes and releasing the resources
video.release()
writer.release()
cv2.destroyAllWindows()
