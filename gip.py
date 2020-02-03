from tkinter import *
import math
import numpy as np

root = Tk()
root.iconbitmap('icon.ico')

# Параметры окна
root.title("Вычисление гипотенузы")

# Содержимое окна
def mid(event):
	num = ent1.get()
	num_arr = num.split()
	num_arrInt = []
	num_len = len(num_arr)

	for i in range(num_len):
		t = int(num_arr[i])
		num_arrInt.append(t**2)

	arr_sum = np.sum(num_arrInt)
	fact = math.sqrt(arr_sum)
	fact = round(fact, 2)

	lbl1['text'] = fact


lbl1 = Label(root, width=30, font=30)
btn1 = Button(root, text='Вычислить', width=30, font=30)
ent1 = Entry(root, width=30, font=30)

ent1.grid(row=0, column=0)
lbl1.grid(row=1, column=0)
btn1.grid(row=2, column=0)

btn1.bind("<Button-1>", mid)

root.mainloop()