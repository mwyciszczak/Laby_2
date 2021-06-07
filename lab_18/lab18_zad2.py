inwokacja = open("pantadeusz.txt", 'r', encoding="utf8")

for i, x in enumerate(inwokacja.readlines()):
    if i == 7:
        print(x.rstrip())
    elif i == 11:
        print(x.rstrip())
    elif i == 59:
        print(x.rstrip())
    elif i == 97:
        print(x.rstrip())
    elif i == 103:
        print(x.rstrip())
