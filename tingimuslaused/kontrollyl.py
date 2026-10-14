nimi = str(input("Sisesta oma nimi: "))
punktisumma = int(input("Sisesta punktisumma: "))
puudumiste_arv = int(input("Sisesta puudumiste arv: "))
esitatud_tood = str(input("Kas kõik tööd on esitatud (jah/ei): "))

print("Õpilane:", nimi)
if punktisumma >= 90:
    print("Hinne: 5")
elif punktisumma >= 75 and punktisumma <= 89:
    print("Hinne: 4")
elif punktisumma >= 50 and punktisumma <= 74:
    print("Hinne: 3")
elif punktisumma >= 20 and punktisumma <= 49:
    print("Hinne: 2")
else:
    print("Hinne: 1")

if puudumiste_arv > 10:
    print("Hoiatus: liiga palju puudumisi.")
else:
    print("Puudumiste arv on lubatud.")

if esitatud_tood == "ei":
    print("Kõik tööd ei ole esitatud.")
else:
    print("Kõik tööd on esitatud.")

if punktisumma >= 50 and puudumiste_arv <= 10 and esitatud_tood == "jah":
    print("Aine on läbitud.")
else:
    print("Aine ei ole läbitud.")