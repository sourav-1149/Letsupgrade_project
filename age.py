def age():
    age=int(input("enter your age "))
    if age<18:
        print ("you are minor")

    elif age>=18 and age<65:
        print("you are adult")

    else:
        print("you are senior")

    age()
