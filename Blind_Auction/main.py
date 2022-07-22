#!/usr/bin/python3

from art import logo
import os

#Print the logo and clear the screen
os.system("clear")
print(logo)


end_of_bid = False
bidders_dictionary = {}

def find_the_hghiest_bidder(bidders):
    winner_bidder = ""
    top_bid_amount = 0
    for bidder in bidders:
        bidder_bid = bidders[bidder]
        if bidder_bid >= top_bid_amount:
            top_bid_amount = bidder_bid
            winner_bidder = bidder
    print()
    print(f"The winner is '{winner_bidder}' with a bid of '${top_bid_amount}'.")
    print("Have a nice day!")

while not end_of_bid:
    bidder_name = input("What is your name?: ")
    bid_amount = int(input("What is your bid?: $"))
    bidders_dictionary[bidder_name] = bid_amount
    
    # ask if the is another bidder
    other_bidders = input("Are there any other bidders? type 'yes' or 'no'.\n").lower()
    if other_bidders == 'no':
        find_the_hghiest_bidder(bidders_dictionary)

        end_of_bid = True
    else:
        os.system("clear")
    
            








