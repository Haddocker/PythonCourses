# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12
# Round the result to 2 decimal places.

print("Welcome to the tip calculator\n")

bill = input("What was the total bill?: $")
tip = input("What percentage tip would you like to give ? 10, 12, or 15?: ")
people = input("How many people to split the bill?: ")


total_bill = (bill / tip) * (1 * (100))

bill_