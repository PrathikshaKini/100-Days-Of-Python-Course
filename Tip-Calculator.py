print("Welcome to the tip calculator!")

bill=float(input("What was the total bill? $"))

tip=int(input("How much tip would you like to give? 10, 12, or 15?"))

num=int(input("How many people to split the bill?"))

rate=bill*(tip/100)

amount=bill+rate

net_amount=amount/num

#Rounding to 2 decimal places
answer =round(net_amount, 2)

print("Each person should pay: ${0}".format(answer))
