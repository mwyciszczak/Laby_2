import timeit

#  stos za pomocą podwójnie zakończonek kolejki(deque)
x = """from collections import deque
import random

kolejka50 = deque()
kolejka100 = deque()
kolejka150 = deque()

for x in range(50):
    kolejka50.append(random.randint(1, 1000))

for x in range(100):
    kolejka100.append(random.randint(1, 1000))

for x in range(150):
    kolejka150.append(random.randint(1, 1000))

print(kolejka50, kolejka100, kolejka150)"""

print("Operacja zajęła {}".format(timeit.timeit(stmt=x, number=1)))