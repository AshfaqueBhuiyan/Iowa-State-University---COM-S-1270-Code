# Ash Bhuiyan                                       06-29-2025
# Lab 3 - Functional version of finding the area of a circle from radius.

# CITATION - URL: https://www.cuemath.com/measurement/area-of-circle/
# CITATION - Author: Cuemath
# CITATION - Date Accessed: 06-24-2025

import math

def areaOfCircle(radius):
    return math.pi * (radius ** 2)

def main():
    radius = int(input("Enter value 'radius': "))
    answer = areaOfCircle(radius)
    print(f"That circle's area = {answer:.3f} square units.")

if __name__ == "__main__":
    main()
