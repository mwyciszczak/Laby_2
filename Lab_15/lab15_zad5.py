"""         l. poj.	    l. mn.
Dopełniacz.	pokoju	pokoi/pokojów
obie formy są poprawne
"""
import random
import sqlite3


class Hotel:
    def __init__(self, pietra, pokoje_na_pietro):
        self.pietra = pietra
        self.pokoje_na_pietro = pokoje_na_pietro
        self.lista_pokoi = []
        self.tworz_pokoje()
        self.baza = sqlite3.connect("baza_zad5.db")
        self.tworz_tabele()
        self.uaktualnij_dane_programu()

    def __del__(self):
        self.baza.close()

    def tworz_tabele(self):
        try:
            self.baza.execute("""CREATE TABLE Pokoje
            (NR_POKOJU INT PRIMARY KEY,
            PIETRO INT,
            IMIE_LOKATOR,
            NAZWISKO_LOKATOR)
            """)
            print("Utworzono tabelę pokojów w bazie danych 'Pokoje'")
        except:
            print("Baza danych już istnieje")

    def uaktualnij_dane_programu(self):
        cursor = self.baza.execute("SELECT NR_POKOJU, PIETRO, IMIE_LOKATOR, NAZWISKO_LOKATOR from Pokoje")
        indeks = 0
        for x in cursor:
            for y in self.lista_pokoi:
                if y.nr_pokoju == x[0]:
                    y.pietro = x[1]
                    y.zajety = True
                    y.lokator = Osoba(x[2], x[3])

    def tworz_pokoje(self):#tworzy pokoje i dodaje do listy
        pietro = 1
        pokoj = 1
        for x in range(self.pietra):
            for y in range(self.pokoje_na_pietro):
                self.lista_pokoi.append(Pokoj(pokoj, pietro))
                pokoj += 1
            pietro += 1

    def czy_wolny_pokoj(self):#podaje czy jest dostępny choć jeden pokój
        for x in self.lista_pokoi:
            if not x.zajety:
                print("Jest dostępny co najmniej jeden pokój.")
                break

    def ile_wolnych(self):#podaje ile jest wolnych pokoi
        counter = 0
        for x in self.lista_pokoi:
            if not x.zajety:
                counter += 1
        print("Jest dostępnych {} wolnych pokoi.".format(counter))

    def wynajmij_dowolny(self, osoba):#wynajmuje losowy pokoj; osoba ma być obiektem Osoba
        while True:
            pok = random.choice(self.lista_pokoi)
            if not pok.zajety:
                pok.zajety = True
                pok.lokator = osoba
                print("Wynajęto pokój nr {} osobie {} {}.".format(pok.nr_pokoju, osoba.imie, osoba.nazwisko))
                break
        self.baza.execute("INSERT INTO Pokoje(NR_POKOJU, PIETRO, IMIE_LOKATOR, NAZWISKO_LOKATOR) VALUES('{}','{}','{}','{}')".format(pok.nr_pokoju, pok.pietro, pok.lokator.imie, pok.lokator.nazwisko))
        self.baza.commit()

    def wynajmij_pokoj(self, nr, pietro, osoba):#wynajmuje podany pokoj; osoba ma być obiektem Osoba
        wyn = False
        for x in self.lista_pokoi:
            if x.nr_pokoju == nr and not x.zajety:
                x.zajety = True
                x.lokator = osoba
                wyn = True
                print("Wynajęto pokój nr {} osobie {} {}.".format(nr, osoba.imie, osoba.nazwisko))
                break
        if not wyn:
            print("Pokoj jest już zajęty.")
        self.baza.execute(
            "INSERT INTO Pokoje(NR_POKOJU, PIETRO, IMIE_LOKATOR, NAZWISKO_LOKATOR) VALUES('{}','{}','{}','{}')".format(
                nr, pietro, osoba.imie, osoba.nazwisko))
        self.baza.commit()

    def czy_wynajmuje(self, osoba):#wypisuje pokoje wynajmowane przez osobę; osoba ma być obiektem Osoba
        print("Osoba {} {} zajmuje pokoje:".format(osoba.imie, osoba.nazwisko))
        for x in self.lista_pokoi:
            try:
                if x.lokator.imie == osoba.imie and x.lokator.nazwisko == osoba.nazwisko:
                    print("Pokój nr {}".format(x.nr_pokoju))
            except:
                pass

    def zwolnij_pokoje(self, osoba):#zwalnia wszystkie pokoje osoby; osoba ma być obiektem Osoba
        for x in self.lista_pokoi:
            try:
                if x.lokator.imie == osoba.imie and x.lokator.nazwisko == osoba.nazwisko:
                    x.lokator = None
                    x.zajety = False
                    print("Zwolnionio pokój nr {}".format(x.nr_pokoju))
                    self.baza.execute("DELETE FROM Pokoje WHERE NR_POKOJU LIKE '{}'".format(x.nr_pokoju))
            except:
                pass
        self.baza.commit()

    def zwolnij_pokoj(self, nr, osoba):#zwalnia podany pokój należący do osoby; osoba ma być obiektem Osoba
        for x in self.lista_pokoi:
            try:
                if x.lokator.imie == osoba.imie and x.lokator.nazwisko == osoba.nazwisko and x.nr_pokoju == nr:
                    x.lokator = None
                    x.zajety = False
                    print("Zwolnionio pokój nr {}".format(x.nr_pokoju))
            except:
                pass
        self.baza.execute("DELETE FROM Pokoje WHERE NR_POKOJU LIKE '{}'".format(nr))
        self.baza.commit()

    def trzy_pokoje(self):#sprawdza czy da się wynająć trzy pokoje obok siebie, jeśli tak przekazuje numer pierwszego
        counter = 0
        temp = []
        trzy = False
        for x in self.lista_pokoi:
            if not x.zajety:
                counter += 1
                temp.append(x)
            elif x.zajety:
                counter = 0
                temp.clear()
            if counter == 3:
                print("Można wynająć trzy pokoje obok siebie, numer pierwszego z nich to {}".format(temp[0].nr_pokoju))
                trzy = True
                break
        if not trzy:
            print("Nie da się wynająć trzech pokoi obok siebie.")


class Pokoj:
    def __init__(self, nr_pokoju, pietro):#numer pokoju i piętro musi być intigerem
        self.nr_pokoju = nr_pokoju
        self.pietro = pietro
        self.zajety = False#ułatwia sprawdzanie zajętych pokoi
        self.lokator = None

    def __repr__(self):
        if self.zajety:
            return "Pokoj nr {} na pietrze {} zajęty przez {} {}".format(self.nr_pokoju, self.pietro,
                                                                         self.lokator.imie, self.lokator.nazwisko)
        else:
            return "Pokój nr {} na pietrze {}, wolny".format(self.nr_pokoju, self.pietro)


class Osoba:
    def __init__(self, imie, nazwisko):#przyjmuje imie i nazwisko jako string
        self.imie = imie
        self.nazwisko = nazwisko

    def __repr__(self):
        return "Osoba {} {}".format(self.imie, self.nazwisko)


h1 = Hotel(4, 5)
o1 = Osoba("Maciej", "Wyciszczak")










