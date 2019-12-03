from detect_blinks1 import *
from tkinter import *
import time
import math
import pyautogui


headers1 = ['ㄅ', 'ㄆ', 'ㄇ', 'ㄈ']
headers2 = ['ㄉ', 'ㄊ', 'ㄋ', 'ㄌ']
headers3 = ['ㄍ', 'ㄎ', 'ㄏ']
headers4 = ['ㄐ', 'ㄑ', 'ㄒ']#must with body
headers5 = ['ㄓ', 'ㄔ', 'ㄕ', 'ㄖ']
headers6 = ['ㄗ', 'ㄘ', 'ㄙ']
headers7 = ['確認']
utility = ['左', '右', '上', '下', '後退']
headers = headers7 + headers1 + headers2 + headers3 + headers4 + headers5 + headers6
body = ['ㄧ', 'ㄨ', 'ㄩ']
tail = ['ㄚ', 'ㄛ', 'ㄜ', 'ㄝ', 'ㄞ', 'ㄟ', 'ㄠ', 'ㄡ', 'ㄢ', 'ㄣ', 'ㄤ', 'ㄥ']
sound = ['-', 'ˊ', 'ˇ', 'ˋ', '˙']

root = Tk()
def actions(c):
	if c == 'ㄅ':
		pyautogui.typewrite('1',0.25)
	elif c == 'ㄆ':
		pyautogui.typewrite('q',0.25)
	elif c == 'ㄇ':
		pyautogui.typewrite('a',0.25)
	elif c == 'ㄈ':
		pyautogui.typewrite('z',0.25)
	elif c == 'ㄉ':
		pyautogui.typewrite('2',0.25)
	elif c == 'ㄊ':
		pyautogui.typewrite('w',0.25)
	elif c == 'ㄋ':
		pyautogui.typewrite('s',0.25)
	elif c == 'ㄌ':
		pyautogui.typewrite('x',0.25)
	elif c == 'ㄍ':
		pyautogui.typewrite('e',0.25)
	elif c == 'ㄎ':
		pyautogui.typewrite('d',0.25)
	elif c == 'ㄏ':
		pyautogui.typewrite('c',0.25)
	elif c == 'ㄐ':
		pyautogui.typewrite('r',0.25)
	elif c == 'ㄑ':
		pyautogui.typewrite('f',0.25)
	elif c == 'ㄒ':
		pyautogui.typewrite('v',0.25)
	elif c == 'ㄓ':
		pyautogui.typewrite('5',0.25)
	elif c == 'ㄔ':
		pyautogui.typewrite('t',0.25)
	elif c == 'ㄕ':
		pyautogui.typewrite('g',0.25)
	elif c == 'ㄖ':
		pyautogui.typewrite('b',0.25)
	elif c == 'ㄗ':
		pyautogui.typewrite('y',0.25)
	elif c == 'ㄘ':
		pyautogui.typewrite('h',0.25)
	elif c == 'ㄙ':
		pyautogui.typewrite('n',0.25)
	elif c == 'ㄧ':
		pyautogui.typewrite('u',0.25)
	elif c == 'ㄨ':
		pyautogui.typewrite('j',0.25)
	elif c == 'ㄩ':
		pyautogui.typewrite('m',0.25)
	elif c == 'ㄚ':
		pyautogui.typewrite('8',0.25)
	elif c == 'ㄛ':
		pyautogui.typewrite('i',0.25)
	elif c == 'ㄜ':
		pyautogui.typewrite('k',0.25)
	elif c == 'ㄝ':
		pyautogui.typewrite(',',0.25)
	elif c == 'ㄞ':
		pyautogui.typewrite('9',0.25)
	elif c == 'ㄟ':
		pyautogui.typewrite('o',0.25)
	elif c == 'ㄠ':
		pyautogui.typewrite('l',0.25)
	elif c == 'ㄡ':
		pyautogui.typewrite('.',0.25)
	elif c == 'ㄢ':
		pyautogui.typewrite('0',0.25)
	elif c == 'ㄣ':
		pyautogui.typewrite('p',0.25)
	elif c == 'ㄤ':
		pyautogui.typewrite(';',0.25)
	elif c == 'ㄥ':
		pyautogui.typewrite('/',0.25)
	elif c == '確認':
		pyautogui.press('enter')
	elif c == '-':
		pyautogui.press('space')
	elif c == 'ˊ':
		pyautogui.typewrite('6',0.25)
	elif c == 'ˇ':
		pyautogui.typewrite('3',0.25)
	elif c == 'ˋ':
		pyautogui.typewrite('4',0.25)
	elif c == '上':
		pyautogui.press('up')
	elif c == '下':
		pyautogui.press('down')
	elif c == '左':
		pyautogui.press('left')
	elif c == '右':
		pyautogui.press('right')
	elif c == '後退':
		pyautogui.press('backspace')
