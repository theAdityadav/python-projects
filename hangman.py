import random

# List of words to guess from
words = ["apple", "banana", "cherry", "date", "elderberry"]

# Choose a random word from the list
word = random.choice(words)

# Create a list to store the guessed letters
guessed = ["_"] * len(word)

# Create a set to store the incorrect guesses
incorrect_guesses = set()

# The number of chances the player has
chances = 6

print("Welcome to Hangman!")
print(" ".join(guessed))

while chances > 0:
    # Get the player's guess
    guess = input("Guess a letter: ")

    # Check if the guess is in the word
    if guess in word:
        # Reveal the correctly guessed letter
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
        print(" ".join(guessed))
    else:
        # Add the incorrect guess to the set
        incorrect_guesses.add(guess)
        chances -= 1
        print(f"Incorrect! You have {chances} chances left.")

    # Check if the player has won
    if "_" not in guessed:
        print("Congratulations! You won!")
        break

# If the player has lost, reveal the word
if chances == 0:
    print(f"Game over! The word was {word}.")