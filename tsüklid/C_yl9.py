i = 1 # i on 1
summa = 0 # summa on 0

while i <= 5: # samal ajal, kui i on väiksem kui või võrdne 5-ga
    summa = summa + i # , siis summale lisatakse iga kord juurde i ning
    i = i + 1 # ning i-le lisatakse juurde 1 iga kord
# lõpuks läheb see nii, et 0 + 1, 1 + 2, 3 + 3, 6 + 4, 10 + 5 (mis = 15)
print(summa) # ehk siia tuleb lõpptulemusena 15