def show_row(row = -1, col = -1, type = 0):#type: 0->headers 1->body 2->tail 3->sound
	if type == 0:
		alpha_array = utility + headers + body
		while(len(alpha_array) < 30):
			alpha_array += ' '
	elif type == 1:
		alpha_array = utility + body + tail + sound
		while(len(alpha_array) < 30):
			alpha_array += ' '
	elif type == 2:
		alpha_array = utility + tail + sound
		while(len(alpha_array) < 30):
			alpha_array += ' '
	elif type == 3:
		alpha_array = utility + sound
		while(len(alpha_array) < 30):
			alpha_array += ' '
	for x in range(6):
		for y in range(5):
			if row == -1 and col == -1:
				l = Label(root, text = alpha_array[5*x+y], font = 'labelfont 24')
			elif col == -1:
				if x == row:
					l = Label(root, text = alpha_array[5*x+y], font = 'labelfont 24', bg = "black", fg = "white")
				else:
					l = Label(root, text = alpha_array[5*x+y], font = 'labelfont 24')
			elif row == -1:
				if y == col:
					l = Label(root, text = alpha_array[5*x+y], font = 'labelfont 24', bg = "black", fg = "white")
				else:
					l = Label(root, text = alpha_array[5*x+y], font = 'labelfont 24')
			l.grid(column=y, row=x, sticky=N+S+E+W)
	for i in range(5):
		root.grid_rowconfigure(i, weight=1)
		root.grid_columnconfigure(i, weight=1)
	root.grid_rowconfigure(5, weight=1)

def show_col(row = -1, col = -1, type = 0):
	if type == 0:
		alpha_array = utility + headers + body
		while(len(alpha_array) < 30):
			alpha_array += ' '
	elif type == 1:
		alpha_array = utility + body + tail + sound
		while(len(alpha_array) < 30):
			alpha_array += ' '
	elif type == 2:
		alpha_array = utility + tail + sound
		while(len(alpha_array) < 30):
			alpha_array += ' '
	elif type == 3:
		alpha_array = utility + sound
		while(len(alpha_array) < 30):
			alpha_array += ' '
	for x in range(6):
		for y in range(5):
			if x == row:
				if y == col:
					l = Label(root, text = alpha_array[5*x+y], font = 'labelfont 24', bg = "black", fg = "white")
				else:
					l = Label(root, text = alpha_array[5*x+y], font = 'labelfont 24')
			else:
				l = Label(root, text = '')
			l.grid(column=y, row=x, sticky=N+S+E+W)
	for i in range(5):
		root.grid_rowconfigure(i, weight=1)
		root.grid_columnconfigure(i, weight=1)
	root.grid_rowconfigure(5, weight=1)
def pressrow(row, col, type):
	if type == 0:
		if row == 0:
			row = 5
		else:
			row -= 1
	elif type == 1:
		if row == 0:
			row = 4
		else:
			row -= 1
	elif type == 2:
		if row == 0:
			row = 4
		else:
			row -= 1
	elif type == 3:
		if row == 0:
			row = 1
		else:
			row -= 1
	return row, col, type
def presscol(row, col, type):
	if type == 0:
		alpha_array = utility + headers + body
		while(len(alpha_array) < 30):
			alpha_array += ' '
		actions(alpha_array[5*row+col])
		if row == 0:
			if col == 4:
				type = 0
			else:
				type = 0
		else:
			type = 1
	elif type == 1:
		alpha_array = utility + body + tail + sound
		while(len(alpha_array) < 30):
			alpha_array += ' '
		actions(alpha_array[5*row+col])
		if row == 0:
			if col == 4:
				type = 0
			else:
				type = 1
		elif row == 4:
			type = 0
		else:
			type = 2
	elif type == 2:
		alpha_array = utility + tail + sound
		while(len(alpha_array) < 30):
			alpha_array += ' '
		actions(alpha_array[5*row+col])
		if row == 0:
			if col == 4:
				type = 1
			else:
				type = 2
		elif row == 3:
			if col > 1 and col < 5:
				type = 0
			else:
				type = 3
		elif row == 4:
			if col == 0 or col == 1:
				type = 0
			else:
				type = 3
		else:
			type = 3
	elif type == 3:
		alpha_array = utility + sound
		while(len(alpha_array) < 30):
			alpha_array += ' '
		actions(alpha_array[5*row+col])
		if row == 0:
			if col == 4:
				type = 2
			else:
				type = 3
		else:
			type = 0
	row = -1
	col = -1
	return row, col, type

def show(vs, detect, row = -1, col = -1, state = 0, type = 0):#state:0->choose row 1->choose col
	press = False
	(m ,key)= confirm_status(vs,detect)
	if state == 0:
		if (m == 1) and (detect.response[-2] == 0):
			print("get")
			state = 1
			#row, col, type = pressrow(row, col, type)
		else:
			if type == 0:
				row = (row+1)%6
			elif type == 1:
				row = (row+1)%5
			elif type == 2:
				row = (row+1)%5
			elif type == 3:
				row = (row+1)%2
		show_row(row, col, type)		
	elif state == 1 :
		if (m == 1) and (detect.response[-2] == 0):
			state = 0
			press =True
		else:
			col = (col+1)%5
		show_col(row, col, type)
	if press == True:
		row, col, type = presscol(row, col, type)
	root.after(500, show, vs, detect, row, col, state, type)
def initialize():
	"""Constructor method"""
	root.title('EYES TALK') 
	root.geometry('400x300+0+0')
	
				

#Main
'''
if __name__ == "__main__": 
	initialize()
	root.after(0, show)
	#col = root.after(0, head_col, row)
	root.mainloop()
'''