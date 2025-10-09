#1
a = int(input("a="))
b = int(input("b="))
c = int(input("c="))

print(str(a) + "+" + str(b) + " =", a + b)
print(str(a) + "+" + str(c) + " =", a + c)
print(str(b) + "+" + str(c) + " =", b + c)

#2
baza = float(input("Baza ="))
inaltimea = float(input("Inaltimea ="))

print("Aria =", (baza*inaltimea)/2)

#3
lungime = float(input("Lungimea = "))
latime = float(input("Latimea = "))
n = float(input("Limita n = "))

if (2*lungime + 2*latime > n):
    print("Perimetrul",  2*lungime + 2*latime, "este mai mare decat limita", n)
else:
    print("Perimetrul",  2*lungime + 2*latime, "este mai mic decat limita", n)

#4
varsta = int(input("Varsta: "))
print("Varsta in zile este:", 365*varsta)

#5
cuvant = input("Cuvantul: ")
n = int(input("Nr. repetitii: "))
print(n*cuvant)

#6
val_nota_plata = float(input("Valoarea notei de plata: "))
nr_persoane = int(input("Numar de persoane: "))

if((val_nota_plata/nr_persoane)%1 != 0):
    print(int(val_nota_plata/nr_persoane), "lei si", round((val_nota_plata/nr_persoane)%1,2), "de bani")
else:
    print(int(val_nota_plata/nr_persoane), "lei")

#7
grade_celsius = int(input("Temperatura in grade Celsius: "))
print("Temperatura in grade Fahrenheit:", float((grade_celsius*9/5)+32))

#8
caracter = input("Caracterul: ")
for i in range(3):
    print((i+1)*caracter)

#9
#def media_aritmetica():
a = int(input("a = "))
b = int(input("b = "))
a, b = b, a
print("a =", a)
print("b =", b)
print("Media aritmetica: ", float((a+b)/2))


# if __name__ == "__main__":
#     media_aritmetica()