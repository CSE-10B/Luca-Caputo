# Program 2: Check if a number is even or odd


# Ask the user to enter a number
# int() converts the text input into a whole number
number = int(input("\nEnter a number: "))

# Even numbers have no remainder when divided by 2
# so this can actually tell us if the number is even, then theres no remainder
# The % symbol gives us the remainder
if number % 2 == 0:
    print(f"{number} is Even.")
else:
    print(f"{number} is Odd.")