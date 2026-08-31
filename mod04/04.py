while True:
    leapYear=int(input("Enter the year number \n"))

    if leapYear % 400==0:
        print(f"{leapYear} year is a leap year \n \n")
    elif leapYear % 100==0:
        print(f"{leapYear} year is NOT a leap year \n \n")
    elif leapYear % 4==0:
        print(f"{leapYear} year is a leap year \n \n")
    else:
        print(f"{leapYear} year is NOT a leap year \n \n")