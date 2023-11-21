import Listing as list
import ministry as min
import priceChange as price
import costChange as cost
import uom as uom
import pyttsx3
import os

def start():
  engine = pyttsx3.init()
  voices = engine.getProperty('voices')
  engine.setProperty('voices', voices[0].id)
  engine.runAndWait()
  items = {1:"Listing", 2:"UOM", 3:"Price Change", 4:"Cost Change", 5:"Ministry"}

  pyttsx3.speak("Welcome to Food Palace A I ")
  pyttsx3.speak("Please Select which help you need ")

  #os.system("start excel")

  print("""Welcome to Food Palace AI !!
        Select option you need: 
        [1] Listing
        [2] UOM
        [3] Price Change
        [4] Cost Change
        [5] Ministry
        """)
  #pyttsx3.speak(f"{items[1]}")
  #pyttsx3.speak(f"{items[2]}")
  #pyttsx3.speak(f"{items[3]}")
  #pyttsx3.speak(f"{items[4]}")
  #pyttsx3.speak(f"{items[5]}")
  appSelection = int(input("Please enter number: "))

  try:
    match appSelection:
      case 1:
        pyttsx3.speak(f"You choose {items[appSelection]}")
        list.appListing()
        start()
      case 2:
        pyttsx3.speak(f"You choose {items[appSelection]}")
        uom.appUom()
        start()
      case 3:
        pyttsx3.speak(f"You choose {items[appSelection]}")
        price.appPriceChange()
        start()
      case 4:
        pyttsx3.speak(f"You choose {items[appSelection]}")
        cost.appCostChange()
        start()
      case 5:
        pyttsx3.speak(f"You choose {items[appSelection]}")
        min.appMinistry()
        start()
      case _:
        print("Selected number is not in the list")
        pyttsx3.speak("Selected number is not in the list")
        appSelection = input("Please enter number: ")

  except ValueError:
    appSelection = input("Please enter number: ")
    pyttsx3.speak("Please enter number: ")

start()