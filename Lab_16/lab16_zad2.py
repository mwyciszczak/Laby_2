import sqlite3


class Baza:
    def __init__(self):
        self.baza = sqlite3.connect("pracownicy.db")
        self.pracownicy = []
        self.glob_id = 0
        self.tworz_tabele()
        self.uaktualnij()

    """def __del__(self):
        print("Usunięto bazę danych")"""

    def uaktualnij(self):
        cursor = self.baza.execute("SELECT id_pracownika, imie, nazwisko, miejscowosc, zarobki FROM Pracownicy")
        for x in cursor:
            self.pracownicy.append(Pracownik(x[0], x[1], x[2], x[3], int(x[4]),))
            if x[0] > self.glob_id:
                self.glob_id = x[0]
        self.glob_id += 1

    def tworz_tabele(self):
        try:
            self.baza.execute("""CREATE TABLE Pracownicy
                        (id_pracownika INT PRIMARY KEY,
                        imie TEXT NOT NULL,
                        nazwisko TEXT NOT NULL,
                        miejscowosc TEXT NOT NULL,
                        zarobki TEXT NOT NULL)
                        """)
        except:
            print("Tabela już istnieje")

    def dodaj_pracownika(self, imie, nazwisko, miejscowosc, zarobki):
        idd = self.glob_id
        self.glob_id += 1
        self.pracownicy.append(Pracownik(idd, imie, nazwisko, miejscowosc, zarobki))
        self.baza.execute("INSERT INTO Pracownicy(id_pracownika, imie, nazwisko, miejscowosc, zarobki) VALUES('{}','{}','{}','{}','{}')".format(idd, imie, nazwisko, miejscowosc, zarobki))
        self.baza.commit()

    def usun_pracownika(self, idd_pracownika):
        self.baza.execute("DELETE FROM Pracownicy WHERE id_pracownika LIKE '{}'".format(idd_pracownika))
        self.baza.commit()
        for x in self.pracownicy:
            if x.id_pracownika == idd_pracownika:
                self.pracownicy = [x for x in self.pracownicy if x.id_pracownika != idd_pracownika]

    def wyswietl_posortowane(self):
        sortowana_lista = sorted(self.pracownicy, key=lambda Pracownik: Pracownik.imie)
        for x in sortowana_lista:
            print("{} {} z miasta {}, zarabia {} zł".format(x.imie, x.nazwisko, x.miejscowosc, x.zarobki))

    def uaktualnij_dane(self, idd, imie, nazwisko, miejscowosc, zarobki):
        for x in self.pracownicy:
            if x.id_pracownika == idd:
                x.imie = imie
                x.nazwisko = nazwisko
                x.miejscowosc = miejscowosc
                x.zarobki = zarobki
        self.baza.execute("UPDATE Pracownicy SET imie = '{}', nazwisko = '{}', miejscowosc = '{}', zarobki = '{}' WHERE id_pracownika = '{}'".format(imie, nazwisko, miejscowosc, zarobki, idd))
        self.baza.commit()

    def najwieksze_zarobki(self):
        sortowana_lista = sorted(self.pracownicy, key=lambda Pracownik: Pracownik.zarobki)
        print(sortowana_lista[-1])

    def najmniejsze_zarobki(self):
        sortowana_lista = sorted(self.pracownicy, key=lambda Pracownik: Pracownik.zarobki)
        print(sortowana_lista[0])


class Pracownik:
    def __init__(self, id_pracownika, imie, nazwisko, miejscowosc, zarobki):
        self.id_pracownika = id_pracownika
        self.imie = imie
        self.nazwisko = nazwisko
        self.miejscowosc = miejscowosc
        self.zarobki = zarobki

    def __repr__(self):
        return "Pracownik {} {}, z miejscowosci {}, zarabia {} zł".format(self.imie, self.nazwisko, self.miejscowosc, self.zarobki)

    """def __del__(self):
        print("Pracownik {} {} został usunięty".format(self.imie, self.nazwisko))"""


b1 = Baza()

"""b1.dodaj_pracownika("Jan", "Kowalski", "Wadowice", 213)
b1.dodaj_pracownika("Piotr", "Nowak", "Stocznia", 420)
b1.dodaj_pracownika("Piotr", "Kozioł", "Katowice", 2000)
b1.dodaj_pracownika("Marcin", "Jagoda", "Ściernisko", 300)"""

"""for x in range(len(b1.pracownicy)):
    b1.usun_pracownika(x+1)"""

b1.najmniejsze_zarobki()