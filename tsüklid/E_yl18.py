kasutaja_arv = int(input("Sisesta positiivne arv: "))

while kasutaja_arv <= 0:
    print("Vigane sisend.")
    kasutaja_arv = int(input("Sisesta arv: "))

print("Aitäh!")