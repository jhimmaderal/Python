import pyautogui as pg
import time
import cv2 as cv
import random

def autoDetect() :
  counter = 0
  noMob = 0
  
  def moveCam():
    print('Moving Camera')
    pg.keyDown('left')
    time.sleep(.5)
    pg.keyUp('left')

  def movePlayer():
    movementKey = ["w", "a", "s", "d"]
    randNum = random.randrange(len(movementKey))
    randMove1 = movementKey[randNum]
    randMove2 = movementKey[randNum]
    print("Action Moving Player...")
    pg.keyDown(randMove1)
    pg.keyDown(randMove2)
    time.sleep(3)
    pg.keyUp(randMove1)
    pg.keyUp(randMove2)

  while True:
    try:     
      # Timer
      counter = counter +  1
      
      # Checking Validations
      mob = pg.locateOnScreen('resources/mobs/wagsaac.png',confidence=.8)
      # Monster Coordinate
      x = mob[0]
      y = mob[1]
      w = mob[2]
      h = mob[3]
      
      clickCoordinates = (x-30,y+50,w,h) # Mobs

      if len(mob) > 1 :
        try:
          arrowBotRight = pg.locateOnScreen('resources/arrowRed.png',confidence=.9)
          arrowBotLeft = pg.locateOnScreen('resources/arrowRed2.png',confidence=.9)
          
          print("Gotcha !")
          pg.leftClick(clickCoordinates)  
          #pg.moveTo(clickCoordinates)
          attackTime = 0

          # Attacking Mobs
          while len(arrowBotRight) > 0 or len(arrowBotLeft) > 0:
            attackTime = attackTime + 1
            #petFilter = pg.locateOnScreen('resources/pet.png',confidence=.8)
            arrowBotRight = pg.locateOnScreen('resources/arrowRed.png',confidence=.9)
            arrowBotLeft = pg.locateOnScreen('resources/arrowRed2.png',confidence=.9) 
            pg.press('1')
            print(f"Attacking Monster!")

            if attackTime == 20:
              pg.press('esc')
              moveCam()
              movePlayer()
              attackTime = 0

        except:
          pass
          
    # Checking Error
    except:
      noMob = noMob + 1
      
      # Variable Timers
      camTimer = noMob % 20
      noMobTimer = noMob % 15

      # Move Player
      if noMobTimer == 0:
        movePlayer()

      # Change Camera Angle
      if camTimer == 0:
        moveCam()
        
      pass
      
autoDetect()


