import cv2
import uuid
import os
import time
import labelImg

face_cascade = cv2.CascadeClassifier('C:\SGU\Python\Trash_detection_AI\haarcascade\haarcascade_trash.xml')
lables = ['thumbup', 'thumbdown', 'thankyou', 'livelong']
number_imgs = 5

img_path = os.path.join('Tensorflow', 'workspace', 'images', 'collectedimages')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 4)
    for(x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
    cv2.imshow('frame', frame) 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()