class Obywatel:
    def __init__(self, imie, nazwisko, ulica, nr_domu, kod_pocztowy, miejscowosc):
        self.imie = imie
        self.nazwisko = nazwisko
        self.ulica = ulica
        self.nr_domu = nr_domu
        self.kod_pocztowy = kod_pocztowy
        self.miejscowosc = miejscowosc

    def zapisz_do_pliku(self):
        wizytowka = """----------------------
{} {}
ul.{} {}
{} {}
----------------------\n""".format(self.imie, self.nazwisko, self.ulica, self.nr_domu, self.kod_pocztowy, self.miejscowosc)
        plik = open("wizytowki.txt", "a")
        plik.write(wizytowka)
        plik.close()

ob1 = Obywatel("Jan", "Kowalski", "Miodowa", "23", "51-342", "Wroclaw")
ob1.zapisz_do_pliku()