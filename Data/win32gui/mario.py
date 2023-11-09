import win32gui, win32ui, win32con,win32api
import time

def main():
  list_window_names()
  get_inner_windows()
  windowName = "Flyff Universe - Google Chrome"
  hwnd= win32gui.FindWindow(None, windowName)
  win = win32ui.CreateWindowFromHandle(hwnd)
  get_inner_windows(hwnd)
  
  # Give focus on the window
  win32gui.SetForegroundWindow(hwnd)
  time.sleep(2)
  
  win32api.SendMessage(hwnd, win32con.WM_KEYDOWN,0x20,0)


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
  return hwnds

main()