trueUser = "python"
truePass = "rules"

i = 0

while i < 5:
    userName = input("Enter your username: ")
    userPass = input("Enter password: ")

    if userName == trueUser and userPass == truePass:
        print("welcome")
        break
    else:
        print("wrong password or username")
        i += 1

if i == 5:
    print("forbiden")
