import cv2 as cv
import numpy as np
import pyautogui as pg


gameImg = cv.imread('resources/game.png', cv.IMREAD_UNCHANGED)
mobImg = cv.imread('resources/mushpang.png', cv.IMREAD_UNCHANGED)

result = cv.matchTemplate(gameImg,mobImg, cv.TM_CCOEFF_NORMED )

# get best match position
minVal, maxVal, minLoc, maxLoc = cv.minMaxLoc(result)

print('Best match top left positon %s' % str(maxLoc))
print('Best match confidence %s' % maxVal)

threshold = 0.8

if maxVal >= threshold:
  print('Found Mobs')

  # get dimension of mobs
  mobWidth = mobImg.shape[1]
  mobHeight = mobImg.shape[0]
  
  topLeft = maxLoc
  botRight = (topLeft[0] + mobWidth, topLeft[1] + mobHeight)
 
  cv.rectangle(gameImg, topLeft, botRight, color=(0,255,0), thickness=2,lineType=cv.LINE_4)
  
  cv.imshow('Result', gameImg)
  cv.waitKey()
  #cv.imwrite('result.jpg', gameImg) # save image

else:
  print('No Mobs')
