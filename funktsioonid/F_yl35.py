arv = 100

def muuda():
    arv = 20
    print("Funktsioonis:", arv)

muuda()
print("Põhiprogrammis:", arv)

# arv ei muutu põhiprogrammis, kuna arv = 20 muutuja on muuda() funktsiooni sees, väljaspool seda funktsiooni ei eksisteeri arv muutuja 20-nena, vaid 100-na.