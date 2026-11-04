arv = 0

with open("linnad.txt", encoding="utf-8") as fail:
    for rida in fail:
        print(rida.strip())
        arv += 1

print("Linnade arv: ", arv)

