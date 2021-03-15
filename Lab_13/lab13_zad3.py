#polecenie kończy się z metodami oraz parametrami
lista = []
class Smartphone:
    def __init__(self, firma, model, przekatna, ram, pojemnosc_baterii, kolor):
        self.firma = firma
        self.model = model
        self.przekatna = przekatna
        self.ram = ram
        self.pojemnosc_baterii = pojemnosc_baterii
        self.kolor = kolor

    def __repr__(self):
        return "Smartfon {} {}".format(self.firma, self.model)

    def opis(self):
        return "Smartfon marki {} o modelu {}. Przekatna ekranu to {} cali, a kolor to {}. Pojemnosc baterii to {} mAh, a " \
               "dostępna pamiec ram to {} GB".format(self.firma, self.model, self.przekatna, self.kolor,
                                                     self.pojemnosc_baterii, self.ram)

    def dodaj_do_listy(self):
        lista.append(self)

    def zadzwon(self, nr):
        print("Smartfon {} {} dzwoni na numer {}".format(self.firma, self.model, nr))


samsung_s9 = Smartphone("Samsung", "S9", 5.6, 8, 3600, "Czarny")
iphone_x = Smartphone("Apple", "X", 5.6, 4, 3500, "Biały")

samsung_s9.dodaj_do_listy()
iphone_x.dodaj_do_listy()
samsung_s9.opis()
iphone_x.zadzwon(123456789)

print(lista)