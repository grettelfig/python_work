# Õpilase päev
nimi = str(input("Sisesta oma nimi: "))
vanus = int(input("Sisesta oma vanus: "))
koolitee = float(input("Sisesta koolitee pikkus kilomeetrites: "))
aeg_minutites = float(input("Sisesta koolitee läbimise pikkus minutites: "))
järgmise_aasta_vanus = vanus + 1
koolitee_meetrites = koolitee * 1000
tunnid = aeg_minutites // 60
keskmine_kiirus = koolitee / aeg_minutites

print("Tere, " + nimi + "!")
print("Järgmisel aastal oled " + str(järgmise_aasta_vanus) + "-aastane")
print("Sinu koolitee pikkus on " + str(koolitee_meetrites) + " meetrit.")
print("Koolitee kestab " + str(tunnid) + " tundi ja " + str(aeg_minutites) + " minutit.")
print("Keskmine kiirus on " + str(keskmine_kiirus) + " km/h.")