import pyautogui as py
import time

def fullSupport():
  hotkeyHeal = 1
  hotkeyPots = 5 
  print(f"""[INSTRUCTION] \n
        1. Input buff interval in seconds.
        2. Buffs should be in Alt 1-0 sequence.
        3. [{hotkeyHeal}]Heal and [{hotkeyPots}]Mana Potion.
        """)
  
  healInterval = int(input("Enter seconds Heal Interval: (Ave 40-50sec): "))
  buffInterval = int(input("Enter seconds buffs interval: "))

  

def healer():
  start = 'y'
  second = 0 

  print("""[INSTRUCTION] \n
        1. Input Heal interval by seconds
        2. Input Hotkey for Mana Potion
        """)
  try:
    botDuration = int(input("Enter Bot Duration by Minute: "))
    healInterval = int(input("Enter in seconds Heal interval: "))
    #hotkeyPots = int(input("Input Hotkey for Mana Potion: "))
    #manaTime = int(input("Enter in seconds Mana Potion interval: "))
    
    py.leftClick(9,7)
    
    botDurationMin  = botDuration * 60  
  except ValueError:
    print("Enter a valid integer")
    healer()
    
  except UnboundLocalError:
    print("Enter a valid integer \n")
    healer()
  
  finally:
    while start == "y":
      for  x in range(botDurationMin):
        time.sleep(1)
        print(f'Timer: {x}')
        second = second + 1
        
        actionTimer = second % healInterval
        #print(actionTimer)
        #actionPotion = second % manaTime
        #print(actionPotion)
        buffTimer = x % 300
      
      
        if actionTimer == 0: # Heal
          py.press('1') # Heal
        #elif actionPotion == 0:
        #  py.press(f'{hotkeyPots}') # Potion Hotkey

        elif buffTimer == 0 :
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
        
def moonBeam():
  start = 'y'
  second = 0 
  print("""[INSTRUCTION] \n
        1. Input buff interval in seconds.
        2. Buffs should be in Alt 1-0 sequence.
        3. Input Hotkey for Moonbeam, Heal and Mana Potion.
        """)
  try:
    botDuration = int(input("Enter Bot Duration by Minute: "))
    buffInterval = int(input("Enter seconds buffs interval: "))
    hotkeyMoon = int(input("Input Hotkey for Moonbeam: "))
    hotkeyHeal = int(input("Input Hotkey for Heal: "))
    hotkeyPots = int(input("Input Hotkey for Mana Potion: "))

    botDurationMin  = botDuration * 60
    py.leftClick(9,7)
  except ValueError:
    print("Enter a valid integer")
    moonBeam()
  
  finally:
    while start == 'y':
      for x in range(botDurationMin): 
        time.sleep(1)
        second = second + 1

        botTimer = x % 600
        healTimer = x % 3
        moonTimer = x % 2
        buffTimer = x % buffInterval        

        
        if botTimer == 0:
          print(f"Your Using this Bot for {x/60} minutes.")
        
        if buffTimer == 0 :
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
          py.press(f'{hotkeyPots}',presses = 3, interval= .5)

        if moonTimer == 0:
          print("Action : Using Moonbeam")
          py.press(f'{hotkeyMoon}')
          
        if healTimer == 0:
          print("Action : Using Heal")
          py.press(f'{hotkeyHeal}')       
        
def merkaba():
  start = 'y'
  second = 0 
  
  hotkeyMerk = 2
  hotkeyPrev = 3
  hotkeyHeal = 1
  hotkeyPots = 4
  buffDuration = 420
  
  print(f"""[INSTRUCTION] \n
        1. Input buff interval in seconds.
        2. Buffs should be in Alt 1-0 sequence.
        3. Place Hotkey for [{hotkeyMerk}]Merkaba, [{hotkeyPrev}]Prevention, [{hotkeyHeal}]Heal and [{hotkeyPots}]Mana Potion.
        """)
  try:
    #botDuration = int(input("Enter Bot Duration by Minute: "))
    #buffInterval = int(input("Enter seconds buffs interval: "))
    #prevInterval = int(input("Enter seconds Prevention interval: "))
    merkInterval = int(input("Enter seconds Merkava interval: (Ave 40-50sec): "))
    
    botDurationMin  = 60 * 60
    py.leftClick(9,7)
  except ValueError:
    print("Enter a valid integer")
    merkaba()
  except UnboundLocalError:
    print("Enter a valid integer")
    merkaba()
  
  finally:
    while start == 'y':
      for x in range(botDurationMin):
        time.sleep(1)
        second = second + 1
        #print(x)
        print(second)
        
        botTimer = second % 480 #evey 5 mins
        merkabaTimer = second % merkInterval
        #merkabaRemTimer = second % (merkInterval-5)
        buffTimer = second % buffDuration
        buffRemTimer = second % (buffDuration - 10)      
      
        if botTimer == 0:
          print(f"Your Using this Bot for {second/60} minutes.")

        elif buffRemTimer == 0 :
          print("Reminder : Buffing will start in 10sec! ")   
          
        elif buffTimer == 0 or x == 0:
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
          #py.press(f'{hotkeyPots}',presses = 1, interval= .5)
          second = second + 5

        #elif merkabaRemTimer == 0: # Merkaba
        #  print("Reminder : Using Merkaba in 5sec")
          
        elif merkabaTimer == 0: # Merkaba
          print("Action : Using Merkaba")
          py.press('esc')
          py.press(f'{hotkeyMerk}')
          time.sleep(1)
          second = second + 1
          
          print("Action : Prevention")
          py.press(f'{hotkeyPrev}')
          time.sleep(1)
          second = second + 1
          
          print("Action : Using Heal")
          py.press(f'{hotkeyHeal}',presses= 7, interval= 1)
          second = second + 7
                    
          print("Action : Using Merkaba")
          py.press(f'{hotkeyMerk}')
          time.sleep(1)
          second = second + 1
          
          print("Action : Prevention")
          py.press(f'{hotkeyPrev}')
          time.sleep(1)
          second = second + 1
          
          print("Action : Using Heal")
          py.press(f'{hotkeyHeal}',presses= 5, interval= 1)
          second = second + 5
               
        #elif prevTimer == 0: # Reminder 
          #print("Action : Prevention")
          #py.press(f'{hotkeyPrev}')

def autoFarm():
  for x in range(0,10):
    res1 = py.locateOnScreen('voitName.png',confidence=.7)
  try:   
    if len(res1) >= 1:
      print(res1)
      py.leftClick(res1)
      time.sleep(2)

  except:
    print("No Image")

                  
def runAssistBot():
  print ("Welcome to Assist Bot! Select Option: ")
  print("[1] Full Support")
  print("[2] Healer Only")
  print("[3] Moonbeam Solo")
  print("[4] Merkaba Solo")
  print("[5] Auto Farm")

  try:
    selection = int(input("Select Option: "))
    if selection > 4:
      print("Not in the List! Select Again.")
      selection = int(input("Select Option: "))

  except ValueError:
    print("Enter a valid integer \n")
    runAssistBot()
    
  except UnboundLocalError:
    print("Enter a valid integer \n")
    runAssistBot()
    
  match selection:
    case 1: # FS
      pass
    case 2: # Healer
      healer()
    case 3: # Moonbeam
      moonBeam()
    case 4: # Merkaba
      merkaba()
    case 5: # Auto Farm
      pass
    case _:
      print("Enter a valid integer")
      
runAssistBot()