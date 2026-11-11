from tkinter import *
aken = Tk()
canvas = Canvas(aken, width=500, height=400)
canvas.pack()

def joonista_ruut(canvas, x, y, suurus, värv):
    canvas.create_rectangle(
        x, y,
        x + suurus, y + suurus,
        fill = värv
    )

joonista_ruut(canvas, 400, 340, 50, "pink")

aken.mainloop()