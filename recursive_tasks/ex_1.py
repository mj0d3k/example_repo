# fib
# max of list
# silnia
# sudoku

# suma z listy

"""
pseudokod:
jezeli lista jest pusta
to 0
jesli nie jest pusta
do pierwszego elemenu dodaj sumę kolejnych elementow listy
"""


def zad1(lista: list[float]) -> float:
    if len(lista) == 0:
        return 0
    else:
        element = lista.pop(0)
        suma_listy = element + zad1(lista)
        return suma_listy


print(zad1([]))
print(zad1([1]))
print(zad1([1, 2]))
print(zad1([1, 2, 3]))

# max z listy

"""
pseudokod:
jeżeli lista jest pusta zwróć None
jeżeli lista zawiera tylko jeden element
zwróć ten element
w przeciwnym razie
pierwszy_element := lista[0]
reszta_listy := lista[1:]
max_reszty := znajdz_max(reszta_listy)
jeżeli pierwszy_element > max_reszty
zwróć pierwszy_element
w przeciwnym razie
zwróć max_reszty
"""


def zad2(lista: list[float]) -> float | None:
    if not lista:
        return None
    if len(lista) == 1:
        return lista[0]
    else:
        el_1 = lista[0]
        reszta_el = lista[1:]
        max_reszta = zad2(reszta_el)
        if el_1 > max_reszta:
            return el_1
        else:
            return max_reszta

print(zad2([]))
print(zad2([1]))
print(zad2([1, 2]))
print(zad2([1, 2, 3]))
