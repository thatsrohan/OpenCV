import cv2
import sys
s=0
if len(sys.argv)>1:
    s=sys.argv[1]
source=cv2.VideoCapture(s)
cv2.namedWindow('Camera Preview',cv2.WINDOW_NORMAL)
while cv2.waitKey(1)!=27:  #if the key pressed is not the Escape Key,keep looping
    frame=source.read()
    if not frame:
      break
cv2.imshow('Camera Preview',frame)