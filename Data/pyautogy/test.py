import pyautogui
import time

time.sleep(3)

# screen resolution
#print(pyautogui.size())

# mouse position
# print(pyautogui.position())

# move mouse position overtime
# pyautogui.moveTo(100,100,3)

# move relatively
# pyautogui.moveRel(100,100,3)

# click (coor1,coor2, #clks, #dur, button)
# pyautogui.click(500,500,3,3,button="right")

# press tab
# pyautogui.press('tab', presses = 3)

# scroll up/down
# pyautogui.scroll(500)
# pyautogui.scroll(-500)

# mouse up and down
# pyautogui.mouseUp(100, 100, button="left")
# pyautogui.mouseDown(100, 100, button="left")

# example
pyautogui.mouseDown(300, 400, button="left")
pyautogui.moveTo(800, 400, 3)
pyautogui.mouseUp()
pyautogui.moveTo(1000, 400, 3)
