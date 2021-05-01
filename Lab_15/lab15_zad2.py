class Browar:
    piwa = []

    def sortuj_ocena(self):
        return sorted(self.piwa, key=lambda Beer: Beer.opinia)

    def sortuj_nazwa(self):
        return sorted(self.piwa, key=lambda Beer: Beer.nazwa)


class Beer:
    def __init__(self, nazwa, alc, cena, opinia):
        self.nazwa = nazwa
        self.alc = alc
        self.cena = cena
        self.opinia = opinia

    def __repr__(self):
        return "Styl to {}, alkohol {}%, cena to {}zł , ocena to {}/5".format(self.nazwa, self.alc, self.cena, self.opinia)


browar = Browar()

for x in range(3):
    ocena = float(input("podaj ocene"))
    nnazwa = input("podaj nazwe")
    browar.piwa.append(Beer(nnazwa, 3.5, 3.99, ocena))

print(browar.piwa)
print(browar.sortuj_ocena())
print(browar.sortuj_nazwa())