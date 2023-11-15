import pyautogui as py
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
  py.leftClick(71,649)
  
  for x in range(18000): # 5hrs
    
    time.sleep(1)
    second = second + 1
    print(x)
    print(second)
   
    if buffAction == 0 or x == 0:
      py.leftClick(71,649)
      py.press('esc')
      print("test")
      buffs()
      found = True
      # Target Char
      while found == True:
        try:
          main = py.locateOnScreen('sora.png', confidence=.9)
          if len(main) > 0 :
            x = main[0]
            y = main[1]
            w = main[2]
            h = main[3]
            mainCoor = (x-5,y,w,h+60)
            py.leftClick(mainCoor)
            buffs() 
            py.press('z')
            py.leftClick(71,167)
            found = False
        except:
            print("No Image")   
      second = second + 12

    if healAction == 0:
      py.leftClick(71,649)
      print("Action : Using Heal")
      py.press(f'{hotkeyHeal}')
      currentMouse = py.position()
      py.leftClick(currentMouse)

def buffs():
  print("Action : Using Buffs.....")
  py.hotkey('alt','1', interval= .5)   
  py.hotkey('alt','1', interval= .5)   
  py.hotkey('alt','2', interval= .5)   
  py.hotkey('alt','3', interval= .5)   
  py.hotkey('alt','4', interval= .5)   
  py.hotkey('alt','5', interval= .5)   
  py.hotkey('alt','6', interval= .5)
  py.hotkey('alt','7', interval= .5)
  py.hotkey('alt','8', interval= .5)
  py.hotkey('alt','9', interval= .5)
  py.hotkey('alt','0', interval= .5)

fullSupport()
#py.displayMousePosition()