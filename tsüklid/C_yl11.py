arv = 1
summa = 0

while arv <= 5:
    sisestatud_arv = int(input("Sisesta " + str(arv) + ". arv: "))
    summa = summa + sisestatud_arv
    arv = arv + 1

print("Arvude summa on", summa)