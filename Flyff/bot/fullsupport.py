import pyautogui as pg
import time

def fullSupport():
  second = 1
  hotkeyHeal = 1
  hotkeyPots = 5 
  print(f"""[INSTRUCTION] \n
        1. Input buff interval in seconds.
        2. Buffs should be in Alt 1-0 sequence.
        3. [{hotkeyHeal}]Heal and [{hotkeyPots}]Mana Potion.
        """)
  
  healInterval = int(input("Enter seconds Heal Interval: "))
  buffInterval = int(input("Enter seconds Buffs interval: ")) #600 10mins

  healAction = second % healInterval
  buffAction = second % buffInterval
  found = False 
  pg.leftClick(71,649)
  
  for x in range(18000): # 5hrs
    
    time.sleep(1)
    second = second + 1
    #print(x)
    print(second)
   
    if buffAction == 0 or x == 0:
      pg.leftClick(71,649)
      pg.press('esc')
      print("test")
      buffs()
      found = True
      # Target Char
      while found == True:
        try:
          main = pg.locateOnScreen('sora.png', confidence=.9)
          if len(main) > 0 :
            x = main[0]
            y = main[1]
            w = main[2]
            h = main[3]
            mainCoor = (x-5,y,w,h+60)
            pg.leftClick(mainCoor)
            buffs() 
            pg.press('z')
            pg.leftClick(71,167)
            found = False
        except:
            print("No Image")   
      second = second + 12

    if healAction == 0:
      pg.leftClick(71,649)
      print("Action : Using Heal")
      pg.press(f'{hotkeyHeal}')
      currentMouse = pg.position()
      pg.leftClick(currentMouse)

def runApp():
  while True:
    mobTarget()


def mobTarget():
  
  def checkMob():
    target = False
    try:
      while target==False :
        monster = pg.locateOnScreen('giggle.png',confidence=.9)
        #print(monster)
        x = monster[0]
        y = monster[1]
        w = monster[2]
        h = monster[3]
        monsterCoordinate = (x-5,y,w,h+30)
        
        if len(monster) >= 1:
          
          print(len(monsterCoordinate))
          pg.leftClick(monsterCoordinate)
          target = True
          monster= ""
          return True
    except :
        print("monster")

  def checkTarget(arrow):
    try:
        while arrow == True :
            arrow = pg.locateOnScreen('arrow.png',confidence=.7)
            continue
        if len(arrow <= 0) :
            print("arrow = false")
            arrow = False
            checkMob()
    except :
          print("no arrow")
          
          
  checker = checkMob()
  checkTarget(checker)

def buffs():
  print("Action : Using Buffs.....")
  pg.hotkey('alt','1', interval= .5)   
  pg.hotkey('alt','1', interval= .5)   
  pg.hotkey('alt','2', interval= .5)   
  pg.hotkey('alt','3', interval= .5)   
  pg.hotkey('alt','4', interval= .5)   
  pg.hotkey('alt','5', interval= .5)   
  pg.hotkey('alt','6', interval= .5)
  pg.hotkey('alt','7', interval= .5)
  pg.hotkey('alt','8', interval= .5)
  pg.hotkey('alt','9', interval= .5)
  pg.hotkey('alt','0', interval= .5)

#fullSupport()
#mobTarget()
runApp()
#pg.displayMousePosition()