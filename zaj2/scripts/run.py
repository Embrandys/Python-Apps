from zajecia02 import *
from zajecia02.liczniki_stanu import *
#6
dane=(2024, 'Python', 3.8)
rok, jezyk, wersja=dane
print(dane)
print(f"{rok}, {jezyk}, {wersja}")
#7
oceny=[4,3,5,2,5,4]
pierwsza, *srodek, ostatnia=oceny
print(f"{pierwsza}, {ostatnia}, {srodek}")
#8
info = ('Jan', 'Kowalski', 30, 'Polska', 'programista')
imie, nazwisko, _, _, zawod=info
print(zawod)
#9
dane = (2024, ['Python', 3.8, ('Stabilna', 'Wersja')])
rok, (jezyk, wersja, *opis)=dane
print(f"{rok}, {jezyk}, {wersja}, {opis}")
#10
a = b = [1, 2, 3]
b[0]='zmieniono'
print(f"a: {a}, b:{b}")
#są mutowalne
#11
c=a[:]
c[0]='nowa wartosc'
print(f"a: {a}, b: {b}, c: {c}")
#12
x=y=10
y=y+1
print(f"x: {x}, y: {y}")
#intigery nie sa mutowalne
#13
K=[1,2]
L=K
K=K+[3,4]
M=[1,2]
N=M
M+=[3,4]
print(f"K: {K}, L: {L}, M: {M}, N:{N}")
#14
imiona=['Anna', 'Jan', 'Ewa']
oceny=[5,4,3,2]
zip=zip(imiona, oceny)
for imie, ocena in zip:
    print(f"{imie} : {ocena}")
#jesli listy nie sa rowne, wtedy dlugosc par jest dlugosci krotszej listy
#15
liczby=[1,2,3,4,5]
lista_kw=list(map(zad15.kwadrat, liczby))
print(lista_kw)
#16
lista=['elo','hejka','siema']
liczba=24
print(f"lista: {lista}, liczba: {liczba}")
print(f"PO: lista: {zad16.zmien_wartosc(lista)}, liczba: {zad16.zmien_wartosc(liczba)}")
#17
returns=[]
returns.append(zad17.zamowienie_produktu("gogle", cena=300, ilosc=2))
returns.append(zad17.zamowienie_produktu("piłka", cena=50, ilosc=3))
returns.append(zad17.zamowienie_produktu("hula-hop", cena=30, ilosc=10))
suma=0
for i, j in returns:
    print(i)
    print(f"Wartosc zamowienia: {j}")
    suma=suma+j
print(f"Sumaryczna wartosc zamowien: {suma}")
#18
zad18.stworz_raport(101, 102, nazwa_101="Kubek termiczny", cena_101="45.99 zł", nazwa_102="Długopis", cena_102="4.99 zł")
#19
potega_2 = zad19.stworz_funkcje_potegujaca(2) # Tworzy funkcję potęgującą do kwadratu
print(potega_2(4)) # Wynik: 16
#20
#a nonlocal
liczniczek=licznik1.licznik()
print(liczniczek())
print(liczniczek())

#b global


print(licznik2.licznik2())
print(licznik2.licznik2())
print(licznik2.licznik2())

#__init__ i __call__

class klasa_licznik:
    def __init__(self):
        self.licznik=0
    def __call__(self):
        self.licznik += 1
        return self.licznik
object=klasa_licznik()
print(object())
print(object())

#atrybut funkcji

print(licznik3.licznik())
print(licznik3.licznik())
print(licznik3.licznik())

#22

lista_ksiazek = [{'tytul': 'Gra o tron', 'autor': 'George R. R. Martin', 'rok_wydania': '1996'},
                 {'tytul': 'Władca Pierścieni', 'autor': 'J.R.R. Tolkien', 'rok_wydania': '1954'},
                 {'tytul': 'Harry Potter i Kamień Filozoficzny', 'autor': 'J.K. Rowling', 'rok_wydania': '1997'},
                 {'tytul': 'Ballada ptaków i węży', 'autor': 'Suzanne Collins', 'rok_wydania': '2020'}]
#a
x=sorted(lista_ksiazek, key=lambda x: x['rok_wydania'])
for i in x:
    print(i)
#b
x=filter(lambda x: x if(x['rok_wydania']>'2000') else None, lista_ksiazek)
for i in x:
    print(i)

#c
lista=map(lambda x: x['tytul'],lista_ksiazek)
for i in lista:
    print(i)

#23 generatory
for dzien in zad23.generator():
    print(dzien)

x=zad23.generator()
print(next(x))
print(next(x))
print(next(x))
