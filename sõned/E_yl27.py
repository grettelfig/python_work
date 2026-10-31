import tkinter as tk

laius = 600
kõrgus = 400
taustavärv = "white"

aken = tk.Tk()
aken.title("Minu esimene graafika")

tahvel = tk.Canvas(
    aken,
    width=laius,
    height=kõrgus,
    bg=taustavärv)

tahvel.pack()

aken.mainloop()