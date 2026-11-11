def poora_sone(tekst):
    tulemus = ""

    for täht in tekst:
        tulemus = täht + tulemus

    return tulemus

print(poora_sone("programmeerimine"))