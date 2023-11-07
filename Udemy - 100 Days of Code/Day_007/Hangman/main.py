import random
# import os
from hangman_art import logo, stages
from hangman_words import word_list


# Faking a clear all...
def clear_screen():
    print('\n' * 100)


print(logo)
print("Welcome to a game of Hangman!")

chosen_word = random.choice(word_list)
word_len = len(chosen_word)
game_over = False
lives = 6

# Create blanks
display = []
for _ in range(word_len):
    display += "_"


print(f"{' '.join(display)}")

while not game_over:
    guess = input("Guess a letter: ").lower()

    # Calling clear_screen function
    clear_screen()

    # Check if letter is already guessed.
    if guess in display:
        print(f"You've already guessed {guess}")

    # Check guessed letter.
    for position in range(word_len):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Check if minus lives or lose.
    if guess not in display:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose!")

    # Join all elements in the list and turn into string.
    print(f"{' '.join(display)}")

    # Check if win.
    if "_" not in display:
        game_over = True
        print("You win!")

    print(stages[lives])

