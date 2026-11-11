def positiivsed(arvud):
    järjend = []
    for arv in arvud:
        if arv > 0:
            järjend.append(arv)

    return järjend

print(positiivsed([3, -7, 0, 9, 23, -12, -5]))