arvude_arv = 0
summa = 0

with open("arvud.txt", encoding="utf-8") as fail:
    for rida in fail:
        print(rida.strip())
        arvude_arv += 1
        summa += int(rida)

print("Arvude arv: ", arvude_arv)
print("Arvude summa: ", summa)