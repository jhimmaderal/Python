import cv2 as cv
import numpy as np

blank  = np.zeros((500,500,3), dtype = 'uint8') # height, width, color channels
print(blank.shape)
#cv.imshow('Blank', blank)

def blankImg():
# Paint the image a certain colour
  blank[200:300, 300:400] = 0,255,0
  cv.imshow('Green', blank)

def rectangles() :
  cv.rectangle(blank,(0,0),(250,250),(0,255,0), thickness=-1) # Green
  cv.imshow('Rectangle', blank)
  cv.rectangle(blank,(0,500),(250,250),(255,255,0), thickness=cv.FILLED) # Cyan
  cv.imshow('Rectangle', blank)
  cv.rectangle(blank,(500,0),(250,250),(255,0,0), thickness=cv.FILLED) # Blue
  cv.imshow('Rectangle', blank)
  cv.rectangle(blank,(500,500),(250,250),(0,0,255), thickness=5) # Red
  cv.imshow('Rectangle', blank)

def circle():
  cv.rectangle(blank,(0,0),(250,250),(0,255,255), thickness=3)
  cv.circle(blank,(blank.shape[1]//2, blank.shape[0]//2),40,(0,0,255), thickness=3)
  cv.imshow('Circle', blank)

def line():
  cv.rectangle(blank,(0,0),(blank.shape[1]//2, blank.shape[0]//2),(0,255,0), thickness=-1) # Green
  cv.circle(blank,(blank.shape[1]//2, blank.shape[0]//2),40,(0,0,255), thickness=-1)
  cv.line(blank,(100,250),(300,400),(255,255,255), thickness=3)
  cv.imshow('Line',blank)

def textImage():
  cv.putText(blank, "Hello", (100,225), cv.FONT_HERSHEY_TRIPLEX, 1.0,(0,255,0),2)
  cv.imshow('Text', blank)

textImage()

cv.waitKey(0)