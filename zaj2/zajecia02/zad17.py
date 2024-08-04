def zamowienie_produktu(nazwa_produktu, *, cena, ilosc):
    pass
    wartosc=cena*ilosc
    podsum=f"Podsumowanie zamówienia: \nNazwa produktu: {nazwa_produktu} \nŁączna cena: {cena*ilosc}\n ilosc: {ilosc}"
    return podsum, wartosc