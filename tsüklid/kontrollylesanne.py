arve_kokku = 0
summa = 0
positiivne_arv = 0
negatiivne_arv = 0
paarisarv = 0
paaritu_arv = 0

while True:
    sisestatud_arv = int(input("Sisesta arv: "))

    if sisestatud_arv == 0:
        break

    if sisestatud_arv > 0:
        positiivne_arv += 1
    elif sisestatud_arv < 0:
        negatiivne_arv += 1

    if sisestatud_arv % 2 == 0:
        paarisarv += 1
    else:
        paaritu_arv += 1

    arve_kokku += 1
    summa += sisestatud_arv

print("--- TULEMUSED ---")
print("Sisestatud arve: ", arve_kokku)
print("Summa: ", summa)
print("Keskmine: ", round(summa / arve_kokku, 2))
print("    ")
print("Positiivseid arve: ", positiivne_arv)
print("Negatiivseid arve: ", negatiivne_arv)
print("Paarisarve: ", paarisarv)
print("Paarituid arve: ", paaritu_arv)



    