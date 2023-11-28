alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo
print(logo)

def caesar(cipher_direction, start_text, shift_amount):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    # Encoding/decoding only alphabetic characters.
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {cipher_direction}d message is {end_text}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Making sure the shift number is in the alphabet range.
    shift = shift % 26

    caesar(cipher_direction=direction, start_text=text, shift_amount=shift)

    try_again = input("Do you want to do it again? Type 'Y' or 'N':\n").lower()
    if try_again == "n":
        should_continue = False
        print("Quitting the Caesar Cipher.")



# OLD CODE
# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")
#
# def decrypt(encrypted_text, shift_amount):
#     plain_text = ""
#     for letter in encrypted_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabet
#         plain_text += alphabet[new_position]
#     print(f"The decoded text is {plain_text}")
#
#
# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(encrypted_text=text, shift_amount=shift)