import art

print(art.logo)

# TODO-1: Ask the user for input
bidder = {}

bid_cont = True
while bid_cont == True:
    name = str(input("What is your name? "))
    ammount = int(input("What is your bid? "))

    # TODO-2: Save data into dictionary {name: price}
    bidder[name] = ammount

    # TODO-3: Whether if new bids need to be added
    bid_yn = str(input("Are there any other bidders? Type 'yes or no'. ")).lower()
    print("\n" * 100)

    if bid_yn == "yes":
        bid_cont = True
    elif bid_yn == "no":
        bid_cont = False



# TODO-4: Compare bids in dictionary
highestBid_ammount = 0
highest_bidder = ""

for x in bidder:
    if bidder[x] > highestBid_ammount:
        highestBid_ammount = int(bidder[x])
        highest_bidder = str(x)
    elif bidder[x] < highestBid_ammount:
        highestBid_ammount = highestBid_ammount
        highest_bidder = highest_bidder

print("The winner is {bid_person} with a bid of {ammount_bid}. ".format(bid_person = highest_bidder, ammount_bid = highestBid_ammount))