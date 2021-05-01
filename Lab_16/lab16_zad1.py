import sqlite3


class Baza:
    def __init__(self):
        self.baza = sqlite3.connect("kontakty.db")
        self.tworz_baze()
        self.lista_osob = []
        self.aktualizuj_program()

    def __del__(self):
        self.baza.close()

    def tworz_baze(self):
        try:
            self.baza.execute("""CREATE TABLE kontakty(
                            imie TEXT,
                            nazwisko TEXT,
                            numer TEXT
                            )""")
        except:
            print("Baza danych już istnieje.")

    def aktualizuj_program(self):#zapełnia listę kontaktami z bazy danych
        cur = self.baza.execute("SELECT * from kontakty")#ID, imie, nazwisko, numer
        for x in cur:
            temp = Osoba(x[0], x[1], x[2])
            self.lista_osob.append(temp)

    def dodaj_osobe(self, osoba):#dodaje osobę, argument obiekt Osoba
        self.baza.execute("INSERT INTO kontakty(imie, nazwisko, numer) VALUES('{}','{}','{}')".format(osoba.imie, osoba.nazwisko, osoba.numer))
        self.baza.commit()
        self.lista_osob.append(osoba)

    def usun_osobe(self, osoba):#usuwa osobę, argumentem jest obiekt Osoba
        for x in self.lista_osob:
            if x.imie == osoba.imie and x.nazwisko == osoba.nazwisko and x.numer == osoba.numer:
                self.baza.execute("DELETE FROM kontakty WHERE imie = '{}' AND nazwisko = '{}' AND numer = '{}'".format(osoba.imie, osoba.nazwisko, osoba.numer))
                self.baza.commit()
        self.lista_osob = [x for x in self.lista_osob if x.imie != osoba.imie and x.nazwisko != osoba.nazwisko and x.numer != osoba.numer]

    def numery(self):#printuje wszystkie kontakty
        for x in self.lista_osob:
            print("{} {}; Tel:{}".format(x.imie, x.nazwisko, x.numer))

    def wyszukaj(self, numer):#wyszukuje po numerze telefonu w formacie "xxxxxxxxx"
        for x in self.lista_osob:
            if x.numer == numer:
                print("Podany numer należy do {} {}".format(x.imie, x.nazwisko))

    def sortowanie(self):#dodana metoda, printuje alfabetycznie kontakty
        templist = sorted(self.lista_osob, key=lambda Osoba: Osoba.nazwisko)
        for x in templist:
            print("{} {}; Tel:{}".format(x.nazwisko, x.imie, x.numer))


class Osoba:
    def __init__(self, imie, nazwisko, numer):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer = numer

    def __repr__(self):
        return "{} {} numer tel:{}".format(self.imie, self.nazwisko, self.numer)


b1 = Baza()
o1 = Osoba("Maciej", "Wyciszczak", "505545124")
o2 = Osoba("Jan", "Paweł", "123456789")
o3 = Osoba("Rostyslav", "Zhytkomlinov", "333333333")
o4 = Osoba("Lech", "Walesa", "567901328")

"""b1.dodaj_osobe(o1)
b1.dodaj_osobe(o2)
b1.dodaj_osobe(o3)
b1.dodaj_osobe(o4)"""






