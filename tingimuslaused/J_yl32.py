balance = 1000
pin = "1234"

kasutaja_pin = input("Sisesta PIN: ")
if kasutaja_pin != pin:
    print("Vale PIN.")
elif kasutaja_pin == pin:
    väljavõetav_summa = int(input("Sisesta väljavõetav summa: "))
    if väljavõetav_summa <= 0:
            print("Viga! Summa peab olema positiivne.")
    elif väljavõetav_summa > 1000:
            print("Viga! Summa ületab kontojääki.")
    elif väljavõetav_summa % 10 != 0:
        print("Viga! Summa peab jaguma 10-ga.")
    else:
        print("Raha väljastatud: ", väljavõetav_summa, " eurot. Kontole jäi: ", balance - väljavõetav_summa, " eurot.")