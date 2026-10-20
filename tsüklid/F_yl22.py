rahvaarv = 50000
aastaarv = 1

while rahvaarv <= 60000:
    rahvaarv = round(rahvaarv + rahvaarv * 0.02, 1)
    aastaarv = aastaarv + 1

print("Aastaid kulus: ", aastaarv)
print("Elanike arv: ", rahvaarv)

