import cv2
import pyautogui as pg
import numpy as np

gameImg = cv2.imread('game.png', cv2.IMREAD_UNCHANGED)
mobImg = cv2.imread('mob.png', cv2.IMREAD_UNCHANGED)
mobName = cv2.imread('mobName.png', cv2.IMREAD_UNCHANGED)

result = cv2.matchTemplate(gameImg, mobImg, cv2.TM_CCOEFF_NORMED)

w = mobImg.shape[1]
h = mobImg.shape[0]

minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
#print(maxLoc)
#print(maxVal)

#rectangle = cv2.rectangle(gameImg,maxLoc,(maxLoc[0]+w, maxLoc[1]+h), (0,255,255),2)
#print(rectangle)

threshold = .50

yloc, xloc = np.where(result >= threshold)
print(len(xloc))


# Rectangle x,y,w,h
rectangles = []
for (x,y) in zip(xloc,yloc):
  rectangles.append([int(x), int(y), int(w), int(h)])
  rectangles.append([int(x), int(y), int(w), int(h)])


rectangles,weight = cv2.groupRectangles(rectangles,1,0.2)
print(len(rectangles))

for (x,y,w,h) in rectangles:
  cv2.rectangle(gameImg,(x,y), (x+w,y+h), (0,255,255),2)


cv2.imshow("GameImg", gameImg)
cv2.waitKey()
cv2.destroyAllWindows()



