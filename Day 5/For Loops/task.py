from xmlrpc.client import APPLICATION_ERROR

fruits = ["Apple", "Peach", "Pear"]

# pause 1

# Apple -> Apple pie -> Peach -> Peach pie -> Pear -> Pear pie

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")