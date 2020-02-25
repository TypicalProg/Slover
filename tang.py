from tkinter import *

root = Tk()
root.resizable(0, 0)

# Параметры окна
root.title("Вычисление тангенса")

def mid(event):
	a = ent1.get()
	b = ent2.get()
	a = float(a)
	b = float(b)

	tang = a / b
	tang = round(tang, 3)

	lbl1['text'] = tang


lbl1 = Label(root, width=15, font=30)
lbl2 = Label(root, font=30, text='Введите длины катетов:')
btn1 = Button(root, text='Вычислить', width=30, font=30)
lbl3 = Label(root, text='Противолежащий', font=30)
ent1 = Entry(root, width=15, font=30)
lbl4 = Label(root, font=30, text='Прилежащий')
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