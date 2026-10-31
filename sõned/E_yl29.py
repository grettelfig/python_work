import tkinter as tk
aken = tk.Tk()
aken.title("Eesti lipp")

tahvel = tk.Canvas(
    aken,
    width=600,
    height=300,
    bg="white")

tahvel.pack()

tahvel.create_rectangle(0, 0, 600, 100, fill="blue")
tahvel.create_rectangle(0, 100, 600, 200, fill="black")
tahvel.create_rectangle(0, 200, 600, 300, fill="white")

aken.mainloop()