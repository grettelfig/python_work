from random import randint

salajane = randint(1, 10)
kasutaja_arv = int(input("Arva ära arv 1-10: "))

while kasutaja_arv != salajane:
    print("Vale arv! Proovi uuesti.")
    kasutaja_arv = int(input("Arva ära arv 1-10: "))

print("Õige!")