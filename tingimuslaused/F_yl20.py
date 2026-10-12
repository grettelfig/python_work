esimene_külg = int(input("Sisesta esimese külje pikkus: "))
teine_külg = int(input("Sisesta teise külje pikkus: "))
kolmas_külg = int(input("Sisesta kolmanda külje pikkus: "))

if esimene_külg + teine_külg > kolmas_külg:
    print("Kolmnurk on võimalik.")
else:
    print("Kolmnurk ei ole võimalik.")