def stworz_raport(*args, **kwargs):
    raport = ""
    for id in args:
        nazwa = kwargs.get(f"nazwa_{id}", "")
        cena = kwargs.get(f"cena_{id}", "")
        raport += f"Produkt o ID {id}: {nazwa}, Cena: {cena}\n"
    print("RAPORT:")
    print(raport)