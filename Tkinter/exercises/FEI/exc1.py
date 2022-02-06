from tkinter import *

app = Tk()
app.title("Exercício 1")
app.geometry("300x300")

# ↑
txtNorte = Label(app, text="Label Norte")
txtNorte.place(x=120, y=10)

# →
txtLeste = Label(app, text="Label Leste")
txtLeste.place(x=235, y=130)

# ←
txtOeste = Label(app, text="Label Oeste")
txtOeste.place(x=0, y=130)

# ↓
txtSul = Label(app, text="Label Sul")
txtSul.place(x=130, y=275)

app.mainloop()