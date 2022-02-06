from tkinter import *
from tkinter import messagebox

def mostrarMsg(tipomsg, mensagem):
    for c in range(0, 3):
        if tipomsg == lista[c]:
            messagebox.showinfo(title=lista[c], message=mensagem)

vmsg = 'Curso de Tkinter'
lista = ['Informação', 'Aviso', 'Erro']

app = Tk()
app.title('Tkinter')
app.geometry('500x300')

vnum_cstexto = StringVar()
caixa = 'Selecione uma opção'

bl_caixa = Label(app, text='Message Box')

op_caixa = OptionMenu(app, caixa, *lista)
op_caixa.pack()

btn_msg = Button(app, text='Mostrar mensagem', command=lambda: mostrarMsg(vnum_cstexto.get(), vmsg))
btn_msg.pack()


app.mainloop()