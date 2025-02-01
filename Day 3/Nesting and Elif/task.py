print("Welcome to the rollercoaster!")
x = int(input("What is your height in cm? "))

# if x >= 120:
#     print("You can ride the rollercoaster")
# else:
#     print("Sorry you have to grow taller before you can ride.")

# roller coaster problem


if x > 120:
    print("you can ride")
    y = int(input("How old are you"))
    if y <12:
        print("pay 5$")
    if y >18:
        print("pay 12$")
    if y >= 12 and y <= 18:
        print("pay 7$")

else:
    print("You cannot ride")