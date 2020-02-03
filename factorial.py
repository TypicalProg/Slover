from tkinter import *
import math

root = Tk()
root.iconbitmap('icon.ico')
root.resizable(0, 0)

# Параметры окна
root.title("Вычисление факториала")

# Содержимое окна
def mid(event):
	num = ent1.get()

	f = math.factorial(int(num))

	lbl1['text'] = f


lbl1 = Label(root, width=30, font=30)
btn1 = Button(root, text='Вычислить', width=30, font=30)
ent1 = Entry(root, width=30, font=30)

ent1.grid(row=0, column=0)
lbl1.grid(row=1, column=0)
btn1.grid(row=2, column=0)

btn1.bind("<Button-1>", mid)

root.mainloop()