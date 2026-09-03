import random

randomNum = random.randint(1, 10)

while True:
    guess = int(input("arvo numero 0-10: "))

    if guess > randomNum:
        print("Liian suuri arvaus")
    elif guess < randomNum:
        print("Liian pieni arvaus")
    else:
        print("Oikein ", randomNum)
        break