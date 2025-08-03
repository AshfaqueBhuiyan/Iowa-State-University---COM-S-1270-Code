# Ash Bhuiyan                                       06-29-2025
# Lab 3 - Functional version of finding area of a rectangle from user input.

# CITATION - URL: https://www.cuemath.com/measurement/area-of-rectangle/
# CITATION - Author: Cuemath
# CITATION - Date Accessed: 06-24-2025

def areaOfRectangle(base, height):
    return base * height

def main():
    base = int(input("Enter value 'base': "))
    height = int(input("Enter value 'height': "))
    answer = areaOfRectangle(base, height)
    print(f"The rectangle's area = {answer} square units.")

if __name__ == "__main__":
    main()
