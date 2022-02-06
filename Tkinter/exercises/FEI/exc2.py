from tkinter import *

app = Tk()
app.title("Exercício 2")
app.geometry("300x150")

Label(app, text="1° Valor", anchor=W).place(x=105, y=10, width=100, height=20)
valor1 = Entry(app)
valor1.place(x=105, y=30, width=100, height=20)

Label(app, text="2° Valor", anchor=W).place(x=105, y=60, width=100, height=20)
valor2 = Entry(app)
valor2.place(x=105, y=80, width=100, height=20)

def soma():
    resultSoma = int(valor1.get()) + int(valor2.get())
    print(f"Soma: {resultSoma}")

Button(app, text="Somar", command=soma).place(x=105, y=105, width=100, height=20)

app.mainloop()