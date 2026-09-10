import random


def heita_noppaa(tahkot):
    return random.randint(1, tahkot)


tahkot = int(input("Anna nopan tahkojen määrä: "))

while tahkot < 1:
    tahkot = int(input("Anna vähintään 1: "))

silmaluku = 0

while silmaluku != tahkot:
    silmaluku = heita_noppaa(tahkot)
    print(silmaluku)