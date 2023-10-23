# Importing all necessary libraries
import cv2
import os

# Read the video from specified path
cam = cv2.VideoCapture("smile/here.mp4")

try:

    # creating a folder named data
    if not os.path.exists('data'):
        os.makedirs('data')

# if not created then raise error
except OSError:
    print('Error: Creating directory of data')

# frame
currentframe = 0

while (True):

    # reading from frame
    ret, frame = cam.read()

    if ret:
        name = './data/frame{:06d}.png'.format(currentframe)
        print('Creating...' + name)

        # writing the extracted images
        cv2.imwrite(name, frame)
        currentframe += 1
    else:
        break


# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()
