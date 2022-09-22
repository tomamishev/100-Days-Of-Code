# You are going to write a program that will select a random name from a list of names.
# The person selected will have to pay for everybody's food bill.
# You are not allowed to use the choice() function.

import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

length = len(names)
random = random.randint(0, length - 1)

print(f"{names[random]} is going to buy the meal today!")


