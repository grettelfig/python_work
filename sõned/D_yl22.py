epost = str(input("Sisesta e-post: "))

if epost.count("@") != 1:
    print("Viga: aadress peab sisaldama ühte @ märki.")
elif epost.find("@") == 0:
    print("Viga: @ ees peab olema vähemalt üks tähemärk.")
elif "." not in epost:
    print("Viga: domeeniosas peab olema punkt.")
elif epost[epost.find("@") + 1] == "." or epost[-1] == ".":
    print("Viga: domeeniosa ei tohi alata ega lõppeda punktiga.")
elif " " in epost:
    print("Viga: aadressis ei tohi olla tühikuid.")
else:
    print("Aadressi kuju on sobiv.")