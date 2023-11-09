import pyautogui as py
import time

def healer():
  heal = 'y'
  second = 0 
  
  print("""[INSTRUCTION] \n
        1. Input Heal interval by seconds
        2. Input Hotkey for Mana Potion
        
        """)
  try:
    interval = int(input("Enter in seconds Heal interval: "))
    manaPots = str(input("Input Hotkey for Mana Potion: "))
    manaTime = str(input("nter in seconds Mana Potion interval "))
    
  except():
    print("Enter a valid integer")
  
  while heal == "y":
    time.sleep(interval)
    py.press('3') # Heal
    second = second + 1
    usePotion = second % manaTime
    if usePotion == manaTime:
      py.press(f'{manaPots}') # Potion Hotkey
    
def moonBeam():
  
  heal = 'y'
  second = 0 
  
  print("""[INSTRUCTION] \n
        1. Input buff interval in seconds
        2. Buffs should be in Alt 1-0 sequence
        3. Input Hotkey for Mana Potion
        
        """)
  try:
    interval = int(input("Enter seconds buffs interval: "))
    manaPots = str(input("Input Hotkey for Mana Potion: "))
  except():
    print("Enter a valid integer")
    
  while heal == 'y':
      for i in range(interval): #5mins
          if second == 0 or second >= 300:
              time.sleep(2)   
              py.hotkey('alt','1', interval= .5)   
              py.hotkey('alt','1', interval= .5)   
              py.hotkey('alt','2', interval= .5)   
              py.hotkey('alt','3', interval= .5)   
              py.hotkey('alt','4', interval= .5)   
              py.hotkey('alt','5', interval= .5)   
              py.hotkey('alt','6', interval= .5)
              py.hotkey('alt','7', interval= .5)
              py.hotkey(f'{manaPots}',presses = 3, intervaasl= .5)
              second = 0
          time.sleep(1)
          py.press('2')
          second = second + 1
          print(f'count {second}')
          time.sleep(2)
          py.press('3')
          second = second + 2
          i = i + 1
          time.sleep(1)
          second = second + 1

def runAssistBot():
  print ("Welcome to Assist Bot! Select Option: ")
  print("[1] Full Support")
  print("[2] Healer Only")
  print("[3] Moonbeam Solo")
  print("[4] Mercaba Solo")

  try:
    selection = int(input("Select Option: "))
    if selection > 4:
      print("Not in the List! Select Again.")
      selection = int(input("Select Option: "))

  except ValueError:
    print("Enter a valid integer")
    
  match selection:
    case 1: # FS
      pass
    case 2: # Healer
      healer()
    case 3: # Moonbeam
      moonBeam()
    case 4: # Mercaba
      pass
    case _:
      print("Enter a valid integer")
      


runAssistBot()