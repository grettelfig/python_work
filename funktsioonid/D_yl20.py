def arvu_tyyp(arv):
    if arv > 0:
        arv = "Positiivne"
    elif arv < 0:
        arv = "Negatiivne"
    else:
        arv = "Null"

    return arv

minu_arv = arvu_tyyp(0)
print(minu_arv)