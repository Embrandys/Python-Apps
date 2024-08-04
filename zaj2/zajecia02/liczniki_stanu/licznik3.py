def licznik():
    if not hasattr(licznik, 'licznik_stanu'):
        licznik.licznik_stanu=0
    licznik.licznik_stanu+=1
    return licznik.licznik_stanu