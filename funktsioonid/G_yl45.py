from tkinter import *

aken = Tk()

canvas = Canvas(aken, width=600, height=400, bg="#293B65")
canvas.pack()

def joonista_hoone(canvas, x, y, laius, korgus, varv):
    canvas.create_rectangle(
        x, y,
        x + laius, y + korgus,
        fill=varv
    )
def joonista_aken(canvas, x, y, suurus, varv):
    canvas.create_rectangle(
        x, y,
        x + suurus, y + suurus,
        fill=varv
    )
def joonista_kuu(canvas, x, y, raadius):
        canvas.create_oval(
        x - raadius,
        y - raadius,
        x + raadius,
        y + raadius,
        fill="lightyellow"
    )

def joonista_linn(canvas):
    joonista_hoone(canvas, 30, 180, 80, 220, "#394761")
    joonista_hoone(canvas, 120, 130, 80, 270, "#52647C")
    joonista_hoone(canvas, 210, 200, 80, 200, "#394761")
    joonista_hoone(canvas, 300, 150, 80, 250, "#52647C")
    joonista_hoone(canvas, 390, 190, 80, 210, "#394761")

    for x, y in [(30, 180), (120, 130), (210, 200), (300, 150), (390, 190)]:
        for rida in range(3):
            for veerg in range(3):
                joonista_aken(
                    canvas,
                    x + 10 + veerg * 25,
                    y + 20 + rida * 30,
                    15,
                    "yellow"
                )

    joonista_kuu(canvas, 450, 80, 35)

joonista_linn(canvas)

aken.mainloop()