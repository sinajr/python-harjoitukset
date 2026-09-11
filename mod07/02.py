import random
noppa_tahkoista = int(input("kirija noppan tahkosta: "))
def random_noppa(tahko):
    i=0
    while i <tahko:
        randomNum = int(random.randint(1,tahko))
        print(randomNum)
        i=randomNum
random_noppa(noppa_tahkoista)