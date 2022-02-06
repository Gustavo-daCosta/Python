from tkinter import *

def imprimirEsporte():
    ve = vesporte.get()
    if ve == "futebol":
        print("O esporte escolhido é o Futebol")
    elif ve == "basquete":
        print("O esporte escolhido é o Basquete")
    elif ve == "volei":
        print("O esporte escolhido é o Vôlei")
    else:
        print('Selecione um esporte')

app = Tk()
app.title('Tkinter')
app.geometry('500x300')

vesporte = StringVar()
vcor = StringVar()

bl_esportes = Label(app, text='Esportes')
bl_esportes.pack()

rb_futebol = Radiobutton(app, text='Futebol', value='futebol', variable=vesporte)
rb_futebol.pack()

rb_volei = Radiobutton(app, text='Vôlei', value='volei', variable=vesporte)
rb_volei.pack()

rb_basquete = Radiobutton(app, text='Basquete', value='basquete', variable=vesporte)
rb_basquete.pack()

rb_verde = Radiobutton(app, text='Verde', value='#0f0', variable=vcor)
rb_verde.pack()

rb_vermelho = Radiobutton(app, text='Vermelho', value='#f00', variable=vcor)
rb_vermelho.pack()

btn_esporte = Button(app, text='Esporte selecionado', command=imprimirEsporte)
btn_esporte.pack()


app.mainloop()