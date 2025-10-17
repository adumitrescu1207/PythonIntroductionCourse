#1

nota = int(input("Introdu nota: "))
if nota in range(0, 50):
    print("Insuficient")
elif nota in range(50,70):
    print("Suficient")
elif nota in range(70,90):
    print("Bine")
elif nota in range(90,101):
    print("Foarte bine")
else:
    print("Nota incorecta")

#2

n = int(input("Introdu n="))
for index in range(n+1):
    print(index*"*")

#3

l = [11, 4, 23, 8, 16]
max = 0
for index in range(len(l)):
    if l[index] > max:
        max = l[index]
print("Numarul maxim din lista este:", max)

#4

sir = input("Introdu sirul: ")
if sir == sir[::-1]:
    print("Sirul este palindrom")
else:
    print("Sirul nu este palindorm")

#5

lista = list()
palindorm = True
dim_lista = int(input("Introdu dimensiunea listei: "))
for index in range(dim_lista):
   elem_lista = int(input("Introdu element: "))
   lista.append(elem_lista) 
print("Lista este:", lista)
if lista == lista[::-1]:
   print("Lista este palindrom")
else:
   print("Lista nu este palindrom")

#6

fraza = input("Introdu fraza: ")
vocale = {"a", "e", "i", "o", "u",
          "A", "E", "I", "O", "U"}
nr_vocale = 0
for ch in fraza:
    if ch in vocale:
        nr_vocale += 1
print("Nr. vocale:", nr_vocale)
print("Nr. consoane: ", len(fraza) - nr_vocale)

#7

agenda = {"Maria": "0712345678",
          "Andrei": "0722222222",
          "Mircea": "0766111222",
          "Daniel": "0744555999"
          }
nume = input("Introdu numele: ")
print("Numarul de telefon este:", agenda[nume])
