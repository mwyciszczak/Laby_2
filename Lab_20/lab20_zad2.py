def bmr(wiek, wzrost, waga, plec):
    while True:
        try:
            wiek = int(wiek)
            break
        except ValueError:
            print("Podaj prawidłowy wiek")
            wiek = input()

    while True:
        try:
            wzrost = int(wzrost)
            break
        except ValueError:
            print("Podaj prawidłowy wzrost w cm")
            wzrost = input()

    while True:
        try:
            waga = float(waga)
            break
        except ValueError:
            print("Podaj prawidlowa wage")
            waga = input()

    while True:
        if plec == "k" or plec == "m":
            break
        else:
            print("Podaj plec litera (k) lub (m)")
            plec = input()

    if plec == "m":
        wynik = 66.47 + (13.7 * waga) + (5 * wzrost) - (6.76 * wiek)
        return wynik

    elif plec == "k":
        wynik = 655.1 + (9.567 * waga) + (1.85 * wzrost) - (4.68 * wiek)
        return wynik

    else:
        print("Nie działa")


print(bmr("a", 165, 65, "k"))

