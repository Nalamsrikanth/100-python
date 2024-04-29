height = int(input())
if height >= 120:
    print(("You can ride."))
    age = int(input("What is your age?"))
    if age < 12:
        print("your ticket price is $5")
        ticket = int(5)
    elif age <18:
        print("your ticket price is $7")
        ticket = int(7)
    elif age >= 18:
        print("your ticket price is $12")
        ticket = int(12)

    photo = input("do you want photo yes or no")
    if photo == "yes":
        print("its price is $3")
        ticket += int(3)
    print(f" the total bill is {ticket}")
else:
    print("you cant ride")



