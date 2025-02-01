import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# jawaban EASY

kata_kunci = []


for huruf in range(nr_letters):
    hurufnya = random.choice(letters)
    kata_kunci.append(hurufnya)
for simbol in range(nr_symbols):
    simbol = random.choice(symbols)
    kata_kunci.append((simbol))
for angka in range(nr_numbers):
    angka = random.choice(numbers)
    kata_kunci.append((angka))

print("\n yang easy")
print("".join(kata_kunci))

# jawaban HARD

print("\nJawaban yang hard")
random.shuffle(kata_kunci)
print("".join(kata_kunci))