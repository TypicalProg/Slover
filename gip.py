from tkinter import *
import math

root = Tk()
root.resizable(0, 0)

# Параметры окна
root.title("Вычисление гипотенузы")

def mid(event):
	num1 = ent1.get()
	num2 = ent2.get()
	num1 = float(num1)
	num2 = float(num2)

	sum1 = num1 ** 2 + num2 ** 2

	fact = math.sqrt(sum1)
	fact = round(fact, 2)

	lbl1['text'] = 'Гипотенуза = ' + str(fact)


lbl1 = Label(root, width=15, font=30)
lbl2 = Label(root, font=30, text='Введите длины катетов:')
btn1 = Button(root, text='Вычислить', width=30, font=30)
lbl3 = Label(root, text='a = ', font=30, width=5)
ent1 = Entry(root, width=15, font=30)
lbl4 = Label(root, font=30, text='b = ', width=5)
ent2 = Entry(root, width=15, font=30)

lbl2.grid(row=0, column=0)
lbl3.grid(row=1, column=0)
ent1.grid(row=2, column=0)
lbl4.grid(row=3, column=0)
ent2.grid(row=4, column=0)
lbl1.grid(row=5, column=0)
btn1.grid(row=6, column=0)

btn1.bind("<Button-1>", mid)

root.mainloop()
