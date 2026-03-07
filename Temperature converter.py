#Program 7: Temperature converter (Celsius to Fahrenheit and vice versa)


# Show the user their options
print("\nTemperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    # Convert Celsius to Fahrenheit
    # Formula: F = (C * 9/5) + 32
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    # int() removes the decimal point to match expected output
    print(f"{int(celsius)}°C is {int(fahrenheit)} in Fahrenheit")
    # on 3wschools I learned that when we set values (such as celsius and fahrenheit, we can use it to check if it matches a secondary value)
elif choice == "2":
    # Convert Fahrenheit to Celsius
    # Formula: C = (F - 32) * 5/9
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{int(fahrenheit)}°F is {int(celsius)} in Celsius")
    # 3wschools states that float can be used to represent decimals and fractional values

else:
    print("Invalid choice!")