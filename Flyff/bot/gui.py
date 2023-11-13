from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
import win32gui, win32ui, win32con
import time
import os
import sys

class mainWindow(QMainWindow): # windows
  def __init__(self, *args, **kwargs):
    super(mainWindow,self).__init__(*args,**kwargs)
    self.setWindowTitle("Flyff")
    
    self.browser = QWebEngineView()
    self.browser.setUrl(QUrl("https://universe.flyff.com/play?server=5"))
    self.setCentralWidget(self.browser)
    
def list_window_names():
  def winEnumHandler(hwnd, ctx):
    if win32gui.IsWindowVisible(hwnd):
      print(hex(hwnd), win32gui.GetWindowText(hwnd))
  win32gui.EnumWindows(winEnumHandler, None)

def get_inner_windows(whndl):
  def callback(hwnd, hwnds):
    if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
      hwnds[win32gui.GetClassName(hwnd)] = hwnd
    return True
  hwnds = {}
  win32gui.EnumChildWindows(whndl,callback,hwnds)
  print (hwnds)
  return (hwnds)

def main():

    windowName = "Opening links in a new window with QWebEngineView - Google Chrome"
    hwnd= win32gui.FindWindow(None, windowName)
    hwnd = get_inner_windows(hwnd)["Chrome_RenderWidgetHostHWND"]
    win = win32ui.CreateWindowFromHandle(hwnd)
    list_window_names()
    
    print("Test")
    
    for x in range(15):
      time.sleep(1)
      print(x)
    
    win.SendMessage(win32con.WM_CHAR,ord('b'),0)
    
app = QApplication(sys.argv)
window = mainWindow()
window.show()

app.exec_()

      
