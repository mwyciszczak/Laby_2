from lab20_zad1 import palindrome


def test1():
    assert palindrome("abcd") == "dcba", "Powinno byc 'dcba'"  # prosty test


def test2():
    assert palindrome("ab cd") == "dc ba", "Powinno byc 'dc ba'"  # test ze spacją


def test3():
    assert isinstance(palindrome("123"), str), "Powinien być string"  # sprawdzenie czy to string


def test4():
    assert palindrome("1234") == "4321", "Powinno byc 4321"

