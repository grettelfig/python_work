import tkinter as tk

aken = tk.Tk()
aken.title("Malelaud")

tahvel = tk.Canvas(aken, width=400, height=400, bg="white")
tahvel.pack()

ruut = 50

for rida in range(8):
    for veerg in range(8):
        x1 = veerg * ruut
        y1 = rida * ruut
        x2 = x1 + ruut
        y2 = y1 + ruut

        if (rida + veerg) % 2 == 0:
            varv = "beige"
        else:
            varv = "black"

        tahvel.create_rectangle(x1, y1, x2, y2,
                                fill=varv, outline=varv)

aken.mainloop()