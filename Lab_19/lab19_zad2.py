try:
    a1 = open("tad.txt", "r", encoding="utf8")
except FileNotFoundError:
    name = input("Podaj nazwe pliku")
    a1 = open("{}".format(name), "r", encoding="utf8")
try:
    a2 = open("dziady.txt", "r", encoding="utf8")
except FileNotFoundError:
    name = input("Podaj nazwe pliku")
    a2 = open("{}".format(name), "r", encoding="utf8")

a1_list = []
a2_list = []

for line in a1.readlines():
    a1_list.append(line.rstrip())

for line in a2.readlines():
    a2_list.append(line.rstrip())

if len(a1_list) > len(a2_list):
    ltab = len(a1_list)
elif len(a1_list) < len(a2_list):
    ltab = len(a2_list)
else:
    ltab = len(a1_list)

output = open("wynik.txt", "a", encoding="utf8")

for x in range(ltab):
    try:
        print(a1_list[x])
        output.write(a1_list[x]+"\n")
    except IndexError:
        print("Nie ma kolejnej linijki")

    try:
        print(a2_list[x])
        output.write(a2_list[x]+"\n")
    except IndexError:
        print("Nie ma kolejnej linijki")

output.close()
