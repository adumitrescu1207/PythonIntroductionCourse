# Tupluri

t = (1, "doi", 3.0)
print("Tuplul t:", t, type(t))

t_un_elem = (1, )
print("Tuplul cu un element: ", t_un_elem, type(t_un_elem))

t1 = (1, "doi") + ("trei", 4)
print("Primul tuplu concatenat: ", t1)

t2 = (1, "doi") + (3,)
print("Al doilea tuplu concatenat: ", t2)

t3 = (1, "doi") * 2
print("Tuplu dublat", t3)

tuplu = (1, 2, 3, 4)
(a, b, c, d) = tuplu
print("a:", a, "b:", b, "c:", c, "d:", d)

(x, y, *z) = tuplu
print("x:", x, "y:", y, "z:", z)

#Liste

l = [1, 2, 3, 4, 5]
print("Lista:", l)

l_dif = [False, 1, "doi", 3.0]
print("Lista cu elem. dif. :", l_dif)

print("Concatenare liste:", l + l_dif)

#Dictionare

note = {
    "Ana":9,
    "Andrei":10,
    "George":5
}
print("Dictionar de note:", note)
print("Nota Anei:", note["Ana"])