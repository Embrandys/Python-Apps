def stworz_funkcje_potegujaca(wykladnik:int) -> int:
    def poteguj(podstawa:int)->int:
        return podstawa**wykladnik
    return poteguj