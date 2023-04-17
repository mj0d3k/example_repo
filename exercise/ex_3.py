def trojkat(bok_a, bok_b, bok_c, wysokosc_a):
    obwod = bok_a + bok_b + bok_c
    pole = (bok_a * wysokosc_a) / 2
    return obwod, pole

# kwadrat, prostokat dla studenta 1
def kwadrat(bok_a):
    obwod = 4*bok_a
    pole = bok_a**2
    return obwod, pole


def prostokat(bok_a, bok_b):
    obwod = 2*bok_a + 2*bok_b
    pole = bok_a*bok_b
    return obwod, pole

# rownoleglobok i romb dla studenta 2
def rownoleglobok(bok_a, bok_b, wysokosc_a):
    # TODO
    obwod=bok_a*2+bok_b*2
    pole=bok_a*wysokosc_a
    return obwod, pole
print(rownoleglobok(7, 10, 4))
assert rownoleglobok(6, 8, 3) == (28, 18)

def romb(bok, wysokosc):
    # TODO
    obwod=bok*4
    pole=bok*wysokosc
    return obwod, pole
print (romb(50,10))
assert romb(40, 10) == (160, 400)

# trapez i kolo dla studenta 3
def trapez(bok_a, bok_b, bok_c, bok_d, wysokosc_a):
    # TODO
    obwod=bok_a+bok_b+bok_c+bok_d
    pole=(bok_a+bok_b)*wysokosc_a/2
    return obwod, pole
print(trapez(2, 5, 6, 7, 5))
assert trapez(2, 5, 6, 7, 5) == (20, 17.5)

#def kolo(promien):
 #   obwod = promien*2*π
  #  pole = π*promien**2
   # return obwod, pole


# assert trojkat(10, 15, 16, 8) == (41, 40)
# assert kwadrat(20) == (80, 400)
# assert prostokat(12, 10) == (44, 120)
# assert rownoleglobok(6, 5, 2) == (22, 12)
# assert rownoleglobok(6, 8, 3) == (28, 18)
# assert romb(10, 5) == (40, 50)
# assert romb(40, 10) == (160, 400)
# assert trapez(10, 15, 7, 14, 2) == (45, 25)
# assert trapez(2, 5, 6, 7, 5) == (20, 17.5)
# TODO na koniec! dopisz 2 testy dla kola i dla kazdej innej figury po jednym dodatkowym tescie

