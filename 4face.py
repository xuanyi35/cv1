import numpy as np
import cv2
import pickle 

face_casecade = cv2.CascadeClassifier('cascades\data\haarcascades\haarcascade_frontalface_alt.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")
labels = {}      #person name : id
with open("labels.pkl", 'rb') as f:   # read bytes
    old_labels = pickle.load(f)
    labels = {v:k for k,v in old_labels.items()} # reverse key and value


cap =cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)    # faces can be detected in gray scale
    faces = face_casecade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for (x,y,w,h) in faces:
        #print(x,y,w,h)
        roi_gray = gray[y:y+h, x:x+w]   # region of interest(face)
        roi_color = frame[y:y+h, x:x+w]

        # recognizer (from cv2)
        id_get, conf = recognizer.predict(roi_gray)
        if conf >= 45 and conf <=85:
            #print(labels[id_get])
            font = cv2.FONT_HERSHEY_SIMPLEX
            name = labels[id_get]
            color = (255, 255, 255)
            stroke = 2
            cv2.putText(frame, name, (x,y), font,1, color, stroke,cv2.LINE_AA)



        #img_item = "myface.png"
        #cv2.imwrite(img_item, roi_gray)   #used to save an image

        color = (255,300,0)  # BGR 0-255
        stroke = 2
        end_of_x = x + w
        end_of_y = y + h
        cv2.rectangle(frame, (x,y),(end_of_x, end_of_y), color, stroke)

    # display
    cv2.imshow('frame',frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
