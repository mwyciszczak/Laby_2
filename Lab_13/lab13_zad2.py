lista_ksiazek = []

class Ksiazka:
    def __init__(self, autor, tytul):
        self.autor = autor
        self.tytul = tytul

    def __repr__(self):
        rep = 'Ksiazka(' + self.autor + ',' + str(self.tytul) + ')'
        return rep

    def dodaj_do_listy(self):
        lista_ksiazek.append(self)

    def sortowanie(self):
        return sorted(lista_ksiazek, key=lambda Ksiazka: Ksiazka.autor)

for x in range(4):
    autor = input("Podaj autora:")
    tytul = input("Podaj tytul:")
    Ksiazka(autor, tytul).dodaj_do_listy()

print(lista_ksiazek)
print(lista_ksiazek[0].sortowanie())
