import os
auction_is_over = True
bidder = {}


def highest_bidder(highest_bidder):
    highest_bid = 0
    winner = ""
    for person in highest_bidder:
        value = highest_bidder[person]
        if value > highest_bid:
            highest_bid = value
            winner = person
    print(f"Drumrolls \nThe winner of this auction is {winner} with a bid of ${highest_bid}")


while auction_is_over:
    name = input("Your Name : ")
    bid = int(input("Your bid is : $"))
    choice = input("Do we have more bidders present here?\nyes/no")
    bidder[name] = bid
    if choice == "yes":
        os.system('cls')
        auction_is_over = True
    else:
        os.system('cls')
        highest_bidder(bidder)
        auction_is_over = False
