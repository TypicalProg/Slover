from tkinter import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

root = Tk()
root.title("Обратная связь")
root.resizable(0, 0)

def send(event):
	def send_mail():
	    # Логин
	    login = " "
	    # Пароль
	    password = " "
	    # Сервер
	    url = "smtp.yandex.ru"
	    # Кому
	    toaddr = " "

	    msg = MIMEMultipart()
	    # Тема
	    theme = tema_ent.get()
	    msg['Subject'] = theme
	    # От кого
	    msg['From'] = login
	    # Текст письма
	    leter = txt_ent.get(1.0, END)
	    body = leter
	    msg.attach(MIMEText(body, 'plain'))

	    try:
	        server = smtplib.SMTP_SSL(url, 465)
	    except TimeoutError:
	        print('No connect')
	    server.login(login, password)
	    server.sendmail(login, toaddr, msg.as_string())

	    messagebox.showinfo("Успешно!", "Письмо отправлено! \nСпасибо за отзывчивость!")


	def main():
	    send_mail()

	if __name__ == "__main__":
	    main()


lbl1 = Label(root, text='Обратная связь', font='12')
tema = Label(root, text='Тема', font='11')
tema_ent = Entry(root, font='11')
text = Label(root, text='Текст сообщения', font='11')
txt_ent = Text(root, width=15, height=5, font=12)
send_btn = Button(root, text='Отправить', font='10')

lbl1.grid(row=0, columnspan=2)
tema.grid(row=1, columnspan=2)
tema_ent.grid(row=2, columnspan=2)
text.grid(row=3, columnspan=2)
txt_ent.grid(row=4, columnspan=2)
send_btn.grid(row=5, columnspan=2)

send_btn.bind("<Button-1>", send)

root.mainloop()