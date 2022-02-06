from tkinter import *
import os

pastaApp = os.path.dirname(os.path.abspath(__file__))

def semComando():
    print("Sem comando")

def novoContato():
    exec(open(pastaApp + "\\NovoContato.py").read(), {'c':pastaApp})

app = Tk()
app.title("Tkinter")
app.geometry("500x300")
app.configure(background="#dde")

# anchor => N = Norte, S = Sul, E = Leste, W = Oeste
# NE = Nordeste, SE = Sudeste, SO = Sudoeste, NO = Noroeste

barra_menu = Menu(app)

menuContatos = Menu(barra_menu, tearoff=0)
menuContatos.add_command(label = "Novo", command=novoContato)
menuContatos.add_command(label = "Pesquisar", command=semComando)
menuContatos.add_command(label = "Deletar", command=semComando)
menuContatos.add_separator()
menuContatos.add_command(label = "Fechar", command=semComando)
barra_menu.add_cascade(label = "Contatos", menu=menuContatos)

menuManutencao = Menu(barra_menu, tearoff=0)
menuManutencao.add_command(label = "Banco de Dados", command=semComando)
barra_menu.add_cascade(label = "Manutenção", menu=menuManutencao)

menuSobre = Menu(barra_menu, tearoff=0)
menuSobre.add_command(label = "CFB Cursos", command=semComando)
barra_menu.add_cascade(label = "Sobre", menu=menuSobre)




app.config(menu=barra_menu)

app.mainloop()