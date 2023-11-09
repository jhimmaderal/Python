import pyautogui as py
import time

heal = 'y'

def startHeal():
    second = 0 
    while heal == 'y':
            
        for i in range(300): #5mins
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
                py.hotkey('5',presses = 3, intervaasl= .5)
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
        
          

startHeal()