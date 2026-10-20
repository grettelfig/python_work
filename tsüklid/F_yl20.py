pangakonto = 1000
aastaarv = 1

while aastaarv <= 10:
    pangakonto = round(pangakonto + pangakonto * 0.05, 2)
    print(aastaarv, ". aasta: ", pangakonto)
    aastaarv = aastaarv + 1
    