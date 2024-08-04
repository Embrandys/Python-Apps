def licznik():
    licznik=0
    def licznik_stanu():
        nonlocal licznik
        licznik+=1
        return licznik
    return licznik_stanu