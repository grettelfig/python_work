tekst = str(input("Sisesta tekst: "))
tähem_koguarv = len(tekst)
kokku = len(tekst)
tyhikud = tekst.count(" ")
sõnad = tekst.split()
täish = "aeiouõäöü"
numbrid = "1234567890"
täish_arv = 0
numbrite_arv = 0

ilma_tyhi = kokku - tyhikud

for täht in tekst:
    if täht.lower() in täish:
        täish_arv += 1
    if täht in numbrid:
        numbrite_arv += 1

print("Tähemärke kokku: ", tähem_koguarv)
print("Tähemärke ilma tühikuteta: ", ilma_tyhi)
print("Sõnu: ", len(sõnad))
print("Täishäälikuid: ", täish_arv)
print("Numbreid: ", numbrite_arv)