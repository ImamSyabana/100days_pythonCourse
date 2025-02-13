def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

opsDic = {
    "+" : add,
    "-" : substract,
    "*" : mult,
    "/" : divide
}

import art

print(art.logo)

def inputanKalkulasiAwal():
    n1 = int(input("What is the first number?: "))
    for x in opsDic:
        print(x)
    ops = str(input("Pick an operator: "))
    n2 = int(input("What is the second number?: "))

    return n1, n2, ops

def operasiBaru(n1, n2, ops):
    if ops in opsDic:
        hasil = opsDic[ops](n1, n2)
        print(f"{n1} {ops} {n2} = {hasil}")
    else:
        print("Unknown operator")
        return None
    return hasil

def inputanKalkulasiLanjutan():
    for x in opsDic:
        print(x)
    ops = str(input("Pick an operator: "))
    n2 = int(input("What is the second number?: "))

    return n2, ops

def operasiLanjutan(hasil, n2, ops):
    if ops in opsDic:
        hasilLanjut = opsDic[ops](hasil, n2)
        print(f"{hasil} {ops} {n2} = {hasilLanjut}")
    else:
        print("Unknown operator")
        return None
    return hasilLanjut

n1, n2, ops = inputanKalkulasiAwal()
hasil = operasiBaru(n1, n2, ops)

while True:
    isCont = str(input(f"Type 'y' to continue calculating with {hasil}, or type 'n' to start a new calculation: "))
    if isCont == "y":
        n2, ops = inputanKalkulasiLanjutan()
        hasil = operasiLanjutan(hasil, n2, ops)
        if hasil is None:
            break
    elif isCont == "n":
        n1, n2, ops = inputanKalkulasiAwal()
        hasil = operasiBaru(n1, n2, ops)
        if hasil is None:
            break
    else:
        print("Invalid input. Please type 'y' or 'n'.")