import pyautogui as pg
import time



for x in range(0,1):
  res1 = pg.locateOnScreen('sora.png',confidence=.9)
  x = res1[0]
  y = res1[1]
  w = res1[2]
  h = res1[3]
  # clickCoordinates = (x-5,y,w,h+25) # Mobs
  clickCoordinates = (x,y,w,h+50) # Char
  try:   
    if len(res1) >= 1:
      print(res1)
      pg.leftClick(clickCoordinates)
      time.sleep(2)
  except:
    print("No Image")


