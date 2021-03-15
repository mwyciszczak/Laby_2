lista_studentow = []


class Student:
    def __init__(self, imie, nazwisko, indeks, wiek, kierunek, semestr, forma, ostatnia_srednia):
        self.imie = imie
        self.nazwisko = nazwisko
        self.indeks = indeks
        self.wiek = wiek
        self.kierunek = kierunek
        self.semestr = semestr
        self.forma = forma
        self.ostatnia_srednia = ostatnia_srednia

    def __repr__(self):
        return "Student {} {} indeks: {}".format(self.imie, self.nazwisko, self.indeks)

    def dodaj_do_listy(self):
        lista_studentow.append(self)

    def zmien_srednia(self, nowa_srednia):
        self.ostatnia_srednia = nowa_srednia


s1 = Student("Jan", "Kowalski", 42152, 20, "Informatyka", 2, "Stacjonarne", 4.4)

print(s1)
s1.dodaj_do_listy()
print(lista_studentow)
print(s1.ostatnia_srednia)
s1.zmien_srednia(4.8)
print(s1.ostatnia_srednia)
