# try:
#     age = int(input("How old are you?"))
#
# except ValueError:
#     while age.isnumeric() != True:
#
#         print("Please enter a valid number: ")
#         age = int(input("How old are you?"))

while True:
    try:
        age = int(input("How old are you? "))  # Try to get a valid integer
        break  # If successful, exit loop
    except ValueError:
        print("Please enter a valid number.")  # Prompt again if input is invalid

if age > 18:
    print(f"You can drive at age {age}.")
