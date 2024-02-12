"""Triangle Classifier:
Write a program that classifies a triangle based on its side lengths.


3 Input

side 1, side 2 and side 3

output - Eq, Iso, Scalene -

Eq. = side 1 == side 2 = side 3"""

side1 = int(input("Enter side1: "))
side2 = int(input("Enter side2: "))
side3 = int(input("Enter side3: "))

if side1 == side2 == side3:
    print("Triangle is equilateral")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("Triangle is isosceles")
else:
    print("Triangle is scalene")