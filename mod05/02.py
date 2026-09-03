while True:
    varInch = float(input("enter umber in inch to see in CM "))
    
    if varInch < 0:
        print("wrong value")
        break
    
    varCM = varInch * 2.54
    print(f"{varInch} inch = {varCM:.2f} cm")
