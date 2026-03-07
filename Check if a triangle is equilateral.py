# Program 5: Check if a triangle is equilateral

# An equilateral triangle has ALL THREE sides equal
side1 = float(input("\nEnter side 1 of the triangle: "))
side2 = float(input("Enter side 2 of the triangle: "))
side3 = float(input("Enter side 3 of the triangle: "))

# Check if all three sides are the same length
if side1 == side2 == side3:
    print("This IS an equilateral triangle!")
else:
    print("This is NOT an equilateral triangle.")