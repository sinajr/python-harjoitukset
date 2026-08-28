# täälä otettan käyttäjän nimi ja ikä
import random


playerName = input("what is the player name?");
playerAge = int(input("player age:"));
userChoosedNum=[]

if  12 <= playerAge:
    print("welcome "+ playerName +" "+ "you are"+" "+ str(playerAge)+" ")
    while True:
        userType = input("ok "+playerName+" select your number: \n or you can choose black and red \n color or even or odd numbers \n for betting type bet: ")

        if userType == "bet":
            print(userChoosedNum)
            break

        userChoosedNum.append((userType))
else:
    print(playerName +" you are"+" "+str(playerAge)+" "+"years old\n" + "you are under 18 so just go back")

# randomNum = random.randint(0,36)
# print(randomNum)