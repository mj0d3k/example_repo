# zadanie 1.1

hello = "Hello"
student = "Ola"

print("Hello Kasia")
print("{} {}".format("Hello", "Ola"))

# zadanie 1.2

student = input("Wpisz swoje imie ")

print("Hello Ola")
print("Hello", student)

# zadanie 1.3

studenci = ["Ania", "Kuba", "Piotr", "Jan"]
liczba_studentow = len(studenci)
print("Liczba studentow wynosi: " + str(liczba_studentow))

# zadanie 1.4

studenci = ["Ania", "Kasia", "Piotr", "Tomek"]

print("Hello", studenci[0])
print("Hello", studenci[1])
print("Hello", studenci[2])
print("Hello", studenci[3])

# zadanie 1.5

liczba = 3
potega = 4

wynik = int(liczba)**int(potega)

print("Wynik wynosi:", str(wynik))

# zadanie 1.6

ciag_znakow = "edbw(hdakqas(skqskahb))adwndwb(wgwidn()dsqwhjdw)"
liczba_nawiasow_otwierajacych = ciag_znakow.count('(')

print("Liczba nawiasow otwierajacych wynosi: " + str(liczba_nawiasow_otwierajacych))

# zadanie 1.7

studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
imiona = sorted(studenci)

print("Alfabetyczna lista studentow wynosi: ")
for student in imiona:
    print(student)

# zadanie 1.8

studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
nazwiska = sorted(studenci, key=lambda x: x.split()[-1])

print("Alfabetyczna lista studentow wynosi: ")
for student in nazwiska:
    print(student)

# zadanie 1.9

studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]

liczba_n = 0
for student in studenci:
    if student.split()[-1].startswith("N"):
        liczba_n += 1
print("Liczba studentow na N wynosi: ", liczba_n)

# zadanie 1.10

wykres_1 = [[2, 4], [4, 4], [6, 4]]
wykres_2 = [[2, 3], [4, 4], [6, 5]]
wykres_3 = [[2, 3], [4, 3], [5, 4]]

def czy_funkcja_liniowa(punkty):
    x1, y1 = punkty[0]
    x2, y2 = punkty[1]
    for i in range(2, len(punkty)):
        x, y = punkty[i]
        if (x - x1) * (y2 - y1) != (y - y1) * (x2 - x1):
            return False
    return True

wykres_1_funkcja_liniowa = czy_funkcja_liniowa(wykres_1)
wykres_2_funkcja_liniowa = czy_funkcja_liniowa(wykres_2)
wykres_3_funkcja_liniowa = czy_funkcja_liniowa(wykres_3)

if wykres_1_funkcja_liniowa:
    print("Dla punktow w wykres_1 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_1 nie mozna wyznaczyc funkcji liniowej.")

if wykres_2_funkcja_liniowa:
    print("Dla punktow w wykres_2 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_2 nie mozna wyznaczyc funkcji liniowej.")

if wykres_3_funkcja_liniowa:
    print("Dla punktow w wykres_3 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_3 nie mozna wyznaczyc funkcji liniowej.")
