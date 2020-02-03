from tkinter import *
import math
import numpy as np

root = Tk()
root.iconbitmap('icon.ico')
root.resizable(0, 0)

# Параметры окна
root.title("Вычисление корня квадратного уравнения")

# Содержимое окна
def mid(event):
	num = ent1.get()

	a = ent1.get()
	b = ent2.get()
	c = ent3.get()

	a = float(a)
	b = float(b)
	c = float(c)

	d = b * b - 4 * a * c

	if d > 0:
		x1 = (-b + math.sqrt(d)) / (2 * a)
		x2 = (-b - math.sqrt(d)) / (2 * a)

	lbl1['text'] = x1
	lbl2['text'] = x2


lbl1 = Label(root, width=15, font=30)
lbl2 = Label(root, width=15, font=30)
btn1 = Button(root, text='Вычислить', width=15, font=30)
ent1 = Entry(root, width=15, font=30)
ent2 = Entry(root, width=15, font=30)
ent3 = Entry(root, width=15, font=30)

ent1.grid(row=0, column=0)
ent2.grid(row=1, column=0)
ent3.grid(row=2, column=0)
lbl1.grid(row=3, column=0)
lbl2.grid(row=4, column=0)
btn1.grid(row=5, column=0)

btn1.bind("<Button-1>", mid)

root.mainloop()