print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = bill + 5
        print("Please pay ${harga}".format(harga=bill))
    elif age <= 18:
        bill = bill + 7
        print("Please pay ${harga}".format(harga=bill))
    else:
        bill = bill + 12
        print("Please pay ${harga}".format(harga=bill))

    x = str(input("Do you want photos:"))
    if x == "YES":
        bill = bill + 3
        print("Your price is ${harga}".format(harga=bill))
    elif x == "NO":
        bill = bill + 0
        print("Your price is ${harga}".format(harga=bill))
else:
    print("Sorry you have to grow taller before you can ride.")
