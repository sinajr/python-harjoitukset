import random

BET_PRICE = 2
MAX_BETS = 3
WIN_CREDIT = 100


# Person is the parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Player is the child class (inherits name and age from Person)
class Player(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.credit = 0
        self.bets = []

    # save the credit to a file with the player's name
    def save(self):
        file = open(self.name + ".txt", "w")
        file.write(str(self.credit))
        file.close()

    # read the credit from the file
    def load(self):
        # "a" mode makes the file if it is not there yet
        file = open(self.name + ".txt", "a")
        file.close()

        file = open(self.name + ".txt", "r")
        text = file.read()
        file.close()

        if text != "":
            self.credit = float(text)


class Roulette:
    def __init__(self):
        self.number = 0
        self.color = ""
        self.evenOrOdd = ""

    def spin(self):
        self.number = random.randint(0, 36)

        if random.random() * 100 >= 50:
            self.color = "red"
        else:
            self.color = "black"

        if self.number % 2 == 0:
            self.evenOrOdd = "even"
        else:
            self.evenOrOdd = "odd"

    # returns how many times the bet price you win (0 = lose)
    def checkBet(self, bet):
        if bet == str(self.number):
            return 36
        elif bet == self.color or bet == self.evenOrOdd:
            return 2
        else:
            return 0


# check that the user typed something we understand
def isValid(text):
    if text.isnumeric():
        return 0 <= int(text) <= 36
    return text == "red" or text == "black" or text == "even" or text == "odd"


playerName = input("what is the player name? ")
playerAge = int(input("player age: "))

if playerAge >= 18:
    player = Player(playerName, playerAge)
    player.load()  # read old credit from file
    print("welcome " + player.name + " you are " + str(player.age))

    if player.credit < 5:
        player.credit += float(input("how much € you are going to bring? "))

    if player.credit >= 5:
        playing = True

        while playing:
            player.bets = []
            roulette = Roulette()

            betCounter = int(player.credit / BET_PRICE)
            if betCounter > MAX_BETS:
                betCounter = MAX_BETS

            print(f"\nyou have {player.credit} € and can have "
                  f"{betCounter} bet chance")

            betsAdded = False
            roundOver = False

            while not roundOver:
                print("\n1. Select your bets")
                print("2. Show your choices")
                print("3. Show result")
                menuChoice = input("select: ")

                if menuChoice == "1":
                    if betsAdded == False:
                        for i in range(betCounter):
                            userType = input(
                                "select number 0-36, red, black, even or odd: ")
                            while not isValid(userType):
                                userType = input("wrong, try again: ")
                            player.bets.append(userType)
                        betsAdded = True
                    else:
                        print("you have already selected your bets")

                elif menuChoice == "2":
                    print(f"this what you choosed {player.name}:")
                    print(player.bets)

                elif menuChoice == "3":
                    if betsAdded:
                        roulette.spin()
                        print("the roulette result is:")
                        print(roulette.number, roulette.color,
                              roulette.evenOrOdd)

                        # pay for the bets, then check which ones won
                        player.credit -= betCounter * BET_PRICE
                        for bet in player.bets:
                            times = roulette.checkBet(bet)
                            if times > 0:
                                print("bet " + bet + " won!")
                                player.credit += times * BET_PRICE

                        print(f"Your credit is: {player.credit} €")
                        player.save()  # write credit to file
                        roundOver = True
                    else:
                        print("select your bets first")

                else:
                    print("please select 1, 2 or 3")

            if player.credit < BET_PRICE:
                print("\nGAME OVER: you have no money left")
                playing = False
            elif player.credit >= WIN_CREDIT:
                print("\nYOU WIN: you have " + str(player.credit) + " €")
                playing = False
            else:
                again = input("\nplay again? (y/n): ")
                if again != "y":
                    print("see you next time, your credit is saved")
                    playing = False
    else:
        print("you should charge at least 5€ in your wallet")

else:
    print(playerName + " you are " + str(playerAge)
          + " years old\nyou are under 18 so just go back")
