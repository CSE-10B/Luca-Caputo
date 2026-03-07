# Program 10: Number Guessing Game (1 to 9)

# The secret number the user has to guess
secret_number = 3

print("\n Guess the Number (between 1 and 9)")

# This loop keeps running UNTIL the user guesses correctly
# Unfortunately, the secret number is always 3, I can not figure out how to make that value interchangable automatically
while True:
    # Ask the user for their guess
    guess = int(input("Take a guess: "))

    # Check if the guess is correct
    if guess == secret_number:
        print("Well guessed!")
        break  # Exit the loop once they get it right
    else:
        print("Wrong guess, try again.")
