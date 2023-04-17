def trojkat(bok_a, bok_b, bok_c, wysokosc_a):
    obwod = bok_a + bok_b + bok_c
    pole = (bok_a * wysokosc_a) / 2
    return obwod, pole
print(trojkat(10, 7, 6, 5))
assert trojkat(3, 4, 5, 6) == (12, 9)

def kwadrat(bok_a):
    obwod = 4*bok_a
    pole = bok_a**2
    return obwod, pole
print(kwadrat(10))
assert kwadrat(15) == (60, 225)

def prostokat(bok_a, bok_b):
    obwod = 2*bok_a + 2*bok_b
    pole = bok_a*bok_b
    return obwod, pole
print(prostokat(10,20))
assert prostokat(4, 10) == (28, 40)

def rownoleglobok(bok_a, bok_b, wysokosc_a):
    obwod=bok_a*2+bok_b*2
    pole=bok_a*wysokosc_a
    return obwod, pole

def romb(bok, wysokosc):
    obwod=bok*4
    pole=bok*wysokosc
    return obwod, pole

# trapez i kolo dla studenta 3
def trapez(bok_a, bok_b, bok_c, bok_d, wysokosc_a):
    obwod=bok_a+bok_b+bok_c+bok_d
    pole=(bok_a+bok_b)*wysokosc_a/2
    return obwod, pole


def kolo(promien):
    obwod = promien*2*π
    pole = π*promien**2
    return obwod, pole

# assert trojkat(10, 15, 16, 8) == (41, 40)
# assert trojkat(15, 8, 12, 6) == (29, 45)
# assert kwadrat(20) == (80, 400)
# assert kwadrat(10) == (40, 100)
# assert prostokat(12, 10) == (44, 120)
# assert prostokat(10, 20) == (40, 200)
# assert rownoleglobok(6, 5, 2) == (22, 12)
# assert rownoleglobok(6, 8, 3) == (28, 18)
# assert romb(10, 5) == (40, 50)
# assert romb(40, 10) == (160, 400)
# assert trapez(10, 15, 7, 14, 2) == (45, 25)
# assert trapez(2, 5, 6, 7, 5) == (20, 17.5)
# TODO na koniec! dopisz 2 testy dla kola i dla kazdej innej figury po jednym dodatkowym tescie

