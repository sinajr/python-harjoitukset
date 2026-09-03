import random

pisteiden_maara = int(input("Anna arvottavien pisteiden määrä: "))

ympyran_sisalla = 0

for i in range(pisteiden_maara):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x ** 2 + y ** 2 < 1:
        ympyran_sisalla += 1

piin_likiarvo = 4 * ympyran_sisalla / pisteiden_maara

print(f"Piin likiarvo on: {piin_likiarvo}")