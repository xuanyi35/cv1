import os
import cv2
import numpy as np
from PIL import Image
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # give path of this py __file__
image_dir = os.path.join(BASE_DIR, "images")
face_casecade = cv2.CascadeClassifier('cascades\data\haarcascades\haarcascade_frontalface_alt.xml')
# recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

people_id =0
label_ids ={}   # dict  [label: id]
y_labels = []   # we need to store integers by using np
x_train = []    # so we link labels to ids

for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg"):
            path = os.path.join(root, file)
            label = os.path.basename(os.path.dirname(path)).replace(" ","_").lower()
            #print(label)
            if not label in label_ids:
                label_ids[label] = people_id
                people_id += 1
            #print(label_ids)
            id_get = label_ids[label]  # get the id based on the file name (label)
            pil_image  = Image.open(path).convert("L")  # gray scale
            size = (500,500)
            final_image = pil_image.resize(size, Image.ANTIALIAS)
            image_array = np.array(final_image,"uint8")   # convert image to np array
            #print(image_array)
            faces = face_casecade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)

            for (x,y,w,h) in faces:
                roi = image_array[y:y+h, x:x+w]
                x_train.append(roi)
                y_labels.append(id_get)

with open("labels.pkl", 'wb') as f:   # write bytes
    pickle.dump(label_ids, f)

recognizer.train(x_train, np.array(y_labels))
recognizer.save("trainer.yml")
