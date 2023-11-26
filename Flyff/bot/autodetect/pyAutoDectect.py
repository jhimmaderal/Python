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
    time.sleep(2)
    pg.keyUp(randMove1)
    pg.keyUp(randMove2)

  def attackMode():
    try:
          arrowRedRight = pg.locateOnScreen('resources/arrowRed.png',confidence=.9, grayscale=True)
          arrowRedLeft = pg.locateOnScreen('resources/arrowRed2.png',confidence=.9, grayscale=True)
          arrowBlueRight = pg.locateOnScreen('resources/arrowBlue.png',confidence=.9, grayscale=True)
          arrowBlueLeft = pg.locateOnScreen('resources/arrowBlue2.png',confidence=.9, grayscale=True)
          
          print("Gotcha !")
          pg.leftClick(clickCoordinates)  
          #pg.moveTo(clickCoordinates)
          attackTime = 0

          # Attacking Mobs
          while len(arrowRedRight) > 0 or len(arrowRedLeft) > 0 or len(arrowBlueRight) > 0 or len(arrowBlueLeft) > 0:
            attackTime = attackTime + 1
            #petFilter = pg.locateOnScreen('resources/pet.png',confidence=.8)
            arrowRedRight = pg.locateOnScreen('resources/arrowRed.png',confidence=.9, grayscale=True)
            arrowRedLeft = pg.locateOnScreen('resources/arrowRed2.png',confidence=.9, grayscale=True)
            arrowBlueRight = pg.locateOnScreen('resources/arrowBlue.png',confidence=.9, grayscale=True)
            arrowBlueLeft = pg.locateOnScreen('resources/arrowBlue2.png',confidence=.9, grayscale=True) 
            pg.press('1')
            print(f"Attacking Monster!")

            if attackTime == 30:
              pg.press('esc')
              moveCam()
              movePlayer()
              attackTime = 0
    except:
        pass
      
  while True:
    try:     
      # Timer
      counter = counter +  1
      
      # Checking Validations
      time.sleep(1)
      mob = pg.locateOnScreen('resources/mobs/greemong.png',confidence=.9)
      print(mob)
      
      # Monster Coordinate
      x = mob[0]
      y = mob[1]
      w = mob[2]
      h = mob[3]

      # Big monster -40 +40
      # Small monster -20 +40
      clickCoordinates = (x,y,w-15,h+40) # Mobs

      if len(mob) > 1 :
          attackMode()
          
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


