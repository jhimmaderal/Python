import pyautogui
import time

print("Running...")

comment = "comment"

time.sleep(5)

for i in range(0,3):
  #pyautogui.typewrite(comment)
  test = "comment " + str(i)
  pyautogui.typewrite(f"{test} \n")
  time.sleep(2)
