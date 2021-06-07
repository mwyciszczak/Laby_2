#  sortowanie ściągnięte z internetu
#  dane wczytywane będą z pliku txt, a wyniki zapisywane do tego samego formatu
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


inp = [4, 10, 11, 5, 73, 5, 1]
tab_plik = []

f = open("liczby.txt", "r")
string = f.readline()
string = string.split(',')
for x in string:
    tab_plik.append(int(x.strip()))

heap_sort(tab_plik)
print(tab_plik)
f.close()
w = open("wynik.txt", "a")
for x in tab_plik:
    w.write(str(x))
    w.write(', ')
w.close()


