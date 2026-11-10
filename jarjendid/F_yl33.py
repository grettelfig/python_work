hinded = [4, 5, 3, 4, 2, 5, 5, 3, 4, 5, 2, 4]
koguarv = 0
summa = sum(hinded)
keskmine = summa / len(hinded)
sagedamini_esinev = 0
positiivsed_hinded = 0
mitterah_hinded = 0
hinne1 = 0
hinne2 = 0
hinne3 = 0
hinne4 = 0
hinne5 = 0

for hinne in hinded:
    if hinne == 1:
        hinne1 += 1
    elif hinne == 2:
        hinne2 += 1
    elif hinne == 3:
        hinne3 += 1
    elif hinne == 4:
        hinne4 += 1
    elif hinne == 5:
        hinne5 += 1

suurim = max(hinne1, hinne2, hinne3, hinne4, hinne5)

for arv in hinded:
    if arv >= 3 and arv <= 5:
        positiivsed_hinded += 1
    else:
        mitterah_hinded += 1

    koguarv += 1

print("Hinnete koguarv: ", koguarv)
print("Keskmine hinne: ", round(keskmine, 2))
if hinne1 == suurim:
    print("Kõige sagedasem hinne: 1")

if hinne2 == suurim:
    print("Kõige sagedasem hinne: 2")

if hinne3 == suurim:
    print("Kõige sagedasem hinne: 3")

if hinne4 == suurim:
    print("Kõige sagedasem hinne: 4")

if hinne5 == suurim:
    print("Kõige sagedasem hinne: 5")
print("Positiivseid hindeid: ", positiivsed_hinded)
print("Mitterahuldavaid hindeid: ", mitterah_hinded)
print("Hinne 1: " + "*" * hinne1)
print("Hinne 2: " + "*" * hinne2)
print("Hinne 3: " + "*" * hinne3)
print("Hinne 4: " + "*" * hinne4)
print("Hinne 5: " + "*" * hinne5)
