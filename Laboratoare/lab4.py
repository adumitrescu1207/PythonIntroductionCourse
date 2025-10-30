import math
#1
class MyMath:
    def calcul_arie_drept(self, lungime: int, latime: int) -> int:
        return lungime * latime
    def calcul_arie_cerc(self, raza: float) -> float:
        return math.pi * raza * raza
    def calcul_arie_patrat(self, lungime: int) -> int:
        return lungime * lungime
    def calcul_arie_trapez(self, baza_mica: int, baza_mare: int, inaltime: int) -> float:
        return ((baza_mica + baza_mare) * inaltime / 2)
    def calcul_arie(self, shape, *sizes):
        shapes = {'drept': self.calcul_arie_drept,
                 'cerc': self.calcul_arie_cerc,
                 'patrat': self.calcul_arie_patrat,
                 'trapez': self.calcul_arie_trapez
        }
        if shape not in shapes:
            return -1
        return shapes[shape](*sizes)

if __name__ == "__main__":
    while True:
        my_math = MyMath()
        shape = input("Introdu forma geometrica: ").strip().lower()
        sizes = [float(x) for x in input("Introdu dimensiunile: ").split()]
        print("Aria:", my_math.calcul_arie(shape, *sizes))



