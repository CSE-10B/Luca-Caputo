# Program 8: Weird or Not Weird

# Take an integer from the user
n = int(input("\nEnter an integer: "))

# Check the conditions one by one
if n % 2 != 0:
    # n is odd (has a remainder when divided by 2)
    print("Weird")
elif 2 <= n <= 5:
    # n is even AND between 2 and 5 (inclusive)
    print("Not Weird")
elif 6 <= n <= 20:
    # n is even AND between 6 and 20 (inclusive)
    print("Weird")
elif n > 20:
    # n is even AND greater than 20
    print("Not Weird")
    # Different instances where different number values can be weird or not weird depending on where they are on the number line