from detect_blinks1 import *
from gui import *
import os
import pyautogui
import win32gui
import win32con
if __name__ == '__main__':
	EYE_AR_THRESH = 0.22
	FRAME_THRES = 0.5
	vs = cv2.VideoCapture(0)
	fileStream = True
	detect = detector(EYE_AR_THRESH,FRAME_THRES)
	os.startfile('notepad')
	HWND = win32gui.FindWindow('notepad',None)
	win32gui.SetActiveWindow(HWND)
	print(HWND)
	win32gui.SetWindowPos(HWND, win32con.HWND_TOPMOST, 1000, 0, 800, 600, win32con.SWP_SHOWWINDOW)
	pyautogui.click(1700,300)
	initialize()
	root.after(0, show, vs, detect)
	root.mainloop()
#	pt.plot(detect.status)
	cv2.destroyAllWindows()
	vs.release()