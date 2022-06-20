# Split string method
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#print(names)
num_items=len(names)

random_choice=random.randint(0,num_items-1)

who_is_going_to_buy=names[random_choice]

print(who_is_going_to_buy+" is going to buy meal today!")
