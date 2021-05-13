import cv2
import time
import mediapipe as mp

#first commit using pycharm

cap = cv2.VideoCapture(0);

while True:
        success, img = cap.read();
        cv2.imshow("Image",img)
        cv2.waitKey(1)