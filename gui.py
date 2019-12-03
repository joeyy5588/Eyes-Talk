from detect_blinks1 import *
from tkinter import *
import time
import math


headers1 = ['ㄅ', 'ㄆ', 'ㄇ', 'ㄈ']
headers2 = ['ㄉ', 'ㄊ', 'ㄋ', 'ㄌ']
headers3 = ['ㄍ', 'ㄎ', 'ㄏ']
headers4 = ['ㄐ', 'ㄑ', 'ㄒ']#must with body
headers5 = ['ㄓ', 'ㄔ', 'ㄕ', 'ㄖ']
headers6 = ['ㄗ', 'ㄘ', 'ㄙ']
headers7 = ['ㄦ']
utility = ['左', '右', '上', '下', '後退']
headers = headers1 + headers2 + headers3 + headers4 + headers5 + headers6 + headers7
body = ['ㄧ', 'ㄨ', 'ㄩ']
tail = ['ㄚ', 'ㄛ', 'ㄜ', 'ㄝ', 'ㄞ', 'ㄟ', 'ㄠ', 'ㄡ', 'ㄢ', 'ㄣ', 'ㄤ', 'ㄥ']
sound = ['-', 'ˊ', 'ˇ', 'ˋ', '˙']

root = Tk()
def actions(c):
	if c == 'ㄅ':
		print(c)
	elif c == 'ㄆ':
		print(c)
	elif c == 'ㄇ':
		print(c)
	elif c == 'ㄈ':
		print(c)
	elif c == 'ㄉ':
		print(c)
	elif c == 'ㄊ':
		print(c)
	elif c == 'ㄋ':
		print(c)
	elif c == 'ㄌ':
		print(c)
	elif c == 'ㄍ':
		print(c)
	elif c == 'ㄎ':
		print(c)
	elif c == 'ㄏ':
		print(c)
	elif c == 'ㄐ':
		print(c)
	elif c == 'ㄑ':
		print(c)
	elif c == 'ㄒ':
		print(c)
	elif c == 'ㄓ':
		print(c)
	elif c == 'ㄔ':
		print(c)
	elif c == 'ㄕ':
		print(c)
	elif c == 'ㄖ':
		print(c)
	elif c == 'ㄗ':
		print(c)
	elif c == 'ㄘ':
		print(c)
	elif c == 'ㄙ':
		print(c)
	elif c == 'ㄧ':
		print(c)
	elif c == 'ㄨ':
		print(c)
	elif c == 'ㄩ':
		print(c)
	elif c == 'ㄚ':
		print(c)
	elif c == 'ㄛ':
		print(c)
	elif c == 'ㄜ':
		print(c)
	elif c == 'ㄝ':
		print(c)
	elif c == 'ㄞ':
		print(c)
	elif c == 'ㄟ':
		print(c)
	elif c == 'ㄠ':
		print(c)
	elif c == 'ㄡ':
		print(c)
	elif c == 'ㄢ':
		print(c)
	elif c == 'ㄣ':
		print(c)
	elif c == 'ㄤ':
		print(c)
	elif c == 'ㄥ':
		print(c)
	elif c == 'ㄦ':
		print(c)
	elif c == '-':
		print(c)
	elif c == 'ˊ':
		print(c)
	elif c == 'ˇ':
		print(c)
	elif c == 'ˋ':
		print(c)
	elif c == '上':
		print(c)
	elif c == '下':
		print(c)
	elif c == '左':
		print(c)
	elif c == '右':
		print(c)
	elif c == '後退':
		print(c)
def show_row(row = -1, col = -1, type = 0):#type: 0->headers 1->body 2->tail 3->sound
	if type == 0:
		alpha_array = utility + headers + body
		while(len(alpha_array) < 30):
			alpha_array += ' '
	elif type == 1:
		alpha_array = utility + body + tail
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
		alpha_array = utility + body + tail
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
		alpha_array = utility + body + tail
		while(len(alpha_array) < 30):
			alpha_array += ' '
		actions(alpha_array[5*row+col])
		if row == 0:
			if col == 4:
				type = 0
			else:
				type = 1
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
		if m == 1:
			state = 1
			#row, col, type = pressrow(row, col, type)
		else:
			if type == 0:
				row = (row+1)%6
			elif type == 1:
				row = (row+1)%4
			elif type == 2:
				row = (row+1)%5
			elif type == 3:
				row = (row+1)%2
		show_row(row, col, type)		
	elif state == 1:
		if m == 1:
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
	root.geometry('800x600')
	
				

#Main
'''
if __name__ == "__main__": 
	initialize()
	root.after(0, show)
	#col = root.after(0, head_col, row)
	root.mainloop()
'''