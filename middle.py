from tkinter import *
import numpy as np

root = Tk()

# Параметры окна
root.iconbitmap('icon.ico')
root.title("Вычисление среднего арифметического значения")
root.resizable(0, 0)

# Содержимое окна
def mid(event):
	num = ent1.get()
	num_arr = num.split()
	num_arrInt = []
	num_len = len(num_arr)

	for i in range(num_len):
		t = int(num_arr[i])
		num_arrInt.append(t)

	arr_sum = np.sum(num_arrInt)
	middle = arr_sum / num_len
	middle = round(middle, 2)

	lbl1['text'] = middle


lbl1 = Label(root, width=30, font=30)
btn1 = Button(root, text='Вычислить', width=30, font=30)
ent1 = Entry(root, width=30, font=30)

ent1.grid(row=0, column=0)
lbl1.grid(row=1, column=0)
btn1.grid(row=2, column=0)

btn1.bind("<Button-1>", mid)

root.mainloop()