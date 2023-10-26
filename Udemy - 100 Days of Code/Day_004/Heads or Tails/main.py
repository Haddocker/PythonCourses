import random

input("Pick Heads (H) or Tails (T): ")

coin_flip = random.randint(0, 1)
if coin_flip == 1:
    print("Heads!")
else:
    print("Tails!")