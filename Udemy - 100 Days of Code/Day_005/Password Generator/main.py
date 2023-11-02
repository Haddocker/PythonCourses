#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")

nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Capture if user input is 0 - NOT DONE.
if nr_letters < 2:
    print("You have to have at least 2 letters! Try again.")
    nr_letters = int(input("How many letters would you like in your password?\n"))
if nr_symbols < 2:
    print("You have to have at least 2 symbols! Try again.")
    nr_symbols = int(input(f"How many symbols would you like?\n"))
if nr_numbers < 2:
    print("You have to have at least 2 numbers! Try again.")
    nr_numbers = int(input(f"How many numbers would you like?\n"))


# Eazy Level - Order not randomised:
# password = ""
#
# for letter in range(1, nr_letters + 1):
#     password += random.choice(letters)
#
# for letter in range(1, nr_symbols + 1):
#     password += random.choice(numbers)
#
# for letter in range(1, nr_symbols + 1):
#     password += random.choice(symbols)
#
# print(password)


# Hard Level - Order of characters randomised:
password = ""

for letter in range(1, nr_letters + 1):
    password += random.choice(letters)

for letter in range(1, nr_symbols + 1):
    password += random.choice(symbols)

for letter in range(1, nr_numbers + 1):
    password += random.choice(numbers)

password_list = list(password)
random.shuffle(password_list)

print(''.join(password_list))