# Face tracking turret

Welcome to face-tracking-turret module! This repository contains a few project files for making your servo-motor rotate along the movement of a camera-detected face, using Haar Cascades library. This module is composed of two python files that are responsible for recognizing your face with Haar Cascade data. As these files draw a box around your face to identify it, the Arduino file will receive this information and move the servo-motor accordingly. 

For this to work, you need to have Haar Cascades library, openCV, and Arduino IDE installed on your computer. I particularly used my Arduino Uno, but compatibility can be set with little adjustments made to the code. 

