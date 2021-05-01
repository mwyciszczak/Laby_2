import random
fig = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Walet", "Dama", "Król", "As"]


class Talia:
    talia = []
    kosz = []

    def utworz_talie(self):
        for x in fig:
            self.talia.append(Karta("Kier", x))
        for x in fig:
            self.talia.append(Karta("Karo", x))
        for x in fig:
            self.talia.append(Karta("Pik", x))
        for x in fig:
            self.talia.append(Karta("Trefl", x))

    def usun_karte(self, kolor, figura):
        z = [x for x in self.talia if x.kolor == kolor and x.figura == figura]
        zz = set(z)
        t = set(self.talia)
        self.talia = list(t.difference(zz))

    def porownaj_figure(self, kar1, kar2):#przyjmuje obiekt Karta
        counter1 = 0
        counter2 = 0
        k1 = kar1
        k2 = kar2
        fig1 = k1.figura
        fig2 = k2.figura

        for x in fig:
            counter1 += 1
            if x == fig1:
                break
        for y in fig:
            counter2 += 1
            if y == fig2:
                break

        if counter1 > counter2:
            print("Karta pierwsza {} jest większa od karty drugiej {} ".format(k1, k2))
            return 1
        elif counter1 < counter2:
            print("Karta pierwsza {} jest mniejsza od karty drugiej {} ".format(k1, k2))
            return 2
        else:
            print("Karty są takie same {} {}".format(k1, k2))
            return 3

    def sortuj_kolor(self):
        print(sorted(self.talia, key=lambda Karta: Karta.kolor))

    def sortuj_figura(self):
        print(sorted(self.talia, key=lambda Karta: Karta.figura))

    def wyswietl_karte(self, kolor, figura):
        for x in self.talia:
            if x.kolor == kolor and x.figura == figura:
                print("Karta o kolorze {} i symbolu {} jest w talii".format(x.kolor, x.figura))

    def dodaj(self, kolor, figura):
        w_talii = False
        for x in self.talia:
            if x.kolor == kolor and x.figura == figura:
                print("Ta karta już jest w talii")
                w_talii = True
        if not w_talii:
            self.talia.append(Karta(kolor, figura))

    def przenies(self, kolor, figura):
        for x in self.talia:
            if x.kolor == kolor and x.figura == figura:
                print("Karta została przeniesiona do kosza")
                self.usun_karte(kolor, figura)
                self.kosz.append(Karta(kolor, figura))


class Karta:
    def __init__(self, kolor, figura):
        self.kolor = kolor
        self.figura = figura

    def __repr__(self):
        return "{} {}".format(self.figura, self.kolor)


talia1 = Talia()
talia1.utworz_talie()

talia2 = Talia()

# Moja implementacja wojny działa, lecz nie emuluje remisu w dokładny sposób i prawdopodobnie to jest
# powodem dlaczego gra nie kończy się nawet w milionach ruchów
"""def wojna(t1, t2):
    while len(t1.talia) > 0 or len(t2.talia) > 0:
        k1 = random.choice(t1.talia)
        k2 = random.choice(t2.talia)
        wynik = t1.porownaj_figure(k1, k2)
        if wynik == 1:
            t2.talia.remove(k2)
            t1.talia.append(k2)
        elif wynik == 2:
            t1.talia.remove(k1)
            t2.talia.append(k1)
        else:
            print("remis")"""


"""print(len(talia1.talia), len(talia2.talia))
wojna(talia1, talia2)
print(len(talia1.talia), len(talia2.talia))"""