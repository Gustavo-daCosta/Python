from tkinter import *
from tkinter import messagebox

# Frame serve para organizar os widgets e o conteúdo das interfaces gráficas

def mostrarMsg():
    messagebox.showinfo(title='Tkinter', message='Hello World!')

app = Tk()
app.title('Tkinter')
app.geometry('500x300')

vnum_cstexto = StringVar()

# relief = SOLID, FLAT, RAISED, SUNKEN, RIDGE, GROOVE
fr_quadro1 = Frame(app, borderwidth=1, relief=SOLID)
fr_quadro1.place(x=10, y=10, width=300, height=100)

lb_tipo = Label(fr_quadro1, text='Tipo de caixa(1/2/3)')
lb_tipo.place(x=10, y=10)
tb_num = Entry(fr_quadro1, textvariable=vnum_cstexto)
vnum_cstexto.set('1')
tb_num.place(x=10, y=30)

btn_msg = Button(fr_quadro1, text='Mostrar mensagem', command=lambda: mostrarMsg())
btn_msg.place(x=10, y=50)

fr_quadro2 = Frame(app, borderwidth=1, relief=SOLID, background="blue")
fr_quadro2.place(x=10, y=120, width=300, height=100)

app.mainloop()