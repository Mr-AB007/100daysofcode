print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bil? "))
bittip= round((bill + (bill*0.12))/people,1)
print(bittip)


