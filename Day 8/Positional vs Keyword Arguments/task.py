# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")

def greet_with(name = "Budi", location = "Jakarta"):
    print(f"Helo {name}")
    print(f"What is it like in {location}")

greet_with("Jery", "US")


def calculate_love_score(type1 , type2):
    type1 = type1.upper()
    type2 = type2.upper()
    nt = (type1.count("T") + type2.count("T"))
    nr = (type1.count("R") + type2.count("R"))
    nu = (type1.count("U") + type2.count("U"))
    ne = (type1.count("E") + type2.count("E"))

    # print("T occurs {nt} times".format(nt=nt))
    # print("R occurs {nr} times".format(nr=nr))
    # print("U occurs {nu} times".format(nu=nu))
    # print("E occurs {ne} times".format(ne=ne))

    #("Total = {total}".format(total=nt + nr + nu + ne))

    nl = (type1.count("L") + type2.count("L"))
    no = (type1.count("O") + type2.count("O"))
    nv = (type1.count("V") + type2.count("V"))
    ne2 = (type1.count("E") + type2.count("E"))

    # print("L occurs {nl} times".format(nl=nl))
    # print("O occurs {no} times".format(no=no))
    # print("V occurs {nv} times".format(nv=nv))
    # print("E occurs {ne2} times".format(ne2=ne2))

    #print("Total = {total}".format(total=nl + no + nv + ne2))

    total1 = str(nt + nr + nu + ne)
    total2 = str(nl + no + nv + ne2)

    totalLove = total1+total2
    return (totalLove)

print(calculate_love_score(type1 =  "Angela Yu", type2 = "Jack Bauer"))