
import numpy as np
import cv2

from utils import CFEVideoConf, image_resize

cap = cv2.VideoCapture(0)

save_path = 'g:/videos/watermark.mp4'
frames_per_seconds = 24
config = CFEVideoConf(cap, filepath=save_path, res='480p')  # used to change the resolution
out = cv2.VideoWriter(save_path, config.video_type, frames_per_seconds, config.dims)

img_path = 'G:\pictures/cats.png'
logo = cv2.imread(img_path,-1)
#watermark = cv2.cvtColor(watermark, cv2.COLOR_BGR2BGRA)
watermark = image_resize(logo, height = 100)  # gray scale, do not have number 3
watermark = cv2.cvtColor(watermark, cv2.COLOR_BGR2BGRA)      #has number 3
#cv2.imshow('watermark', watermark)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    # used to demonstrate
    # start_cord_x = 50
    # start_cord_y = 150
    # stroke = 2
    # color = [255,255,0]
    # w = 100
    # h = 200
    # end_of_x = start_cord_x + w
    # end_of_y = start_cord_y + h
    # cv2.rectangle(frame, (start_cord_x,start_cord_y),(end_of_x, end_of_y), color, stroke)
    # print(frame[start_cord_x: end_of_x, start_cord_y:end_of_y])

    frame_h, frame_w, frame_c = frame.shape                     #(720, 1280, 3)
    #print(frame.shape)
    #gray = cv2.cvtColor(frame.copy(), cv2.COLOR_BGR2GRAY)                                                            # (720, 1280, 3)
    #print(gray.shape)
                                               # (720, 1280)
    # overlay with 4 channels BGR & Alpha
    overlay = np.zeros((frame_h,frame_w, 4), dtype = 'uint8')    # every pixel value is 0
    #overlay[100:200, 100:200] = (255,0,0,1)                     # B G R A  [st_y: e_y, st_x: e_x]
    #cv2.imshow('overlay', overlay)
    watermark_h, watermark_w,watermark_c = watermark.shape
    for i in range(0, watermark_h):     #individual pixel
        for j in range(0,watermark_w):
            # watermark[i,j]   # RBGA
            if watermark[i,j][3] !=0:
                h_offset = frame_h - watermark_h - 10
                w_offset = frame_w - watermark_w - 10
                overlay [h_offset + i,w_offset + j] = watermark[i,j]

    cv2.addWeighted(overlay, 0.70, frame, 1.0, 0, frame)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
    out.write(frame)
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()
