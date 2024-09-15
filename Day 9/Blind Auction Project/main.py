from art import logo

print(logo)

bid_list = {}
anyOtherBid = True
while anyOtherBid:
    name = input("Enter your name : ")
    bid = int(input("Enter your bid Amount: "))
    bid_list[name] = bid
    nextBid =input("Any other bidder yes/no ? ").lower()
    if nextBid == "yes":
        print("\n"*10)
        print(logo)
    else:
        anyOtherBid = False

# can also use max(bid_list) will return key with max value
name = ""
highest_bid = 0
for key in bid_list:
    if bid_list[key] > highest_bid:
        name = key
        highest_bid = bid_list[key]

print(f"{name} won the auction with bid amount $ {highest_bid}")