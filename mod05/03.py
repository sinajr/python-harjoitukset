userNumList=[]
while True:
    userNum=input("enter your number")
    if userNum !="":
        userNumList.append(float(userNum))
    else:
        print (userNumList)
        print("end")
        userNumList.sort()
        print (userNumList)
        print(f"suurimman:  {userNumList[-1]}")
        print(f"pienimmän : { userNumList[0]}")
        break