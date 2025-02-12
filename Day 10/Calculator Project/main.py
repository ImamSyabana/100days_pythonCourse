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

test = {
    "wew" : 21
}

import art

print(art.logo)

# terakhir bikin kode kalkulasi make def yang ada di dic
isCalcs = True

# dibikin jadi fungsi aja

def inputanKalkulasi():
    n1 = int(input("What is the first number?: "))
    for x in opsDic:
        print(x)
    ops = str(input("Pick an operator"))
    n2 = int(input("What is the second number?: "))

    return n1, n2, ops

def operasiBaru (n1, n2, ops):
    if ops == "+":
        hasil = opsDic['+'](n1, n2)
        print("{n1} {ops} {n2} = {result}".format(result = hasil, n1 = n1, n2 = n2, ops = ops))
    elif ops == "-":
        hasil = opsDic['-'](n1, n2)
        print("{n1} {ops} {n2} = {result}".format(result = hasil, n1 = n1, n2 = n2, ops = ops))
    elif ops == "*":
        hasil = opsDic['*'](n1, n2)
        print("{n1} {ops} {n2} = {result}".format(result = hasil, n1 = n1, n2 = n2, ops = ops))
    elif ops == "/":
        hasil = opsDic['/'](n1, n2)
        print("{n1} {ops} {n2} = {result}".format(result = hasil , n1 = n1, n2 = n2, ops = ops))
    else:
        print("Unknown operator")

    return hasil

def operasiLanjutan (hasil, n2, ops):
    if ops == "+":
        hasilLanjut = opsDic['+'](hasil, n2)
        print("{n1} {ops} {n2} = {result}".format(result = hasilLanjut, n1 = hasil, n2 = n2, ops = ops))
    elif ops == "-":
        hasilLanjut = opsDic['-'](hasil, n2)
        print("{n1} {ops} {n2} = {result}".format(result = hasilLanjut, n1 = hasil, n2 = n2, ops = ops))
    elif ops == "*":
        hasilLanjut = opsDic['*'](hasil, n2)
        print("{n1} {ops} {n2} = {result}".format(result = hasilLanjut, n1 = hasil, n2 = n2, ops = ops))
    elif ops == "/":
        hasilLanjut = opsDic['/'](hasil, n2)
        print("{n1} {ops} {n2} = {result}".format(result = hasilLanjut , n1 = hasil, n2 = n2, ops = ops))
    else:
        print("Unknown operator")

    return hasil





while isCalcs == True:

    inputanKalkulasi()

    operasiBaru(inputanKalkulasi())


    isCont = str(input("Type 'y' to continue calculating with {result}, ot type 'n' to start a new calculation: ". format(result = hasil )))
    if isCont == "y":
        isCalcs == True
    elif isCont =="n":
        isCalcs == False




