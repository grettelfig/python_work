from tkinter import *

aken = Tk()

canvas = Canvas(aken, width=600, height=400)
canvas.pack()

def joonista_sein(canvas, x, y, laius, korgus):
    canvas.create_rectangle(
        x, y,
        x + laius, y + korgus,
        fill="orange"
    )
def joonista_katus(canvas, x, y, laius):
    canvas.create_polygon(
        x, y,
        x + laius / 2, y - 60,
        x + laius, y,
        fill="brown"
    )
def joonista_aken(canvas, x, y, suurus):
    canvas.create_rectangle(
        x, y,
        x + suurus,
        y + suurus,
        fill="lightblue"
    )
def joonista_maja(canvas, x, y, laius, korgus):
    joonista_sein(canvas, x, y, laius, korgus)
    joonista_katus(canvas, x, y, laius)
    joonista_aken(canvas, x + 30, y + 30, 30)


joonista_maja(canvas, 50, 150, 100, 120)
joonista_maja(canvas, 200, 150, 120, 120)
joonista_maja(canvas, 370, 150, 100, 120)


aken.mainloop()