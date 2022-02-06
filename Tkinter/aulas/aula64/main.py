from tkinter import *

def imprimirEsporte():
    ve = vesporte.get()
    if ve == "Futebol":
        print("O esporte escolhido é o Futebol")
    elif ve == "Basquete":
        print("O esporte escolhido é o Basquete")
    elif ve == "Vôlei":
        print("O esporte escolhido é o Vôlei")
    else:
        print('Selecione um esporte')

listaEsportes = ['Futebol', 'Basquete', 'Vôlei']

app = Tk()
app.title('Tkinter')
app.geometry('500x300')

vesporte = StringVar()
vesporte.set("Selecione um esporte")

bl_esportes = Label(app, text='Esportes')
bl_esportes.pack()

op_esportes = OptionMenu(app, vesporte, *listaEsportes)
op_esportes.pack()

btn_esporte = Button(app, text='Esporte selecionado', command=imprimirEsporte)
btn_esporte.pack()


app.mainloop()