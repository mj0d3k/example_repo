# fib
# max of list
# silnia
# sudoku

# sum of list

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
    suma_listy = 0
    for el in lista:
        suma_listy += el
    return suma_listy


print(zad1([]))
print(zad1([1]))
print(zad1([1, 2]))
print(zad1([1, 2, 3]))
# fib
# max of list
# silnia
# sudoku

# sum of list

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
    suma_listy = 0
    for el in lista:
        suma_listy += el
    return suma_listy


print(zad1([]))
print(zad1([1]))
print(zad1([1, 2]))
print(zad1([1, 2, 3]))
