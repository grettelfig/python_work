järjend = []
suurim = 0
väikseim = 0
keskmine = 0

with open("arvud.txt", encoding="utf-8") as fail:
    for rida in fail:
        järjend.append(int(rida.strip()))


print("Arvud: ", järjend)
print("Suurim arv: ", max(järjend))
print("Väikseim arv: ", min(järjend))
summa = sum(järjend)
keskmine = summa / len(järjend)
print("Keskmine: ", round(keskmine, 2))
kasvav = sorted(järjend)
print("Kasvav järjekord: ", kasvav)