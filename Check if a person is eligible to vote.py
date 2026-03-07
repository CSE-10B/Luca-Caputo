# Program 4: Check if a person is eligible to vote


# Ask for the person's age
age = int(input("\nEnter your age: "))

# In most countries, you must be 18 or older to vote
if age >= 18:
    print("You are eligible to vote!")
else:
    print("You arent eligible to vote yet.")

