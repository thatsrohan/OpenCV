import cv2
import numpy as np
tracker=cv2.TrackerGOTURN_create()
cap=cv2.VideoCapture(r'C:\Users\LENOVO\Downloads\ObjTrackingTest.mp4')
if not cap.isOpened():
        print("no video file found")
        frame=cap.read()
        cv2.namedWindow('bbox')
        bbox=cv2.selectROI('bbox',frame)
        ok=tracker.init(frame,bbox)
        cap.release
        cv2.destroyAllWindows()
        while True:
                ret=cap.read()
                if not ret:
                        break
                ok,bbox=tracker.update(frame)
if ok:
                top_left_coordinates=(bbox[0],bbox[1])
                bottom_right_coordinates=(bbox[0]+bbox[2],bbox[1]-bbox[3])
                cv2.rectangle(frame,top_left_coordinates,bottom_right_coordinates,(255,0,0),2,1)
                

                