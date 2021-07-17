from tkinter import *
from tkinter import messagebox
import os
from sqlite3 import Error
import banco


app = Tk()
app.title("Login")
app.geometry("200x150")


vsql = ""
cont = 0
def novo():
    global cont
    if btn_novo["bg"] == "black":
        if form_user.get() == "" or form_senha.get() == "":
            messagebox.showinfo(title="Erro", message = "Digite todos os dados")
            form_user.delete(0, END)
            form_senha.delete(0, END)
            return
        try:
            vuser = form_user.get()
            vsenha = form_senha.get()
            vquery = "INSERT INTO usuario_senha(USER, SENHA) " \
                     "VALUES ('"+vuser+"', '"+vsenha+"')"
            banco.dml(vquery)
            form_user.delete(0, END)
            form_senha.delete(0, END)
        except Error as ex:
            print("Erro")

    btn_novo["text"] = "Criar"
    btn_novo["bg"] = "black"
    btn_novo["fg"] = "white"
    cont +=1


def autenticar():
    pass

frame1 = Frame(app)
frame1.place(x=40, y=10)

frame2 = Frame(app)
frame2.place(x=40, y=100, width=125)

"""LABEL USER"""
lb_user = Label(frame1, text = "User")
lb_user.pack()
"""ENTRY USER"""
form_user = Entry(frame1)
form_user.pack()

"""LABEL SENHA"""
lb_senha = Label(frame1, text = "Password")
lb_senha.pack()


"""ENTRY SENHA"""
form_senha = Entry(frame1)
form_senha.pack()

"""BOTÃO LOGIN"""
btn_login = Button(frame2, text = "login", command=autenticar)
btn_login.pack(side=LEFT)
"""BOTÃO NOVO"""
btn_novo = Button(frame2, text = "Novo", command=novo)
btn_novo.pack(side=RIGHT)

app.mainloop()