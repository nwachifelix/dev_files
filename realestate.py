print("A one bedroom flat in Lekki area is listed at N60,000,000. ")
print("Enter your first offer on the house. ")
offer = abs(int(input()))
print("Enter your best offer on the house. ")
best = abs(int(input()))
print("How much more do you want to offer each time? ")
increament = abs(int(input()))
offer_accepted = False
while offer <= best:
    if offer >= 61000000:
        offer_accepted = True
        print("your offer of", offer, "has been accepted! ")
        break
    print("We\'re sorry, your offer of", offer, "naira has not been accepted. ")
    offer += increament