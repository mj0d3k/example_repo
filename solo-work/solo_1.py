# zadanie 1.1

hello = "Hello"
student = "Ola"

# oczekiwany rezultat: Hello Ola
# wykorzystaj w princie zmienne hello i student
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
imiona = sorted(studenci, key=lambda x: x.split()[0])

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

# policz wszystkich studentow z tablicy, ktorych nazwisko zaczyna sie na N
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]

liczba_n = 0
for student in studenci:
    if student.split()[-1].startswith("N"):
        liczba_n += 1
print("Liczba studentow na N wynosi: ", liczba_n)


# zadanie 1.10