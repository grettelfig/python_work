sõna = str(input("Sisesta sõna: ")).lower()

if sõna == sõna[::-1]:
    print("Tegemist on palindroomiga.")
else:
    print("Tegemist ei ole palindroomiga")