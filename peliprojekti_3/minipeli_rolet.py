import random


# Kysytään käyttäjän valinnat ja lisätään ne listaan
def addChoices(playerName, betCounter, userChoosedNum):
    for i in range(betCounter):
        userType = input(
            "ok " + playerName + " select your numbers:\n"
            "or you can choose black and red\n"
            "or even or odd numbers: "
        )

        if userType.isnumeric():
            if 0 <= int(userType) <= 36:
                userChoosedNum.append(userType)

            else:
                print("please enter number between 0 - 36")
                userType = input("try again: ")

                if userType.isnumeric():
                    if 0 <= int(userType) <= 36:
                        userChoosedNum.append(userType)
        else:
            userChoosedNum.append(userType)


# Tulostetaan käyttäjän lista
def showChoices(playerName, userChoosedNum):
    print(f"this what you choosed {playerName}:\n{userChoosedNum}")


# Tulostetaan pelin tulos
def showResult(userCredit, betCounter, betPrice, randomArray):
    print(
        f"you are out of chance\n"
        f"Your credit is: {userCredit - (betCounter * betPrice)} €\n"
        f"the result is:"
    )
    print(f"the roulette result is\n{randomArray}")


# täälä otettan käyttäjän nimi ja ikä
while True:
    playerName = input("what is the player name? ")
    playerAge = int(input("player age: "))

    # tyhjä lista että säästetään mikä numeroita käytäjä on valinnut
    userChoosedNum = []

    # tyhjä lista että säästetään ranomit numerot
    randomArray = []

    # Lasketan randomit numerot
    randomNum = random.randint(0, 36)
    roulettetiRandom = randomNum
    randomArray.append(roulettetiRandom)

    colorPicker = random.random() * 100

    if colorPicker >= 50:
        colorPicker = "red"
        randomArray.append(colorPicker)
    else:
        colorPicker = "black"
        randomArray.append(colorPicker)

    evenOrodd = ""

    if roulettetiRandom % 2 == 0:
        evenOrodd = "even"
        randomArray.append(evenOrodd)
    else:
        evenOrodd = "odd"
        randomArray.append(evenOrodd)

    # käytäjän Credit ja joka peli maksu
    userCredit = 0
    betPrice = 2

    # tarkistetaan käytäjän ikä
    if 12 <= playerAge:
        print(
            "welcome " + playerName + " "
            + "you are" + " " + str(playerAge) + " "
        )

        # lasketan käytäjän raha ja veto
        userCredit = float(
            input("how much € you are going to bring?\n\nJust enter number: ")
        )
        betCounter = int(userCredit / betPrice)

        # käytäjän credit pitäs olla yli 5 euro
        if userCredit >= 5:
            print(
                f"you have {userCredit} € in your wallet\n\n"
                f"you can have {betCounter} bet chance"
            )

            betsAdded = False

            while True:
                print("\n1. Select your bets")
                print("2. Show your choices")
                print("3. Show result")

                menuChoice = input("select: ")

                if menuChoice == "1":
                    if betsAdded == False:
                        addChoices(playerName, betCounter, userChoosedNum)
                        betsAdded = True
                    else:
                        print("you have already selected your bets")

                elif menuChoice == "2":
                    showChoices(playerName, userChoosedNum)

                elif menuChoice == "3":
                    if betsAdded:
                        showResult(
                            userCredit, betCounter, betPrice, randomArray
                        )
                        break
                    else:
                        print("select your bets first")

                else:
                    print("please select 1, 2 or 3")

        else:
            print("you should charge at least 5€ in your wallet")

    else:
        print(
            playerName + " you are " + str(playerAge)
            + " years old\n"
            + "you are under 18 so just go back"
        )