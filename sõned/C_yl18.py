lause = input("Sisesta lause: ").lower()

taish = "aeiouõäöü"
kokku = 0

for taht in lause:
    if taht in taish:
        kokku += 1

a = lause.count("a")
e = lause.count("e")
i = lause.count("i")
o = lause.count("o")
u = lause.count("u")
õ = lause.count("õ")
ä = lause.count("ä")
ö = lause.count("ö")
ü = lause.count("ü")

print("Täishäälikuid kokku:", kokku)
print("a:", a, ", e:", e, ", i:", i, ", o:", o, ", u:", u)
