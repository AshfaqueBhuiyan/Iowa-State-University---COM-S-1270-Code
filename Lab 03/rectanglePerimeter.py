# Ash Bhuiyan                                       06-29-2025
# Lab 3 - Functional version of finding perimeter of a rectangle from user input.

# CITATION - URL: https://www.mometrix.com/academy/calculating-the-perimeter-of-rectangles/
# CITATION - Author: Mometrix
# CITATION - Date Accessed: 06-24-2025

def rectanglePerimeter(length, width):
    return 2 * (length + width)

def main():
    length = int(input("Enter value 'length': "))
    width = int(input("Enter value 'width': "))
    answer = rectanglePerimeter(length, width)
    print(f"The perimeter = {answer} units.")

if __name__ == "__main__":
    main()
