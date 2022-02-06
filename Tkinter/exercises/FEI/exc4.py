from tkinter import *

app = Tk()
app.title("Exercício 3")
app.geometry("200x200")

Button(app, text="1").place(x=90, y=10, width=25, height=30)
Button(app, text="2").place(x=78, y=40, width=25, height=30)
Button(app, text="3").place(x=100, y=40, width=25, height=30)
Button(app, text="4").place(x=68, y=70, width=25, height=30)
Button(app, text="5").place(x=88, y=70, width=25, height=30)
Button(app, text="6").place(x=110, y=70, width=25, height=30)

app.mainloop()