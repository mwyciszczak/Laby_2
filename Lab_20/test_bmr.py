from lab20_zad2 import bmr


def test1():
    assert 1800 <= bmr(22, 189, 70, "m") <= 1900, "Powinno być pomiędzy 1800 a 1900"


def test2():
    assert 1400 <= bmr(34, 165, 65, "k") <= 1500, "Powinno być pomiędzy 1400 a 1500"


def test3():
    assert isinstance(bmr(34, 165, 65, "k"), int) or isinstance(bmr(34, 165, 65, "k"), float), "Powinien być int lub float"


def test4():
    assert bmr("abc", 165, 65, "k"), "Powinno być pomiędzy 1400 a 1500"