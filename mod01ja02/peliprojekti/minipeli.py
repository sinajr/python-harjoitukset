# täälä otettan käyttäjän nimi ja ikä
playerName = input("what is the player name?");
playerAge = int(input("player age:"));
if  18 <= playerAge:
    print("welcome "+ playerName +" "+ "you are"+" "+ str(playerAge)+" " + " \n"+"press to continue ");
else:
    print("you are"+" "+str(playerAge)+" "+"years old\n" + "you are under 18 so just go back")