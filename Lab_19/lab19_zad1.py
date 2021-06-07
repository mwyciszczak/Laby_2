import re

tab = []
pl_zipc = re.compile("\d\d-\d\d\d")
us_zipc = re.compile("\d\d\d\d\d")

try:
    nr = pl_zipc.search("51-649")
    nrzip = nr.group()
except AttributeError:
    print("Nie podano właściwego kodu pocztowego")
    raise AttributeError

f = open("zip.txt", "a")
f.write(nrzip)
f.close()


"""

nr = pl_zipc.search("podaje kody pocztowe 51-649 oraz 50-012 a na koniec 00-000")
for x in nr:
    tab.append(x)
if len(tab) == 0:
    raise 


f = open("zip.txt", "a")
for x in tab:
    x = x + "\n"
    f.write(x)
f.close()"""
# search zwraca tylko pierwszy w formie obiektu; .group()
