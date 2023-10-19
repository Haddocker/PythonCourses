# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12
# Round the result to 2 decimal places.

print("Welcome to the tip calculator\n")

bill = float(input("What was the total bill?: $"))
tip = int(input("What percentage tip would you like to give ? 10, 12, or 15?: "))
people = int(input("How many people to split the bill?: "))


# MY CODE:
# bill_pr_person = round((bill / people) * (1 + (tip / 100)), 2)
# total_bill = round((bill_pr_person * people), 2)
#
# print(f"The total bill is ${total_bill}")
# print(f"and you all have to pay ${bill_pr_person} each.")


# UDEMY CODE:
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
final_amount = ":.2f".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")