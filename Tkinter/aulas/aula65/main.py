from tkinter import *
from tkinter import messagebox

def mostrarMsg(tipomsg, mensagem):
    if tipomsg == '1':
        messagebox.showinfo(title='Informação', message=mensagem)
    elif tipomsg == '2':
        messagebox.showwarning(title='Aviso', message=mensagem)
    elif tipomsg == '3':
        messagebox.showerror(title='Erro', message=mensagem)

def resetarTB():
    res = messagebox.askyesno(title='Resetar', message='Confirmar reset do TextBox?')
    # askyesno // askquestion // askyesnocancel - YES e NO (True e False)
    # askokcancel - OK e CANCEL (True e False)
    # askretrycancel - REPETIR e CANCELAR (True e False)
    # askyesnocancel - YES, NO e CANCEL (True, False e None)
    if res is True:
        tb_num.delete(0, END)
        tb_num.insert(0, '1')


vmsg = 'Curso de Tkinter'

app = Tk()
app.title('Tkinter')
app.geometry('500x300')

vnum_cstexto = StringVar()

Label(app, text='Tipo de caixa(1/2/3)').pack()
tb_num = Entry(app, textvariable=vnum_cstexto)
vnum_cstexto.set('1')
tb_num.pack()

btn_msg = Button(app, text='Mostrar mensagem', command=lambda: mostrarMsg(vnum_cstexto.get(), vmsg))
btn_msg.pack()

btn_reset = Button(app, text='Resetar TextBox', command=resetarTB)
btn_reset.pack()

app.mainloop()