arve_kokku = 0
summa = 0

while True:
    sisestatud_arv = int(input("Sisesta arv: "))

    if sisestatud_arv == 0:
        break

    arve_kokku += 1
    summa += sisestatud_arv

print("--- TULEMUSED ---")
print("Sisestatud arve: ", arve_kokku)
print("Summa: ", summa)
print("Keskmine: ", round(summa / arve_kokku, 2))
print("    ")
if sisestatud_arv % 2 == 0:
    print("Positiivseid arve: ", )