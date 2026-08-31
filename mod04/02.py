shipClass=input("kirija laivan hyttiluokan (LUX, A, B, C)? ")

if shipClass == "LUX" or shipClass == "lux":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif shipClass=="A" or shipClass== "a":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif shipClass=="B" or shipClass== "b":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif shipClass=="C" or shipClass== "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka")