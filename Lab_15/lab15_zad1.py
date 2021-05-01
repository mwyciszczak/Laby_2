import random


class Restaurant:
    def __init__(self, adress, hours, name):
        self.adress = adress
        self.hours = hours
        self.name = name

    def information(self):
        print("Punkt gastronomiczny {}.".format(self.name))
        print("{}, {}".format(self.adress, self.hours))

    def show_flavours(self):
        pass

    def ice_cream_lottery(self):
        pass

    def pick_icecream(self):
        pass

    def show_coffee(self):
        pass

    def order_coffee(self, ctype, size):
        pass


class IceCreamStand(Restaurant):
    flavours_scoop = ["Wanilia", "Czekolada", "Pistacja", "Guma Balonowa", "Śmietana"]
    flavours_italiano = ["Śmietana", "Czekolada", "Mix"]
    form = ["Wafelek", "Kubek"]
    size_italiano = ["Duży", "Średni", "Mały"]
    max_scoop = 5

    def __init__(self, adress, hours, name):
        super().__init__(adress, hours, name)

    def show_flavours(self):
        print("Dostępne smaki lodów w gałce to:")
        for x in self.flavours_scoop:
            print("-", x)
        print("Dostępne smaki lodów włoskich to:")
        for x in self.flavours_italiano:
            print("-", x)

    def ice_cream_lottery(self):
        print("Zdecydowałeś się na losowego loda za pół ceny.")
        ictype = random.randint(0, 1)
        if ictype == 0:
            flavour = random.choice(self.flavours_scoop)
            scoop_count = random.randint(1, 5)
            form = random.choice(self.form)
            print("Wylosowano loda w gałce. Ilość gałek to {}, a smak to {}. Loda dostaniesz w {}".format(scoop_count, flavour, form))
        elif ictype == 1:
            flavour = random.choice(self.flavours_italiano)
            size = random.choice(self.size_italiano)
            print("Wylosowano loda włoskiego. Rozmiar to {}, a smak to {}".format(size, flavour))


class CoffeeShop(Restaurant):
    coffee = ["Latte", "Espresso", "Flat White"]
    sizes = ["Mała", "Średnia", "Duża"]

    def __init__(self, adress, hours, name):
        super().__init__(adress, hours, name)

    def show_coffee(self):
        print("Dostępne kawy to:")
        for x in self.coffee:
            print("- {}".format(x))

    def order_coffee(self, ctype, size):
        print("Zamówiono kawę {} w rozmiarze {}".format(self.coffee[ctype], self.sizes[size]))


ic1 = IceCreamStand("Partyzantów 12, Wrocław", "12:00-22:00", "Polskie Lody")
ic1.show_flavours()
ic1.information()
ic1.ice_cream_lottery()

c1 = CoffeeShop("Partyzantów 12, Wrocław", "8:00-22:00", "")
c1.show_coffee()
c1.order_coffee(1, 2)
