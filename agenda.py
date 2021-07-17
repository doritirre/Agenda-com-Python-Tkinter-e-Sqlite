from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from sqlite3 import Error

import os
import banco

app = Tk()
app.title("Projeto Agenda")
app.geometry("500x420")

def popular():
    tv.delete(*tv.get_children())
    vquery = "SELECT * FROM tb_contatos order by ID"
    linhas = banco.dql(vquery)
    for i in linhas:
        tv.insert("", "end", values=i)

def inserir():
    if vnome.get() == "" or vfone.get() == "":
        messagebox.showinfo(title="Error", message="Digite todos os dados")
        return
    try:
        vquery="INSERT INTO tb_contatos (NOME, TELEFONE) VALUES ('"+vnome.get()+"', '"+vfone.get()+"')"
        banco.dml(vquery)
    except Error as ex:
        messagebox.showinfo(title="Erro", message="Erro ao inserir")
    popular()
    vnome.delete(0, END)
    vfone.delete(0, END)
    vnome.focus()

def deletar():
    try:
        itemSelecionado = tv.selection()[0]
        tv.delete(itemSelecionado)
    except Error as ex:
        messagebox.showinfo(title="Erro", message="Selecione uma ou mais opções")

def pesquisar():
    tv.delete(*tv.get_children())
    vquery = "SELECT * FROM tb_contatos WHERE nome LIKE '%"+vnomepesquisar.get()+"%' order by ID"
    linhas = banco.dql(vquery)
    for i in linhas:
        tv.insert("", "end", values=i)


quadroGrid=LabelFrame(app, text="Contatos")
quadroGrid.pack(fill="both", expand="yes", padx=10, pady=10)

tv = ttk.Treeview(quadroGrid, columns = ('id', 'nome', 'fone'), show= 'headings')
tv.column('id', minwidth=0, width=80)
tv.column('nome', minwidth=0, width=250)
tv.column('fone', minwidth=0, width=120)
tv.heading('id', text='ID')
tv.heading('nome', text='NOME')
tv.heading('fone', text='TELEFONE')
tv.pack()
popular()

quadroInserir=LabelFrame(app, text="Inserir novos contatos")
quadroInserir.pack(fill="both", expand="yes", padx=10, pady=10)

lbnome=Label(quadroInserir, text="Nome")
lbnome.pack(side="left")
vnome = Entry(quadroInserir)
vnome.pack(side="left", padx=10)
lbfone=Label(quadroInserir, text="Fone")
lbfone.pack(side="left")
vfone = Entry(quadroInserir)
vfone.pack(side="left", padx=10)
btn_inserir=Button(quadroInserir, text="Inserir", command=inserir)
btn_inserir.pack(side="left", padx=10)

quadroPesquisar=LabelFrame(app, text="Pesquisar Contatos")
quadroPesquisar.pack(fill="both", expand="yes", padx=10, pady=10)

lbid=Label(quadroPesquisar, text="Nome")
lbid.pack(side="left")
vnomepesquisar = Entry(quadroPesquisar)
vnomepesquisar.pack(side="left", padx=10)
btn_pesquisar = Button(quadroPesquisar, text="Pesquisar", command=pesquisar)
btn_pesquisar.pack(side="left", padx=10)
btn_todos = Button(quadroPesquisar, text="Mostrar Todos", command=popular)
btn_todos.pack(side="left", padx=10)


app.mainloop()