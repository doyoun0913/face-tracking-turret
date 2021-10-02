#Mechatronics Project 1: Face Tracking Turret (Facial Cascade)
#Reference to Alexander Mordvintsev & Abid K, authors of "OpenCV-Python Tutorials Documentation, Release 1"

import cv2 as cv
import numpy as np

face_cascade = cv.CascadeClassifier('C:\\Users\\logan\\AppData\\Local\\Programs\\Python\\Python37-32\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('C:\\Users\\logan\\AppData\\Local\\Programs\\Python\\Python37-32\\Lib\\site-packages\\cv2\\data\\haarcascade_eye.xml')

img = cv.imread('C:\\Users\\logan\\Desktop\\Logan Kim\\Photography\\Pictures\\Camera Roll\\my_face.jpg')
gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


# detecting face from the image
faces = face_cascade.detectMultiScale(gray_image, 1.3, 5, 10)  # output of [[517 135 397 397]], [517 135] for x and y, [397 397] for width and height
for (x,y,w,h) in faces:
    img = cv.rectangle(img,(x,y),(x+w,y+h),(0,69,255),2)
    roi_gray = gray_image[y:y+h, x:x+w]  # slicing off the face from the image(grayscale)
    roi_color = img[y:y+h, x:x+w]  # slicing off the face from the image(color)

    # detecting eyes from the face
    eyes = eye_cascade.detectMultiScale(roi_gray, 1.2, 15, 0)
    for (ex,ey,ew,eh) in eyes:
        cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)

# display outcome
cv.imshow('Image with face detection',img)
cv.waitKey(0)
cv.destroyAllWindows()
