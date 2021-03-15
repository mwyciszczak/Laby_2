import math


class Figura():
    def wypisz(self):
        print(f"Jestem {self.nazwa()}. Moj obwod: {self.obwod()}, a pole: {self.pole()}.")

    def nazwa(self):
        pass

    def obwod(self):
        pass

    def pole(self):
        pass


class Trojkat(Figura):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def nazwa(self):
        return "trójkąt"

    def obwod(self):
        return self.a + self.b + self.c

    def pole(self):
        p = self.obwod()/2
        return math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))


class Kolo(Figura):
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def nazwa(self):
        return "koło"

    def obwod(self):
        return 2 * math.pi * self.r

    def pole(self):
        return math.pi * self.r ** 2


class Kwadrat(Figura):
    def __init__(self, a):
        self.a = a

    def nazwa(self):
        return "kwadrat"

    def obwod(self):
        return 4 * self.a

    def pole(self):
        return self.a ** 2


class Prostokat(Kwadrat):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b

    def nazwa(self):
        return "prostokąt"

    def obwod(self):
        return 2 * (self.a + self.b)

    def pole(self):
        return self.a * self.b


p1 = Prostokat(10, 3)
print(p1.obwod())