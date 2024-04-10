import json

with open('teksty.json') as teksty:
    data=json.load(teksty)

polaczone=""
for i in data['teksty']:
    for klucz, wartosc in i.items():
        print(klucz)
        print(wartosc)
        polaczone=polaczone+wartosc

print(polaczone)
lower=polaczone.lower()
print(lower)
interp=[".", ","]
for i in interp:
    lower=lower.replace(i, '')
lista=lower.split()
lista=[slowo[:-1]+slowo[-1].upper() for slowo in lista]
listaAa=[slowo for slowo in lista if slowo.__contains__("A") or slowo.__contains__("a")]
uniq=set(listaAa)
print(uniq)
count={}
for i in uniq:
    count[i]=listaAa.count(i)
print(count)

zmienne= {
    "unikatowe_wyrazy":list(uniq),
    "wystąpienia":count
}

print(zmienne)

json_object=json.dumps(zmienne, indent=2)
with open('zmienne.json', 'w') as outfile:
    outfile.write(json_object)