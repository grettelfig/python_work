parool = str(input("Sisesta parool: "))
tähemärk = len(parool)

if tähemärk < 8:
    print("Parool on liiga lühike!")
elif tähemärk == 8 or tähemärk == 9 or tähemärk == 10 or tähemärk == 11:
    print("Parooli pikkus on sobiv.")
else:
    print("Parool on liiga pikk!")