from tkinter import *
from tkinter import ttk
import os
import banco

app = Tk()
app.title("Projeto Agenda")
app.geometry("500x300")

frame1 = Frame(app, pady=10)
frame1.pack()

listaNomes = [['0', 'Brertilda', 9878], ['1', 'Crisloide', 5554], ['2', 'Julsevan', 5841]]

tv = ttk.Treeview(frame1, columns = ('id', 'nome', 'fone'), show= 'headings')
tv.column('id', minwidth=0, width=80)
tv.column('nome', minwidth=0, width=250)
tv.column('fone', minwidth=0, width=120)
tv.heading('id', text='ID')
tv.heading('nome', text='NOME')
tv.heading('fone', text='TELEFONE')
tv.pack()

for (i, n, f) in listaNomes:
    tv.insert("", "end", values=(i, n, f))

app.mainloop()