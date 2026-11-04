temperatuurid = [12, 18, 25, 9, 31, 22, 16, 28, 7]
soojad_temp = []
jahedad_temp = []

for kraad in temperatuurid:
    if kraad >= 20:
        soojad_temp.append(kraad)
    else:
        jahedad_temp.append(kraad)

print("Soojad temperatuurid: ", soojad_temp)
print("Jahedad temperatuurid: ", jahedad_temp)
