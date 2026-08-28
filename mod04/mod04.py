name=[]
nimi= input("enter name ")
while nimi != "":
    name.append(nimi)
    nimi= input("enter name or just enter to see the result: ")
    pois=input("haluatko poista nimi k/e ")
    if nimi=="":
         print("your list name is :   ")
    elif pois=="k":
        removeName= input("type the name you want to be remove: ")
        name.remove(removeName)
        print(removeName +" has been removed")
    else:
            continue
print(name)

# lukku = 0
# while lukku <=5:
#     print(lukku)
#     lukku = lukku + 1



# komento = input("anna komento ")
# while komento != "lopeta":
#     if komento == "mayday":
#         break
#     print("suoran toiminnon: "+ komento)
#     komento = input("anna komento: ")
# else:
#     print("Nakemin")
# print("toiminnot lopettu")



# import random

# randomVar= random.randint(1,100)

# print(randomVar)




# agex= int(input("put your age"))
# if agex >= 65:
#     print("olet elake")
# elif agex >= 18:
#     print("olet tyossa")
# elif agex >= 7:
#     print("olet koulussa")
# else:
#      print(" olet pikku lapsi")









# age= int(input("how old are you?"))
# if 15 <= age <=18:
#     weight= int(input("type your weight "))
#     if (weight >= 55 and 18 >= age >= 15) :
#         print("lääken käyttö on sallittua")
# else:
#     print("lääken ei saa käyttä ")





















# age= int(input("how old are you?"))
# if 15 <= age <=18:
#     wight= int(input("type your wight"))
#     if wight > 55:
#         print(f"you can have the pills")
#     else:
#         print(f"you dont have right")
# else:
#     print("you are not in right range")







# raha= float(input("how much raha you have?"))
# latte=5.45
# if raha >= latte:
#     x= raha-latte
#     print(f"fyou can have latte \n {float(x)} you still have float(x) €")

# else:
#     print("you can dont have enoth money ")
