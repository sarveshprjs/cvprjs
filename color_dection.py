import cv2
import numpy as np
from PIL import Image
from util import get_limit

cap=cv2.VideoCapture(0)
yellow=[0,255,255]
while(True):
    ret,frame=cap.read()
    hsv_img=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lowerLimit,upperLimit = get_limit(color=yellow)

    mask=cv2.inRange(hsv_img,lowerLimit,upperLimit)
    mask_=Image.fromarray(mask)
    bbox=mask_.getbbox()
    if bbox is not None:
        x1,y1,x2,y2=bbox
        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),5)
        cv2.imshow('frame', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break