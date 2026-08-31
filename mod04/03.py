while True:
    gender=input("what is your gender (M/F)? ")

    if gender=="M" or gender=="m":
        print("u r male \n ")
        hemoglobin= int(input("how much is your hemoglobin? (enter the number g/l) "))
    
        if 134< hemoglobin <195:
            print(f"Miesten normaali hemoglobiiniarvo on välillä 117-175 g/l. \nJa sinun oli {hemoglobin} g/l.")
        elif hemoglobin <= 134:
            print("hemoglobiiniarvo alhainen")
        elif 195 <= hemoglobin:
            print("hemoglobiiniarvo korkea")
        else:
            print("enter true value")

    elif gender=="F" or gender=="f":
        print("u r famale \n")
        hemoglobin= int(input("how much is your hemoglobin? (enter the number g/l) "))
    
        if 117< hemoglobin <175:
            print(f"Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l. \nJa sinun oli {hemoglobin} g/l.")
        elif hemoglobin <= 117:
            print("hemoglobiiniarvo alhainen")
        elif 175 <= hemoglobin:
            print("hemoglobiiniarvo korkea")
        else:
            print("enter true value")
    else:
        print("Enter true value")