# klasy
class Trojkat:
    def __init__(self, a, b, c, h_a):
        self.bok_a = a  # te a nie muszą być takie same, mogłoby być self.bok_a = a
        self.b = b
        self.c = c
        self.h_a = h_a
        # self.obwod = a + b + c # tego nie musi być, albo to albo definiujemy funkcję w klasie
        # self.pole = a*h_a/2

    def obwod(self):
        return self.bok_a + self.b + self.c

    def pole(self):
        return (self.bok_a * self.h_a) / 2


class Trapez:
    def __init__(self, a, b, c, d, h):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.h = h
        # self.obwod = a + b + c + d
        # self.pole = (a+b)*h/2

    def obwod(self):
        return self.a + self.b + self.c + self.d

    def pole(self):
        return (self.a + self.b) * self.h / 2


class Student:
    def __init__(self, imie, nazwisko, nr_indeksu):
        self.imie = imie
        self.nazwisko = nazwisko
        self.nr_indeksu = nr_indeksu
        self.oceny = []

    def __str__(self): # funkcja ma zwrócić naszego stringa
        # return self.imie + " " + self.nazwisko - opcja poprawna acz brzydka
        return f"{self.imie} {self.nazwisko} {self.nr_indeksu}"

    def __int__(self):
        return 5

    def dodaj_ocene(self, ocena):
        self.oceny.append(ocena)

    def zwroc_srednia(self):
        return sum(self.oceny) / len(self.oceny)


class Ladowarka(): #do samochodu elektrycznego
    def __init__(self, miasto, ulica, moc, liczba_zlacz, wartosc, producent, operator, model):
        self.a = miasto
        self.b = ulica
        self.c = moc
        self.d = liczba_zlacz
        self.e = wartosc
        self.f = producent
        self.g = operator
        self.h = model
    def __str__(self):
        return f"{self.h} {'|'} {self.f} {'|'} {self.g} {'|'} {self.a} {'|'} {self.b}"

    def cena_ladowania(self): #ile będzie kosztowała godzina ładowania
        if self.c > 100:
            return 60 * 1.87
        else:
            return 60 * 1.18

    def ubezpieczenie(self): #jaką kwotą operator zobowiązany jest pokryć ubezpieczenie ładowarki
        if self.e >= 100000:
            return 0.10 * self.e
        else:
            return 0.05 * self.e

    def ile_samochodow(self): #ile samochodów może jednocześnie ładować się na jednej stacji
        if self.c > 50 and self.c <= 100:
            return self.d * 1
        elif self.c > 100:
            if self.d % 2 == 0:
                return self.d / 2 + 1
            elif self.d % 2 != 0:
                return self.d - 1
        else:
            return 1

moja_ladowarka_1 = Ladowarka("Poznan", "Niepodleglosci", 150, 5, 150000, "Sigma", "PowerDot", "Ekoenergetka Axon Easy")
moja_ladowarka_2 = Ladowarka("Warszawa", "Horyzonalna", 60, 3, 40000, "Alfen", "Greenway", "Alfen Eve Double Pro-line")

print(moja_ladowarka_1)
print(moja_ladowarka_2)
print(moja_ladowarka_1.cena_ladowania())
print(moja_ladowarka_2.cena_ladowania())
print(moja_ladowarka_1.ubezpieczenie())
print(moja_ladowarka_2.ubezpieczenie())
print(moja_ladowarka_1.ile_samochodow())
print(moja_ladowarka_2.ile_samochodow())


# printy do poprzednich zadań

# student_ania = Student('Ania', 'Oleksy', 121174)
# student_ania.dodaj_ocene(3)
# print(student_ania)
# print(int(student_ania))
# print(student_ania.oceny)
# print(student_ania.zwroc_srednia())

# moj_trapez = Trapez(10, 8, 6, 5, 6)
# print(moj_trapez)
# print(moj_trapez.h)
# print(moj_trapez.pole())
# print(moj_trapez.obwod())

# trojkat_rownoboczny = Trojkat(10, 10, 10, 8)
# trojkat_ania = Trojkat(10, 8, 8, 6)

# print(trojkat_rownoboczny)
# print(trojkat_rownoboczny.bok_a)
# print(trojkat_rownoboczny.obwod())
# print(trojkat_ania.pole())
# print(trojkat_ania.pole) bez dwóch dodatkowych nawiasów wywołuje pole z klasy, tj. self.pole
def hello(a: str) -> str:
    # TODO
    return "Hello"


print("Example")
print(hello("Ola"))

assert hello("Ola") == "Hello Ola"
assert hello("Zuzia") == "Hello Zuzia"

print("Zadanie zrobione")
