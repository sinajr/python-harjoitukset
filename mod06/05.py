def poista_parittomat(luvut):
    parilliset = []

    for luku in luvut:
        if luku % 2 == 0:
            parilliset.append(luku)

    return parilliset


luvut = [1, 2, 3, 4, 5, 6, 7, 8]

uusi_lista = poista_parittomat(luvut)

print("Alkuperäinen lista:", luvut)
print("Karsittu lista:", uusi_lista)