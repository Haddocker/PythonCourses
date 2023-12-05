from art import logo
print(logo)

bids = {}
restart = True

def clear_screen():
    print('\n' * 100)

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The highest bidder is {winner}, with a bid of ${highest_bid}.")


while restart is True:
    name = input("What is your name?: ") #Key
    price = int(input("What's your bid?: $")) #Value
    bids[name] = price

    add_new_bidder = input("Are there anymore who wants to bid? Y or N: ").lower()
    if add_new_bidder == 'n':
        restart = False
        find_highest_bidder(bids)
    elif add_new_bidder == 'y':
        clear_screen()
