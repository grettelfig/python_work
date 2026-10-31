import tkinter as tk

aken = tk.Tk()
aken.title("Minu esimene graafika")

tahvel = tk.Canvas(
    aken,
    width=600,
    height=400,
    bg="white")

tahvel.pack()

tahvel.create_rectangle(140, 50, 260, 350, fill="black")
tahvel.create_oval(160, 70, 240, 150, fill="red")
tahvel.create_oval(160, 160, 240, 240, fill="yellow")
tahvel.create_oval(160, 250, 240, 330, fill="green")

aken.mainloop()