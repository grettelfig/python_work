temperatuur = int(input("Sisesta temperatuur: "))
if temperatuur < 0:
    print("Külmub")
elif temperatuur >= 0 and temperatuur <= 15:
    print("Jahe")
elif temperatuur > 15 and temperatuur <= 25:
    print("Soe")
else:
    temperatuur > 25
    print("Palav")