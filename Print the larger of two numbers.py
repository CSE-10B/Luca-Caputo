#Program 6: Print the larger of two numbers


# Take two numbers from the user
num1 = float(input("\nEnter the first number: "))
num2 = float(input("Enter the second number: "))
# num1 and num2 just means number 1 and number 2, it can be used to compare quantities
# Compare the two numbers
if num1 > num2:
    print(f"The larger number is: {num1}")
elif num2 > num1:
    print(f"The larger number is: {num2}")
else:
    # This handles the case where both numbers are equal
    print("Both numbers are equal!")
    # >,< are greater and less than symbols it can be used to determine which quantity is larger than another