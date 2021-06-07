#  Zadanie 1 Lab 18
inwokacja = open("pantadeusz.txt", 'r', encoding="utf8")  # kodowanie utf8 potrzebne do polskich znaków

print(inwokacja)  # obiekt

for line in inwokacja.readlines():
    print(line.rstrip())  # usuwam enter z pliku txt, enter w outpucie pochodzi z printa

