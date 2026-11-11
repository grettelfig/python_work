def rea_summa(hind, kogus):
    return hind * kogus

def lisa_käibemaks(summa, määr):
    return summa + summa * määr / 100

def kuva_kokkuvõte(summa, määr):
    ekraanile = lisa_käibemaks(summa, määr)
    print(ekraanile)

esimene = rea_summa(4, 3)
teine = rea_summa(6, 2)
kolmas = rea_summa(2, 8)
kokku = esimene + teine + kolmas
kuva_kokkuvõte(kokku, 20)