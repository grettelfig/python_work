kuu = int(input("Sisesta kuu number: "))
päev = int(input("Sisesta päev: "))
if kuu == 1 or kuu == 3 or kuu == 5 or kuu == 7 or kuu == 8 or kuu == 10 or kuu == 12:
    if päev <= 31:
        print("Kuupäev on korrektne.")
    else:
        print("Kuupäev ei ole korrektne.")
elif kuu == 4 or kuu == 6 or kuu == 9 or kuu == 11:
    if päev <= 30:
        print("Kuupäev on korrektne.")
    else:
        print("Kuupäev ei ole korrektne.")
elif kuu == 2:
    if päev <= 28:
        print("Kuupäev on korrektne.")
    else:
        print("Kuupäev ei ole korrektne.")