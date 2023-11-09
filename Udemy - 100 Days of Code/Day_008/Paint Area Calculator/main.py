import math

def paint_calc(height, width, cover):
    amount_of_cans = (height * width) / cover
    round_up_cans = math.ceil(amount_of_cans)
    print(f"You'll need {round_up_cans} cans of paint.")

test_h = int(input("Height of wall in meter: "))
test_w = int(input("Width of wall in meter: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)