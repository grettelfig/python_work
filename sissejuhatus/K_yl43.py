print("Nädalapäevad tähistatakse: esmaspäev = 0, teisipäev = 1, kolmapäev = 2, neljapäev = 3, reede = 4, laupäev = 5, pühapäev = 6")
esmaspäev = 0
teisipäev = 1
kolmapäev = 2
neljapäev = 3
reede = 4
laupäev = 5
pühapäev = 6
päev = int(input("Sisesta nädalapäeva number: "))
edasi = int(input("Sisesta, mitu päeva edasi soovid liikuda: "))
uus_päev = (päev + edasi) % 7
if uus_päev == esmaspäev:
    print("Uus päev on esmaspäev")
elif uus_päev == teisipäev:
    print("Uus päev on teisipäev")
elif uus_päev == kolmapäev:
    print("Uus päev on kolmapäev")
elif uus_päev == neljapäev:
    print("Uus päev on neljapäev")
elif uus_päev == reede:
    print("Uus päev on reede")
elif uus_päev == laupäev:
    print("Uus päev on laupäev")
else:
    print("Uus päev on pühapäev")  