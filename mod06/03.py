def gallonat_litroiksi(gallonat):
    return gallonat * 3.785


gallonat = float(input("Anna gallonamäärä: "))

while gallonat >= 0:
    litrat = gallonat_litroiksi(gallonat)
    print(f"Litramäärä: {litrat:.3f} l")

    gallonat = float(input("Anna gallonamäärä: "))