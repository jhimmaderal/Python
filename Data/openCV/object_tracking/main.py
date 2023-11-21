import cv2 as cv
from tracker import *

# create Tracker object
tracker = EuclideanDistTracker()

cap = cv.VideoCapture("highway.mp4")


# 1. Object Detection from Stable Camera
object_dectector = cv.createBackgroundSubtractorMOG2(history=100,varThreshold=50)

while True:
  ret, frame = cap.read()
  height, width, _ = frame.shape
  #print(height,width)

  # Extract Region of interest
  roi = frame[340:720,500:800] # from Start:End H & W

  # Object Detection
  mask = object_dectector.apply(roi)
  _, mask = cv.threshold(mask,254,255, cv.THRESH_BINARY) # Remove Shadow (gray or below color in mask)
  contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE) 

  detections = []
  
  for cnt in contours :
    # Calculate Area and remove small element
    area = cv.contourArea(cnt)

    if area >100:
      #cv.drawContours(roi, [cnt], -1,(0,255,0),2) 
      x,y,w,h = cv.boundingRect(cnt)
      detections.append([x,y,w,h])
      #print(detections)

  # 2. Object tracking
  boxsId = tracker.update(detections)
  for boxId in boxsId:
    x,y,w,h,id = boxId
    cv.putText(roi, str(id), (x,y-15), cv.FONT_HERSHEY_PLAIN,2,(255,0,0),2)
    cv.rectangle(roi,(x,y), (x+w,y+h), (0,255,0),3 )

  cv.imshow("ROI", roi)
  cv.imshow("Frame", frame)
  cv.imshow('Mask', mask)
  

  key = cv.waitKey(30)
  if key == 27: # Escape
    break

cap.release()
cv.destroyAllWindows()