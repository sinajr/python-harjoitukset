def laske_summa(luvut):
    summa = 0

    for luku in luvut:
        summa = summa + luku

    return summa


luvut = [2, 5, 8, 3, 10]

tulos = laske_summa(luvut)

print("Summa:", tulos)