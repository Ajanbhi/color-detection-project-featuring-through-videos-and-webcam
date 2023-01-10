import cv2
import numpy as np

cap=cv2.VideoCapture('ballons.mp4') #we can provide path as well
cap.set(cv2.CAP_PROP_FRAME_WIDTH,480)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,220)

while True:
    _,frame=cap.read()
    hsv_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #detecting red color
    low_red=np.array([161,155,84])
    high_red=np.array([179,255,255])
    red_mask=cv2.inRange(hsv_frame,low_red,high_red)
    
    red=cv2.bitwise_and(frame,frame,mask=red_mask)

     #detecting blue color
    low_blue=np.array([103,80,80])
    high_blue=np.array([130,255,255])
    blue_mask=cv2.inRange(hsv_frame,low_blue,high_blue)
    blue=cv2.bitwise_and(frame,frame,mask=blue_mask)

     #detecting green color
    # low_green=np.array([25,52,72])
    # high_green=np.array([102,255,255])
    # green_mask=cv2.inRange(hsv_frame,low_green,high_green)
    # green=cv2.bitwise_and(frame,frame,mask=green_mask)

    cv2.imshow("Frame",frame)
    cv2.imshow("RED",red)
    cv2.imshow("BLUE",blue)
    #cv2.imshow("GREEN",green)

    key=cv2.waitKey(1)
    if(key==27):
        break