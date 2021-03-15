class Pojazd:
    def __init__(self, nr_tablica, marka):
        self.nr_tablica = nr_tablica
        self.marka = marka

    def __del__(self):
        print("Pojazd o nr_tablicy {} został usunięty".format(self.nr_tablica))

    def podaj_tablice(self):
        print("Tablica rejestracyjna tego pojazdu to {}".format(self.nr_tablica))


class Samochod(Pojazd):
    def __init__(self, nr_tablica, marka, kolor):
        super().__init__(nr_tablica, marka)
        self.kolor = kolor

    def brrr(self):
        print("Samochód marki {} o kolorze {} robi brrr".format(self.marka, self.kolor))


class Motocykl(Pojazd):
    def __init__(self, nr_tablica, marka, halas):
        super().__init__(nr_tablica, marka)
        self.halas = halas

    def wziuuum(self):
        print("Motocykl marki {} robi wziuuum z głośnością {} decybeli".format(self.marka, self.halas))


s1 = Samochod("DW 9GL48", "Mazda", "Szary")
m1 = Motocykl("DWR 86TY", "Honda", 95)
print(s1.marka, s1.nr_tablica, s1.kolor)
print(m1.marka, m1.nr_tablica, m1.halas)
s1.podaj_tablice()
s1.brrr()
m1.podaj_tablice()
m1.wziuuum()

def usuwanie(instancja):
    wybor = input("Czy usunąć samochód o nr tablic {}?(Tak-litera, Nie-Cyfra)".format(s1.nr_tablica))
    if wybor is str():
        del instancja

usuwanie(s1)
usuwanie(m1)
#nawet jeśli nie usuniemy funkcją usuwanie to i tak się usuną po końcu programu, stąd printy i tak się pojawią