#!/usr/bin/env python
import rospy
import cv2
import numpy as np
from std_msgs.msg import Int16

rospy.init_node("face_detection_node")

rate = rospy.Rate(66) #1000/15 = 66.6667

pubX = rospy.Publisher('servoX', Int16, queue_size=1)
pubY = rospy.Publisher('servoY', Int16, queue_size=1)

# detector wajah
deteksi_wajah = cv2.CascadeClassifier('/home/didik/tracker2D/src/tracker/src/haarcascades/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640) # 640 x 480 || 1280 x 720
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

global xcpy 
global ycpy

def image_processing():
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # deteksi wajah
    wajah = deteksi_wajah.detectMultiScale(gray, 1.1, 1,  minSize=(150, 150)) #(gray, scale factor, neighboard)
    banyak= "banyak wajah terdeteksi : " + str(len(wajah))
    cv2.putText(frame, banyak, (5,20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 1 ) #10,30
    global xcpy 
    global ycpy
    #publish wajah terdeteksi
    if len(wajah) is not 0:
        for (x,y,w,h) in wajah:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)
            
            posisiX = x+w/2
            posisiY = y+h/2
            
            serialX = 320-posisiX
            serialY = 240-posisiY
            xcpy = serialX
            ycpy = serialY
            
            pubX.publish(serialX)
            pubY.publish(serialY)
            
            rospy.loginfo("posisi x : %d ; posisi y : %d ; serial x : %d ; serial y : %d", posisiX, posisiY, serialX, serialY)
            
            cv2.putText(frame, "Didik", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (3, 255, 255), 1 ) #10,30

    else :
        print("didik")
        x = 0 # no change
        y = 0 # no change
        pubX.publish(x)
        pubY.publish(y)
        rospy.loginfo("Tidak terdeteksi wajah ; serial x : %d ; serial y : %d", x, y)

    cv2.imshow('Hasil',frame)
    cv2.waitKey(10)

if __name__ == "__main__":
    while not rospy.is_shutdown():
        try:
            image_processing()
            rate.sleep()
        except rospy.ROSInterruptException, e:
            rospy.loginfo(e)

