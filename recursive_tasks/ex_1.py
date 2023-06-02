"""
SUMA Z LISTY
pseudokod:
jezeli lista jest pusta
to 0
jesli nie jest pusta (else)
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


"""
MAX Z LISTY
pseudokod:
jeżeli lista jest pusta zwróć None
jeżeli lista zawiera tylko jeden element zwróć ten element
else
pierwszy_element to pierwszy index listy [0]
reszta_listy będzie oznaczona jako = lista[1:]
max reszty znaleźć przez funkcję z reszty_listy
jeżeli pierwszy_element > max_reszty -> zwróć pierwszy_element
else -> zwróć max_reszty
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


print(10 * '-')
print(zad2([]))
print(zad2([1]))
print(zad2([1, 2]))
print(zad2([1, 2, 3]))


"""
SILNIA
pseudokod:
jeżeli n równa się 0 zwróć 1
else -> n * funkcja(n-1) = zwróć wynik
"""

def zad3(n):
    if n == 0:
        return 1
    else:
        wynik = n * zad3(n - 1)
        return wynik


print(10 * '-')
print(zad3(1))
print(zad3(3))
print(zad3(10))


"""
CIĄG FIBONACCIEGO
pseudokod:
jeżeli n równa się 0 zwróć 0
jeżeli n równa się 1 zwróć 1
else -> funkcja(n-1) + funkcja(n-2) 
zwróć wynik
"""

def zad4(n):
    if n < 0:
        return None
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return zad4(n - 1) + zad4(n - 2)


print(10 * '-')
print(zad4(-10))
print(zad4(0))
print(zad4(10))


"""
SUDOKU
pseudokod:

"""