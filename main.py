from tkinter import *
import numpy as np
import math
from decimal import *

activeStr = ' '
stack = []
label = 

# Функции
def mid(event):
	root = Tk()
	root.iconbitmap('icon.ico')

	# Параметры окна
	root.title("Вычисление среднего арифметического значения")

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


def fact(event):
	root = Tk()
	root.iconbitmap('icon.ico')

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


def gip(event):
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

	
def calc(event):
	root = Tk()
	root.iconbitmap('icon.ico')
	root.title('Калькулятор')
	root.resizable(0, 0)

	buttons = (('7', '8', '9', '/', '4'),
	           ('4', '5', '6', '*', '4'),
	           ('1', '2', '3', '-', '4'),
	           ('0', '.', '=', '+', '4')
	           )



	def calculate():
	    global stack
	    global label
	    result = 0
	    operand2 = Decimal(stack.pop())
	    operation = stack.pop()
	    operand1 = Decimal(stack.pop())

	    if operation == '+':
	        result = operand1 + operand2
	    if operation == '-':
	        result = operand1 - operand2
	    if operation == '/':
	        result = operand1 / operand2
	    if operation == '*':
	        result = operand1 * operand2
	    label.configure(text=str(result))

	def click(text):
	    global activeStr
	    global stack
	    if text == 'CE':
	        stack.clear()
	        activeStr = ''
	        label.configure(text='0')
	    elif '0' <= text <= '9':
	        activeStr += text
	        label.configure(text=activeStr)
	    elif text == '.':
	        if activeStr.find('.') == -1:
	            activeStr += text
	            label.configure(text=activeStr)
	    else:
	        if len(stack) >= 2:
	            stack.append(label['text'])
	            calculate()
	            stack.clear()
	            stack.append(label['text'])
	            activeStr = ''
	            if text != '=':
	                stack.append(text)
	        else:
	            if text != '=':
	                stack.append(label['text'])
	                stack.append(text)
	                activeStr = ''
	                label.configure(text='0')

	label = Label(root, text='0', width=35)
	label.grid(row=0, column=0, columnspan=4, sticky="nsew")

	button = Button(root, text='CE', command=lambda text='CE': click(text))
	button.grid(row=1, column=3, sticky="nsew")
	for row in range(4):
	    for col in range(4):
	        button = Button(root, text=buttons[row][col],
	                command=lambda row=row, col=col: click(buttons[row][col]))
	        button.grid(row=row + 2, column=col, sticky="nsew")

	root.grid_rowconfigure(6, weight=1)
	root.grid_columnconfigure(4, weight=1)

	root.mainloop()


def sqr(event):
	root = Tk()
	root.iconbitmap('icon.ico')
	root.resizable(0, 0)

	# Параметры окна
	root.title("Вычисление корня квадратного уравнения")

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


def dk(event):
	def gcd():
	    n1,n2 = correct()
	    prime1 = prime(n1)
	    prime2 = prime(n2)
	    gcd,lcm = gcd_lcm(n1,n2)
	    lab_prime_n1["text"] = prime1
	    lab_prime_n2["text"] = prime2
	    lab_gcd["text"] = gcd
	    lab_lcm["text"] = lcm
	 
	def correct():
	    a = ent_n1.get()
	    b = ent_n2.get()
	    try:
	        a = int(a)
	    except ValueError:
	        a = 0
	        ent_n1.delete(0,END)
	        ent_n1.insert(0,0)
	    try:
	        b = int(b)
	    except ValueError:
	        b = 0
	        ent_n2.delete(0,END)
	        ent_n2.insert(0,0)
	    return abs(a), abs(b)
	 
	def prime(n):
	    a = []
	    while n > 1:
	        i = 2
	        while 1:
	            if n%i==0:
	                a.append(i)
	                n //= i
	                break
	            else:
	                i += 1
	    return a
	 
	def gcd_lcm(a,b):
	    m = a*b
	    while a!=0 and b!=0:
	        if a > b: a %= b
	        else: b %= a
	    g = a + b
	    l = m // g
	    return g, l
	 
	root1 = Tk()
	root1.iconbitmap('icon.ico')
	root1.title('НОД, НОК и разложение на простые числа')
	lab_n1 = Label(root1, text="Число 1")
	lab_n1.grid(row=2,column=0)
	 
	lab_n2 = Label(root1, text="Число 2")
	lab_n2.grid(row=3,column=0)
	 
	ent_n1 = Entry(root1, width=10,bg="white")
	ent_n1.grid(row=2,column=1)
	 
	ent_n2 = Entry(root1, width=10,bg="white")
	ent_n2.grid(row=3,column=1)
	 
	lab_prime = Label(root1, text="Простые сомножители:")
	lab_prime.grid(row=1,column=3,columnspan=2)
	 
	lab_prime_n1 = Label(root1, bg="white")
	lab_prime_n1.grid(row=2,column=3,columnspan=2)
	 
	lab_prime_n2 = Label(root1, bg="white")
	lab_prime_n2.grid(row=3,column=3,columnspan=2)
	 
	lab_gcd_ = Label(root1, text="НОД",bg="lightgreen",width=7)
	lab_gcd_.grid(row=4,column=3)
	lab_gcd = Label(root1, bg="lightgreen",width=10)
	lab_gcd.grid(row=4,column=4)
	 
	lab_lcm_ = Label(root1, text="НОК",bg="lightblue",width=7)
	lab_lcm_.grid(row=5,column=3)
	lab_lcm = Label(root1, bg="lightblue",width=10)
	lab_lcm.grid(row=5,column=4)
	 
	but = Button(root1, text="Вычислить",command=gcd,pady=10)
	but.grid(row=4,column=0,rowspan=2,columnspan=2,sticky=W+N+S+E)
	 
	root1.mainloop()


# Параметры экрана
root = Tk()
root.title("Главное меню")
root.iconbitmap('icon.ico')
root.resizable(0, 0)

# Код
btn1 = Button(root, text='Ср. арифмитическое')
btn2 = Button(root, text='Корень линейного уравнения')
btn3 = Button(root, text='Гипотенуза')
btn4 = Button(root, text='Калькулятор')
btn5 = Button(root, text='Факториал')
btn6 = Button(root, text='НОД, НОК и разложение простые числа')

btn1.bind("<Button-1>", mid)
btn2.bind("<Button-1>", sqr)
btn3.bind("<Button-1>", gip)
btn4.bind("<Button-1>", calc)
btn5.bind("<Button-1>", fact)
btn6.bind("<Button-1>", dk)

btn1.grid(row= 0, column=0)
btn2.grid(row=0, column=1)
btn3.grid(row=1, column=0)
btn4.grid(row=1, column=1)
btn5.grid(row=2, column=0)
btn6.grid(row=2, column=1)

root.mainloop()