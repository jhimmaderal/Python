import win32gui, win32ui, win32con
import time

def main():
  #list_window_names()

  windowName = "Untitled - Notepad"
  hwnd= win32gui.FindWindow(None, windowName)
  hwnd = get_inner_windows(hwnd)['Edit']
  win = win32ui.CreateWindowFromHandle(hwnd)
  
  win.SendMessage(win32con.WM_CHAR,ord('A'),0)
  win.SendMessage(win32con.WM_KEYDOWN, win32con.VK_RETURN,0)
  win.SendMessage(win32con.WM_KEYUP, win32con.VK_RETURN,0)
  win.SendMessage(win32con.WM_CHAR,ord('d'),0)
  get_inner_windows(hwnd)

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

main()