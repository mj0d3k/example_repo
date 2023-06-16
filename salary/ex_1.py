import csv

class Pracownik:
    def __init__(self, imie, nazwisko, wynagrodzenie_brutto):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wynagrodzenie_brutto = float(wynagrodzenie_brutto)

    def __str__(self):
        return f"{self.imie} {self.nazwisko}:"

    @property
    def placa_netto(self):
        skladka_emerytalna = self.wynagrodzenie_brutto * 0.0976
        skladka_rentowa = self.wynagrodzenie_brutto * 0.015
        skladka_chorobowa = self.wynagrodzenie_brutto * 0.0245
        skladka_zdrowotna = self.wynagrodzenie_brutto * 0.09
        skladki = skladka_emerytalna + skladka_rentowa + skladka_chorobowa + skladka_zdrowotna
        return self.wynagrodzenie_brutto - skladki

    @property
    def koszty_pracodawcy(self):
        skladka_emerytalna = self.wynagrodzenie_brutto * 0.0976
        skladka_rentowa = self.wynagrodzenie_brutto * 0.065
        skladka_wypadkowa = self.wynagrodzenie_brutto * 0.0167
        skladka_fgsp = self.wynagrodzenie_brutto * 0.0245
        skladka_fundusz_pracy = self.wynagrodzenie_brutto * 0.010
        skladki = skladka_emerytalna + skladka_rentowa + skladka_wypadkowa + skladka_fgsp + skladka_fundusz_pracy
        return self.wynagrodzenie_brutto + skladki


pracownicy = []
with open('salary.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        pracownicy.append(Pracownik(row[0], row[1], row[2]))

pracownicy_koszty = 0
for pracownik in pracownicy:
    print(f"Pracownik - {pracownik.imie} {pracownik.nazwisko}:")
    print(f"- pensja brutto: {pracownik.wynagrodzenie_brutto}")
    print(f"- pensja netto: {pracownik.placa_netto}")
    koszty_pracodawcy = pracownik.koszty_pracodawcy
    print(f"- koszty pracodawcy: {koszty_pracodawcy}")
    suma_kosztow = pracownik.wynagrodzenie_brutto + koszty_pracodawcy
    print(f"- koszt całkowity: {suma_kosztow}")
    pracownicy_koszty += suma_kosztow
    print()

print(f"Suma kosztów wynosi: {pracownicy_koszty}")
