#Program 3: Print the day based on number input


# Ask the user for a number between 1 and 7
day_number = int(input("\nEnter a number (1-7): "))

# int means integer, like a number
# Each number maps to a day of the week
# elis means else if according to 3wschools, and it can be used to sequence multiple "if" chains
if day_number == 1:
    print("Monday")
elif day_number == 2:
    print("Tuesday")
elif day_number == 3:
    print("Wednesday")
elif day_number == 4:
    print("Thursday")
elif day_number == 5:
    print("Friday")
elif day_number == 6:
    print("Saturday")
elif day_number == 7:
    print("Sunday")
else:
    # If they typed something outside 1-7, let them know
    print("Invalid input, please enter a number between 1 and 7.")