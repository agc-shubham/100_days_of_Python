import art
print(art.logo)
print("Start the bidding Enter your name and Bid: ")


bids ={}
while(True):
    isTrue = input("Are there any more bidders, Type yes or no: ")
    isTrue.lower()
    if isTrue == "no":
        break
    
    bidder = input("Enter the name of the bidder: ")
    value = int(input("Enter the bid value: "))
    bids[bidder] = value

high = 0
name = ""
for key,value in bids.items():
    if(value>high):
        high = value
        name = key

print(f"Highest bid is {high} from {name}")