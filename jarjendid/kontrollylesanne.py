nimed = []
punktid = []
vahemalt_50 = 0
vahem_kui_50 = 0
i = 0 # alustame järjendi esimesest elemendist

with open("kontrolltoo.csv", encoding="utf-8") as fail:
    for rida in fail:
        osad = (rida.strip().split(";"))

        nimi = osad[0]
        punkt = int(osad[1])

        nimed.append(nimi)
        punktid.append(punkt)



while i < len(punktid):
    if punktid[i] >= 50:
        vahemalt_50 += 1
    else:
        vahem_kui_50 += 1

    i += 1

hinne = 0
hinne1 = 0
hinne2 = 0
hinne3 = 0
hinne4 = 0
hinne5 = 0
hinded = []

for punkt in punktid:
    if punkt >= 90:
        hinne = 5
    elif punkt >= 75:
        hinne = 4
    elif punkt >= 50:
        hinne = 3
    elif punkt >= 20:
        hinne = 2
    else:
        hinne = 1

    hinded.append(hinne)
suurim = max(punktid)
indeks = punktid.index(suurim)
inimene = nimed[indeks]

väikseim = min(punktid)
indeks2 = punktid.index(väikseim)
inimene2 = nimed[indeks2]

summa = sum(punktid)

print("KONTROLLTÖÖ TULEMUSED")
print("")
for i in range(len(nimed)):
    print(i + 1, ".", nimed[i], "-", punktid[i], "punkti - hinne", hinded[i])

print("")
print("KONTROLTÖÖ STATISTIKA")
print("")
print("Õpilaste koguarv: ", len(nimed))
print("Keskmine punktisumma: ", summa / len(punktid))
print("Suurim punktisumma: ", inimene, ",", suurim)
print("Väikseim punktisumma: ", inimene2, ",", väikseim)
print("Vähemalt 50 punkti said: ", vahemalt_50)
print("Alla 50 punkti said: ", vahem_kui_50)

õpilase_nimi = input("Sisesta õpilase nimi: ").lower()

leitud = False

for i in range(len(nimed)):
    if õpilase_nimi == nimed[i].lower():
        leitud = True 
        
        print("ÕPILASE OTSIMINE")
        print("")
        print("Õpilane: ", nimed[i])
        print("Punktid: ", punktid[i])
        print("Hinne: ", hinded[i])
        break

if leitud == False:
    print("Sellist õpilast ei leitud.")