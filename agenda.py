from tkinter import *
from tkinter import ttk
import os
import banco

app = Tk()
app.title("Projeto Agenda")
app.geometry("500x330")

def inserir():
    pass

def deletar():
    pass

def obter():
    pass

frame1 = Frame(app, pady=10)
frame1.pack()

lbid=Label(frame1, text="ID")
vid = Entry(frame1)

lbnome=Label(frame1, text="NOME")
vnome = Entry(frame1)

lfone=Label(frame1, text="FONE")
vfone = Entry(frame1)

#listaNomes = [['0', 'Brertilda', 9878], ['1', 'Crisloide', 5554], ['2', 'Julsevan', 5841]]

tv = ttk.Treeview(frame1, columns = ('id', 'nome', 'fone'), show= 'headings')
tv.column('id', minwidth=0, width=80)
tv.column('nome', minwidth=0, width=250)
tv.column('fone', minwidth=0, width=120)
tv.heading('id', text='ID')
tv.heading('nome', text='NOME')
tv.heading('fone', text='TELEFONE')

btn_inserir = Button(frame1, text="Inserir", command=inserir)
btn_deletar = Button(frame1, text="Deletar", command=deletar)
btn_obter = Button(frame1, text="Obter", command=obter)

lbid.grid(column=0, row=0)
vid.grid(column=0, row=1)

lbnome.grid(column=1, row=0)
vnome.grid(column=1, row=1)

lfone.grid(column=2, row=0)
vfone.grid(column=2, row=1)

tv.grid(column=0, row=3, columnspan=3, pady=5)

btn_inserir.grid(column=0, row=4)
btn_deletar.grid(column=1, row=4)
btn_obter.grid(column=2, row=4)

#tv.insert("", "end", values=(i, n, f))

app.mainloop()