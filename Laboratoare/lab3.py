import random
import math
import time
#1

fraza = input("Introdu fraza:")
cuvant = input("Introdu cuvantul de cenzurat:")

if cuvant in fraza:
    print("Fraza cenzurata:", fraza.replace(cuvant, len(cuvant)*"*"))
else:
    print("Cuvantul nu se afla in fraza")

#2

lista_persoane = []
nr_persoane = int(input("Introdu nr. de persoane:"))
for idx in range(nr_persoane):
    lista_persoane.append(input("Introdu persoana:"))
print("Lista sortata alfabetic este:", sorted(lista_persoane))
print("Castigatorul este:", random.choice(lista_persoane))

#3

inventar = {"mar": 10, "banana": 5, "biscuiti":30,
            "apa": 12, "suc": 20}
articol = input("Introdu articolul dorit:")
if articol in inventar:
    print("Articolul", articol, "exista in cantitate de", inventar[articol])
else:
    print("Articolul", articol, "nu este in stoc")

#4

raza = float(input("Introdu raza cercului:"))
print("Perimetrul este", 2*math.pi*raza)
print("Aria este", math.pi*raza*raza)

#5

nota_plata = float(input("Introduceti valoarea notei de plata: "))
numar_persoane = int(input("Introduceti numarul de persoane: "))
suma_per_persoana = nota_plata / numar_persoane
lei = math.floor(suma_per_persoana)
bani = round((suma_per_persoana - lei) * 100)
print("Fiecare persoana trebuie sa plateasca:", lei, "lei si", bani, "bani")

#6

print("Zarul 1:", random.randint(1,6), "Zarul 2:", random.randint(1,6))

#7

nume_ins = input("Introduceti numele institutiei:")
cuvinte = nume_ins.split()
acronim = ""
for cuvant in cuvinte:
    acronim += cuvant[0].capitalize()
print("Acronimul institutiei este:", acronim)

#8

fraza = input("Introdu o fraza:")
cuvinte = fraza.split()
frecventa_cuvinte = {}
for cuvant in cuvinte:
    if cuvant in frecventa_cuvinte:
        frecventa_cuvinte[cuvant] += 1
    else:
        frecventa_cuvinte[cuvant] = 1
print("Dictionarul de cuvinte este:", frecventa_cuvinte)

#9

nr_secret = random.randint(1, 100)
nr_jucator = int(input("Introdu un numar intre 1 si 100:"))
if(nr_jucator < 1 or nr_jucator > 100):
    print("Nu este in interval")
ghicit = False
while (not ghicit):
    if(nr_jucator > nr_secret):
        print("Numarul este mai mic")
        nr_jucator = int(input("Introdu un numar intre 1 si 100:"))
    elif(nr_jucator < nr_secret):
        print("Numarul este mai mare")
        nr_jucator = int(input("Introdu un numar intre 1 si 100:"))
    else:
        ghicit = True
print("Ai ghicit, numarul este", nr_secret)

#10

nr_fraze = int(input("Introdu numărul de fraze: "))
rezultate = {}

for i in range(nr_fraze):
    input("Apasa o tasta cand esti gata")
    start = time.time()
    fraza = input("Introdu fraza: ")
    end = time.time()
    timp = end - start
    rezultate[fraza] = timp
    print("Ai tastat fraza in", timp, "secunde.")

for fraza, timp in rezultate.items():
    print("Fraza:", fraza, "a fost scrisa in", timp, "secunde")

