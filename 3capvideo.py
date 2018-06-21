import os
import numpy as np
import cv2

filename = 'video.avi'  # .avi or .mp4
frames_per_seconds = 24.0
my_res = '720p'  #1080p

#set resolution for the video VideoCapture
def change_res(cap, width, height):
    cap.set(3,width)
    cap.set(4,height)

STD_DIMENSIONS = {
    "480p": (640,480),
    "720p":(1280,720),
    "1080p":(1920,1080),
    "4k":(3840,2160),
}

def get_dims(cap, res='1080p'):
    width, height = STD_DIMENSIONS["480p"]
    if res in STD_DIMENSIONS:
        width,height = STD_DIMENSIONS[res]
    change_res(cap,width,height)
    return width,height

# Video Encoding, might require additional installs
# Types of Codes: http://www.fourcc.org/codecs.php
VIDEO_TYPE = {
    'avi': cv2.VideoWriter_fourcc(*'XVID'),
    #'mp4': cv2.VideoWriter_fourcc(*'H264'),
    'mp4': cv2.VideoWriter_fourcc(*'XVID'),
}

def get_video_type(filename):
    filename, ext = os.path.splitext(filename)
    if ext in VIDEO_TYPE:
      return  VIDEO_TYPE[ext]
    return VIDEO_TYPE['avi']


cap =cv2.VideoCapture(0)
dims = get_dims(cap, res = my_res)

get_video_type2 = get_video_type(filename)
out = cv2.VideoWriter(filename,get_video_type2,frames_per_seconds,dims)  # dims can be width, height

while True:
    ret, frame = cap.read()
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   # gray video
    out.write(frame)
    # display resulting frame
    cv2.imshow('frame',frame)  #imgshow
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
