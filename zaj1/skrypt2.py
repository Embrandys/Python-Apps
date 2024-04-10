import math
import random

wartosc=100
dodawanie=wartosc+123.15
potega=dodawanie**12
#print(potega)
tekst=str(potega)
wartosc_pi=math.pi
#print(wartosc_pi)
losowa=random.choice([1,2,3,4,5])
#print(losowa)
#stringi
tekst=f"Wartosc:{tekst}"
print(tekst)
print(f"Długosc zmiennej tekst: {len(tekst)}, wycinek {tekst[1:4]}")
print(tekst)
print(dir(tekst))
print(tekst.upper())
#tekst[1]="p"
#listy
lista=list(tekst)
lista=lista[0:8]
lista.append(list([1,2,3,4,5]))
lista.__delitem__(7)
print(lista)
lista2=[1,2,3,"banan", 100]
print(lista2)
#listy skladane
lista3=[liczba**2 for liczba in lista2 if liczba!='banan']
print(lista3)
lista4=list(range(2,17,2));
print(f"lista2:{lista2}, lista3:{lista3}, lista4:{lista4}")
#slowniki
ja={}
ja['imie']='Emilia'
ja['nazwisko']='Brandys'
ja['wiek']=22
ja['rodzice']=[{'imie':'Grazyna', 'wiek':66},{'imie':'Henryk', 'wiek':68}]
print(ja['rodzice'])
print(ja['rodzice'][0]['imie'])
print(ja.keys())
print('rodzenstwo' in ja)
#krotki
krotka1=(1,2,"3",4,2,5)
print(f"Dlugosc krotki: {len(krotka1)}, pierwszy wyraz: {krotka1[0]}")
#print(dir(krotka1))
#krotka1[0]=2
print(f'Wartosc 2 wystepuje {krotka1.count(2)} razy')
x=set("kalarepa")
y=set("lepy")
print(x&y)

#instrukcje
imiona=["Emilia", "Zuzanna", "Natalia", "Monika", "Rozalia", "Agata"]
for count,imie in enumerate(imiona):
    print(count,imie)

a=random.randint(0,100)
if a%2==0 and a>0:
    print(f"Liczba {a} jest dodatnia i jest parzysta")
else: print(f"Liczba {a}")

print("Wprowadź liczbę: ")
x=input()
if x != 0:
    print("Liczba różna od 0")

owoce=['jabłko', 'banan', 'pomarańcza']
print("Wprowadz nazwe owocu")
owoc=input()
if owoce.__contains__(owoc):
    print("Owoc jest dostepny")

suma=0
while suma<=100:
    print("Wprowadź liczbę: ")
    x=int(input())
    suma=suma+x
print(suma)

#Dziwactwa
L=[1,2,3,4]
M=[1,2,3,L,4]
print(f"Wartosc zmiennej M przed zmianą L:{M}")
L[1]="woooow"
print(f"Wartosc zmiennej M po zmianie L:{M}")

L=[4,5,6]
X=L*4
Y=[L]*4
print(f"X:{X}, Y:{Y}")
L[1]="wow"
print(f"X:{X}, Y:{Y}")

L=[4,5,6]
Y=[list(L)]*4
L[1]="wow"
print(f"Y:{Y}")
Y[0][1]="wow"
print(f"Y:{Y}")

