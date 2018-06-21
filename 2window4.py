﻿import numpy as np
import cv2

cap =cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (450,350))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',frame)  #imgshow
    cv2.imshow('gray',gray)  #imgshow
    cv2.imshow('frame2',frame)  #imgshow
    cv2.imshow('frame3',frame)  #imgshow
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
