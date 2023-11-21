import cv2 as cv
import numpy as np
import os 
import sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))

gameImg = cv.imread('resources/game3.png', cv.IMREAD_UNCHANGED)
mobImg = cv.imread('resources/mushpang2.png', cv.IMREAD_UNCHANGED)

result = cv.matchTemplate(gameImg,mobImg, cv.TM_CCOEFF_NORMED )
print(result)

threshold = 0.6
locations = np.where(result >= threshold)
print(locations)

# zip those into postion tuplse
locations = list(zip(*locations[::-1]))
print(locations)

if locations:
  print('Found Mobs')

  mobWidth = mobImg.shape[1]
  mobHeight = mobImg.shape[0]
  lineColor = (0,255,0)
  lineType = cv.LINE_4

  for loc in locations:

    topLeft = loc
    botRight = (topLeft[0] + mobWidth, topLeft[1] + mobHeight)

    cv.rectangle(gameImg, topLeft,botRight,lineColor,lineType)
  
  cv.imshow('Result', gameImg)
  cv.waitKey()

else:
  print('No Mobs Found')