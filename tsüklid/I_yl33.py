from random import randint

salajane = randint(1, 100)
kasutaja_arv = int(input("Arva ära arv 1-100: "))

while kasutaja_arv != salajane:
    if kasutaja_arv < salajane:
        print("Salajane arv on suurem.")
    if kasutaja_arv > salajane:
        print("Salajane arv on väiksem.")
    kasutaja_arv = int(input("Arva ära arv 1-100: "))
else:
    print("Õige!")