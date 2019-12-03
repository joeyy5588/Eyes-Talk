import os
import pyautogui
import win32gui
import win32con
import time
os.startfile('notepad')
time.sleep(2)
HWND = win32gui.FindWindow('notepad',None)
win32gui.SetActiveWindow(HWND)
print(HWND)
win32gui.SetWindowPos(HWND, win32con.HWND_TOPMOST, 1000, 0, 800, 600, win32con.SWP_SHOWWINDOW)
pyautogui.click(1700,300)
pyautogui.typewrite('a',0.25)

pyautogui.typewrite('j',0.25)
pyautogui.typewrite('4',0.25)
pyautogui.press('left')
pyautogui.press('down')
pyautogui.press('enter')
