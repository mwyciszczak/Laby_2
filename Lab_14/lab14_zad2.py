import random

class Zwierze:
    pokarm_dla_kota = ["Karmę suchą", "Karmę Mokrą", "Mleko", "Trawę"]
    pokarm_dla_psa = ["Karmę suchą", "Karmę Mokrą", "Kość", "Trawę"]
    pokarm_dla_ptaka = ["Nasiona", "Owoce", "Robaki"]
    pokarm_dla_ryby = ["Plankton", "Glony", "Pokarm dla rybek", "Inne ryby"]

    def __init__(self, oczy, waga, obwod, predkosc, predkosc_max):#obwod w najszerszym miejscu
        self.oczy = oczy
        self.waga = waga
        self.obwod = obwod
        self.predkosc = predkosc
        self.predkosc_max = predkosc_max

    def jedz(self):
        pass

    def ruch(self, przyspieszenie):
        while self.predkosc < self.predkosc_max:
            self.predkosc = self.predkosc + przyspieszenie
            if self.predkosc > self.predkosc_max:
                self.predkosc = self.predkosc_max
            print("Zwierzę porusza się z prędkością {} km/h", self.predkosc)
        print("Zwierzę osiągnęło prędkość maksymalną")

    def spij(self):
        dlugosc_snu = random.randint(0, 12)
        if dlugosc_snu == 0:
            print("Zwierzę nie spało ")
        else:
            print("Zwierzę spało przez {} godzin".format(dlugosc_snu))


class Kot(Zwierze):
    def __init__(self, oczy, waga, obwod, predkosc, predkosc_max, nogi):
        super().__init__(oczy, waga, obwod, predkosc, predkosc_max)
        self.nogi = nogi

    def jedz(self):
        print("Kot je {}.".format(random.choice(Zwierze.pokarm_dla_kota)))


class Pies(Zwierze):
    def __init__(self, oczy, waga, obwod, predkosc, predkosc_max, nogi):
        super().__init__(oczy, waga, obwod, predkosc, predkosc_max)
        self.nogi = nogi

    def jedz(self):
        print("Pies je {}.".format(random.choice(Zwierze.pokarm_dla_psa)))


class Ptak(Zwierze):
    def __init__(self, oczy, waga, obwod, predkosc, predkosc_max, nogi, skrzydla):
        super().__init__(oczy, waga, obwod, predkosc, predkosc_max)
        self.nogi = nogi
        self.skrzydla = skrzydla

    def jedz(self):
        print("Ptak je {}.".format(random.choice(Zwierze.pokarm_dla_ptaka)))


class Ryba(Zwierze):
    def __init__(self, oczy, waga, obwod, predkosc, predkosc_max, pletwy):
        super().__init__(oczy, waga, obwod, predkosc, predkosc_max)
        self.pletwy = pletwy

    def jedz(self):
        print("Ryba je {}.".format(random.choice(Zwierze.pokarm_dla_ryby)))

k1 = Kot(2, 5, 40, 6, 40, 4)
k1.jedz()
k1.ruch(12)
k1.spij()
print(k1.oczy)