esimene_arv = int(input("Sisesta esimene arv: "))
tehe = str(input("Sisesta tehe (+, -, *, /): "))
teine_arv = int(input("Sisesta teine arv: "))

if tehe == "+":
    print("Summa on:" ,esimene_arv + teine_arv)
elif tehe == "-":
    print("Vahe on:" ,esimene_arv - teine_arv)
elif tehe == "*":
    print("Korrutis on:" ,esimene_arv * teine_arv)
elif tehe == "/":
    print("Jagatis on:" ,esimene_arv / teine_arv)
elif tehe != "+" or tehe != "-" or tehe != "*" or tehe != "/":
    print("Tundmatu tehe.")
