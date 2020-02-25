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

		lbl1['text'] = x1
		lbl2['text'] = x2

	elif(d == 0):
		x1 = -b / (2 * a)
		x1 = round(x1, 3)

		lbl1['text'] = x1
		lbl2['text'] = ''
		
	else:
		lbl1['text'] = 'Корней нет'
		lbl2['text'] = ''
		


btn1 = Button(root, text='Вычислить', width=15, font=30)

lbl3 = Label(root, width=20, font=30, text='Введите коэффициенты\nквадратного уравнения:')
lbl1 = Label(root, width=15, font=30)
lbl2 = Label(root, width=15, font=30)
txt_b = Label(root, text='b = ', font=30)
txt_c = Label(root, text='c = ', font=30)
txt_a = Label(root, text='a = ', font=30)

ent1 = Entry(root, font=30)
ent2 = Entry(root, font=30)
ent3 = Entry(root, font=30)


lbl3.grid(row=0, column=0)
txt_a.grid(row=1, column=0)
ent1.grid(row=2, column=0)
txt_b.grid(row=3, column=0)
ent2.grid(row=4, column=0)
txt_c.grid(row=5, column=0)
ent3.grid(row=6, column=0)
lbl1.grid(row=7, column=0)
lbl2.grid(row=8, column=0)
btn1.grid(row=9, column=0)

btn1.bind("<Button-1>", mid)

root.mainloop()