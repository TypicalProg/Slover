from tkinter import *
import math
import numpy as np

root = Tk()

# Параметры окна
root.title("Вычисление корней квадратного уравнения")
root.resizable(0, 0)

# Содержимое окна
def mid(event):
	num = ent1.get()
	x1  = 0
	x2 = 0

	a = ent1.get()
	b = ent2.get()
	c = ent3.get()

	a = float(a)
	b = float(b)
	c = float(c)

	d = b ** 2 - 4 * a * c

	if d > 0:
		x1 = (-b + math.sqrt(d)) / (2 * a)
		x2 = (-b - math.sqrt(d)) / (2 * a)

		x1 = round(x1, 3)
		x2 = round(x2, 3)

		lbl1['text'] = 'x1 = ' + str(x1)
		lbl2['text'] = 'x2 = ' + str(x2)

	elif(d == 0):
		x1 = -b / (2 * a)
		x1 = round(x1, 3)

		lbl1['text'] = 'x = ' + str(x1)
		lbl2['text'] = ''

	else:
		lbl1['text'] = 'Корней нет'
		lbl2['text'] = ''
