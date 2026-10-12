vanus = int(input("Sisesta vanus: "))
õpilane = input("Kas oled õpilane (jah/ei): ")

if vanus < 7:
    print("Pilet on tasuta.")
elif vanus >= 7 and vanus <= 17:
    print("Pilet maksab 5 eurot.")
elif vanus >= 65:
    print("Pilet maksab 6 eurot.")
elif õpilane == "jah" and vanus >= 18:
    print("Pilet maksab 8 eurot.")
else:
    print("Pilet maksab 12 eurot.")
