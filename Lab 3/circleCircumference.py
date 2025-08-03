# Ash Bhuiyan                                       06-29-2025
# Lab 3 - Functional version of calculating circumference of a circle from radius.

# CITATION - URL: https://www.omnicalculator.com/math/circumference
# CITATION - Authors: Bogna Szyk and Mateusz Mucha
# CITATION - Date Updated: 05-08-2025
# CITATION - Date Accessed: 06-24-2025

import math

def circleCircumference(radius):
    return 2 * math.pi * radius

def main():
    radius = int(input("Enter value 'radius': "))
    answer = circleCircumference(radius)
    print(f"The circumference = {answer:.3f} units.")

if __name__ == "__main__":
    main()
