parool = input("Sisesta parool: ")
tähemärgid = len(parool)
punktid = 0
suuri_tahti_kokku = 0
vaikeseid_tahti_kokku = 0
numbrid_kokku = 0
erimargid_kokku = 0



for i in range(len(parool)):
    if parool[i].isalpha():
        if parool[i] == parool[i].upper():
            suuri_tahti_kokku += 1; punktid += 1
        if parool[i] == parool[i].lower():
                vaikeseid_tahti_kokku += 1; punktid += 1
    elif parool[i].isnumeric():
         numbrid_kokku += 1; punktid += 1
    else:
         erimargid_kokku += 1; punktid += 1

if tähemärgid >= 8:
    punktid += 1

if punktid == 0 or punktid == 1 or punktid == 2:
    print("Tulemus: ", punktid,"/5")
    print("Hinnang: Nõrk parool.")

elif punktid == 3 or punktid == 4:
    print("Tulemus: ", punktid,"/5")
    print("Hinnang: Keskmine parool.")

elif punktid == 5:
    print("Tulemus: ", punktid,"/5")
    print("Hinnang: Kõik nõuded täidetud. Tubli!")

elif erimargid_kokku < 1:
     print("Puudub erimärk.")

elif numbrid_kokku < 1:
    print("Puudub number.")

elif suuri_tahti_kokku < 1:
    print("Puudub suurtäht.")

elif vaikeseid_tahti_kokku < 1:
    print("Puudub väiketäht.")

elif tähemärgid < 8:
    print("Parooli pikkus peab olema vähemalt 8 tähemärki.")

else:
    print("Parool vastab nõuetele.")