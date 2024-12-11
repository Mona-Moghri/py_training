bid= {} #need to be outside of the while loop so that it accumulate and dosen't reset to zero every time the while loop runs
while True:
    name= input("what is your name?: ")
    price= int(input("What is your bid?: $"))
    bid[name] = price    #process to save the data into dictionary
    other_person= input("Are_there_any_other_bidders? Type 'yes' or 'no'").lower()
    if other_person == "yes":
        print("\n" *20) #provide the blank screen for avoiding to see previous input
    elif other_person != "yes":
        break
def find_max_bid():
    max_bid= max(bid.values())  #max find maximum function in all value on dictionary
    for key, value in bid.items():     #.items() to get both keys and values from the dictionary.
        if value == max_bid:
            winner = key
    print(f"The winner is {winner} with a bid of {max_bid}")
find_max_bid()