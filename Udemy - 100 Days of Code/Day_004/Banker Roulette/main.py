names_string = input("Write all your names comma separated: ")

names = names_string.split(", ")

import random

# Get the total number of item in list.
num_items = len(names)

# Generate random numbers between 0 and the last index.
random_choice = random.randint(0, num_items - 1)

# Pick out a random person from list of names using the random number.
person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to pay for the meal today!")