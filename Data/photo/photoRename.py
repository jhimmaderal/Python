from openpyxl import load_workbook as lw
import os
import re

codes = {}
photos = []
def openFile():

  file = "list.xlsx"
  xlsfile = lw(file)
  shtFile = xlsfile.active #change Sheet ["sheetName"]
  rowFile = shtFile.max_row  # count total row
  colFile = shtFile.max_column  # count total column
    
  for item in range(2,rowFile):
    fpCode = shtFile.cell(row=item , column = 1)
    fpVal = fpCode.value
    barCode = shtFile.cell(row=item , column = 2)
    barVal = barCode.value
    itemVal = {str(fpVal) + ".jpg" : str(barVal)}
    codes.update(itemVal)
  
def filephotos():
  oldName = []
  source = "AllPhotos"
  for photo in os.listdir(source):
    if os.path.isfile(os.path.join(source,photo)):
      oldName.append(photo)
      #print(photo)
  
  for name in oldName:
    if codes.get(str(name)) is not None:
      barcode = codes[name]
      os.rename(
        os.path.join(source,name),
        os.path.join(source, barcode + ".png")
      )
    else:
      print("not") 
  
openFile()
filephotos()
