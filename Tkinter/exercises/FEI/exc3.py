from tkinter import *

app = Tk()
app.title("Exercício 3")
app.geometry("300x100")

def mostrarNome():
    print(f'Olá, {nome.get()}')

Label(app, text="Nome", foreground="#009").place(x=0, y=10, width=55, height=20)
nome = Entry(app)
nome.place(x=10, y=30, width=150, height=20)

Button(app, text='Confirmar', command=mostrarNome, background="#32CD32").place(x=165, y=26, width=70, height=25)

app.mainloop()