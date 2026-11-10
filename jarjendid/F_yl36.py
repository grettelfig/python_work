tooted = []
hinnad = []


toote_nimi = input("Sisesta toote nimi (lõpetamiseks ENTER): ")

while toote_nimi != "":
    hind = float(input("Sisesta toote hind: "))


    tooted.append(toote_nimi)
    hinnad.append(hind)

    toote_nimi = input("Sisesta toote nimi (lõpetamiseks ENTER): ")

kallim_hind = max(hinnad)
indeks = hinnad.index(kallim_hind)
kallim_toode = tooted[indeks]

print("Ostukorvi sisu: ", tooted)
print("Toodete arv: ", len(tooted))
print("Kogumaksumus: ", sum(hinnad))
print("Kõige kalleim toode: ", kallim_toode, " ", kallim_hind)
