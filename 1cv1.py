import numpy as np
import cv2

# Load an color image in grayscale
pic = input("Enter the picture's name: ")
picN = 'G:\pictures/\/' + pic
img = cv2.imread(picN,1)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('image',500,500)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('image',img_gray)
    name = "G:\Gimages/\/"+pic
    cv2.imwrite(name,img_gray)
    cv2.destroyAllWindows()
