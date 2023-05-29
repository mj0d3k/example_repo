# brutto 3600
# netto 3000
# 600 zl po stornie pracownika
# 600 po stronie pracodawcy
# rozbic na wszytskie skladki po stronie pracodawcy i pracownika

import csv

with open('salary.csv') as my_file:
    my_reader = csv.reader(my_file)

class Pracownik:
    def __init__(self):
        self.imie= ""
        self.nazwisko = ""
        self.wynagrodzenie_brutto = ""

    def __str__(self):
        pass

    @classmethod
    def placa_netto(cls, file):
        pracownicy = []
        with open(file) as pracownicy_file:
            for row in csv.reader(pracownicy_file):
                pracownicy.append(
                    cls(row[0], row[1], row[2])
                )
        return pracownicy

print(Pracownik.placa_netto('salary.csv'))

    # def placa_netto(self):
    #     for pracownik in pracownicy:
    #         suma = self.wynagrodzenie_brutto # czy to jest potrzebne?
    #         return suma - self.wynagrodzenie_brutto * 0.0976 - self.wynagrodzenie_brutto * 0.015 - self.wynagrodzenie_brutto * 0.09 - self.wynagrodzenie_brutto * 0.0245

    # def oblicz_koszty_pracodawcy(self):
    #     for pracownik in pracownicy:
    #         suma = self.wynagrodzenie_brutto
    #         return suma + self.wynagrodzenie_brutto * 0.0976 + self.wynagrodzenie_brutto * 0.065 + self.wynagrodzenie_brutto * 0.0245 + self.wynagrodzenie_brutto * 0.067 + self.wynagrodzenie_brutto * 0.01



    # koszty_wszystkich_pracownikow = 0
    # for pracownik in pracownicy:
    #     print("Pracownik Kowalski: ")
    #     print("- pensja brutto: ")
    #     print("- pensja netto: ")
    #     print("- koszty pracodawcy: ")
    #     print("- koszt całkowity: ")
    #
    # print("Suma kosztów wynosi: ")