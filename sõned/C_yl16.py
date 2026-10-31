kasutajanimi = str(input("Sisesta kasutajanimi: "))
pikkus = len(kasutajanimi)

if 5 > pikkus or pikkus > 15:
    print("Viga: kasutajanime pikkus peab olema 5-15 tähemärki.")
elif not kasutajanimi.isalnum():
    print("Viga: kasutajanimi peab sisaldama ainult ladina tähti ja numbreid.")
elif not kasutajanimi[0].isalpha():
    print("Viga: kasutajanimi peab algama tähega.")
else:
    print("Kasutajanimi sobib.")