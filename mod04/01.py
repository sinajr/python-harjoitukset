normaliKala=37
userKala=float(input("how big is your fish in (cm)\n "))

if(userKala<37):
    print("The fish is still small throw it back to lake \n \n")
    print(f"Your fish is {normaliKala-userKala} cm smaller than normal")
else:
    print("Fish size is ok")