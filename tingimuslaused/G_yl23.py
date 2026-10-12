balance = 500
väljavõetav_summa = int(input("Sisesta väljavõetav summa: "))
if väljavõetav_summa <= 0:
    print("Vigane summa.")
else:
    if väljavõetav_summa > balance:
        print("Kontol pole piisavalt raha.")
    if väljavõetav_summa <= balance:
        balance -= väljavõetav_summa
        print("Raha väljastatud. Kontole jäi", balance, "eurot.")