toodete_arv = 0
kogusumma = 0

while True:
    hind = float(input("Sisesta hind: "))

    if hind == 0:
        break

    toodete_arv += 1
    kogusumma += hind 

print("Tooteid: ", toodete_arv)
print("Kokku: ", kogusumma)