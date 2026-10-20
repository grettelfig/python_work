from random import randint

kord = 1
summa = 0

while kord <= 10:
    juhuarv = randint(1, 6)
    print(kord, ". vise: ", juhuarv)
    summa = summa  + juhuarv
    kord = kord + 1

print("Visete summa: ", summa)
print("Keskmine tulemus: ", summa / 10) 