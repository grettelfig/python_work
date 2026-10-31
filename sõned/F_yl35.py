import tkinter as tk

aken = tk.Tk()
aken.title("Linnasiluett")

tahvel = tk.Canvas(aken, width=600, height=400, bg="#345596")
tahvel.pack()

# Kuu
tahvel.create_oval(420, 50, 520, 150, fill="#FFEB99", outline="")

# Hoonete mõõtmed
hoonete_x = [20, 110, 210, 320, 420]
hoonete_laiused = [80, 90, 100, 90, 140]
hoonete_korgused = [200, 170, 260, 220, 140]

# Hoonete joonistamine
for i in range(5):
    x = hoonete_x[i]
    laius = hoonete_laiused[i]
    korgus = hoonete_korgused[i]
    y = 400 - korgus

    tahvel.create_rectangle(x, y, x + laius, 400,
                            fill="#101B38", outline="")

    # Akende joonistamine
    for rida in range(0, korgus - 20, 25):
        for veerg in range(0, laius - 20, 20):
            akna_x = x + 10 + veerg
            akna_y = y + 15 + rida

            if (rida + veerg) % 3 == 0:
                varv = "yellow"
            else:
                varv = "#40557D"

            tahvel.create_rectangle(
                akna_x, akna_y,
                akna_x + 10, akna_y + 15,
                fill=varv, outline=""
            )

# Uks esimesele hoonele
tahvel.create_rectangle(45, 355, 70, 400,
                        fill="#53678D", outline="")

aken.mainloop()