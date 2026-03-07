# Ask the user to enter a year
year = int(input("\nEnter a year: "))

# Leap year rules (from the Gregorian calendar):
# Rule 1: Divisible by 4 -> leap year
# Rule 2: BUT if also divisible by 100 -> NOT a leap year
# Rule 3: UNLESS also divisible by 400 -> IS a leap year
# Again, we use the "divisible by" trick to only include certain numbers, and exclude numbers we dont want (Percent in 3wschools)

if (year % 400 == 0):
    # Divisible by 400 -> always a leap year
    print(True)
elif (year % 100 == 0):
    # Divisible by 100 but NOT 400 -> not a leap year
    print(False)
elif (year % 4 == 0):
    # Divisible by 4 but NOT 100 -> leap year
    print(True)
else:
    # Not divisible by 4 at all -> not a leap year
    print(False)