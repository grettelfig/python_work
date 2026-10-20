õige_parool = "python123"
kasutaja_parool = str(input("Sisesta parool: "))

while kasutaja_parool != õige_parool:
    print("Vale parool!")
    kasutaja_parool = str(input("Sisesta parool: "))

print("Ligipääs lubatud!")