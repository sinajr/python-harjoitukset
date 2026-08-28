import random

# täälä otettan käyttäjän nimi ja ikä 




playerName = input("what is the player name? ");
playerAge = int(input("player age: "));
userChoosedNum=[]
randomArray=[]

randomNum = random.randint(0,36)
roulettetiRandom = randomNum
randomArray.append(roulettetiRandom)

colorPicker=int(random.random()*100)
if colorPicker>=50:
    colorPicker = "red"
    randomArray.append(colorPicker)
else:
    olorPicker = "black"
    randomArray.append(colorPicker)

evenOrodd=""
if roulettetiRandom / 2 == 0:
    evenOrodd="even"
    randomArray.append(evenOrodd)
else:
    evenOrodd="odd"
    randomArray.append(evenOrodd)


userCredit= 0
betPrice=2
if  12 <= playerAge:
    print("welcome "+ playerName +" "+ "you are"+" "+ str(playerAge)+" ")
    userCredit=float(input("how much € you are going to bring?\n \nJust enter number: "))
    betCounter=int(userCredit/betPrice)
    if userCredit >= 5:
        print(f"you have {userCredit} € in your wallet \n \nyou can have {betCounter} bet chance")

        for i in range(betCounter):
            userType = input("ok "+playerName+" select your number: \n \nor you can choose black and red \n \nor even or odd numbers \n \nfor betting type bet: ")
            if userType.isnumeric():
                if 0 <= int(userType) <= 36:
                    userChoosedNum.append(userType)
                else:
                    print("please enter number between 0 _ 36 or type RED or BLACK, also you can choose EVEN and ODD")
                    userType= input("try again")
                    if 0 <= int(userType) <= 36:
                        userChoosedNum.append(userType)
            else:
                userChoosedNum.append(userType)
        i +=1
        if i == betCounter:
            print(f"you are out of chance \n \n Your creadit is: {userCredit-(betCounter * betPrice)} € \n \n the result is: ")
            print(f"this what you choosed {playerName}: \n{userChoosedNum}")
            print(f"the roulette result is \n{randomArray}")


    else:
        print("you should charge at least 5€ in your wallet")
else:
    print(playerName +" you are"+" "+str(playerAge)+" "+"years old\n" + "you are under 18 so just go back")