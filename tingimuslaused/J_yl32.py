balance = 1000
pin = "1234"

kasutaja_pin = input("Sisesta PIN: ")
if kasutaja_pin != pin:
    print("Vale PIN.")
elif kasutaja_pin == pin:
    väljavõetav_summa = int(input("Sisesta väljavõetav summa: "))