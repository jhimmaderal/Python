import pyautogui as pg
import time 
from openpyxl import load_workbook as lw
  
file = "price change.xlsx"
itemCost = []
xslFile = lw(file)
shtFile = xslFile.active #change Sheet ["sheetName"]
rowFile = shtFile.max_row  # count total row
colFile = shtFile.max_column  # count total column

for item in range(3,rowFile + 1): # loop to A3 to last item
    codeCell = shtFile.cell(row=item, column = 1)
    codeVal = codeCell.value
    itemCost.append(codeVal)
    costCell = shtFile.cell(row=item, column = 3)
    costVal = costCell.value
    itemCost.append(costVal)
    landCell = shtFile.cell(row=item, column = 4)
    landVal = landCell.value
    itemCost.append(landVal)     

def costChange():
  time.sleep(5)
  steps = 0
  
  # Start
  pg.click(58,17, button='left')
  pg.press('f6')
  pg.press('enter')
  for item in itemCost:
    if steps == 0:
      pg.write(str(item))
      pg.press('enter')
      pg.press('f8')
      steps = steps + 1
      
    elif steps == 1:
      pg.press('tab', presses=18)
      pg.write(".")
      pg.press('delete', presses=3)
      pg.press('left', presses= 4)
      pg.write(str(item))
      pg.press('enter')
      steps = steps + 1
      
    elif steps == 2:
      pg.write(".")
      pg.press('delete', presses=3)
      pg.press('left', presses= 4)
      pg.press('left')
      pg.write(str(item))
      steps = 0

def runCostChange():
  print("Price Change - Running.....")
  print(itemCost)
  costChange()

