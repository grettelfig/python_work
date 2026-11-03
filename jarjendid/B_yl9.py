ostukorv = []
tooteid = 0

while len(ostukorv) < 5:
    kasutajalt = input("Lisa ostukorvi toode: ")
    ostukorv.append(kasutajalt)
    tooteid += 1

print("Ostukorvis: ", ostukorv)
print("Tooteid kokku: ", tooteid)