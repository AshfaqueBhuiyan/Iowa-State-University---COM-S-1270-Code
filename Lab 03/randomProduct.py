# Ash Bhuiyan                                       06-29-2025
# Lab 3 - Multiplication of random integers.

# CITATION - URL: https://runestone.academy/ns/books/published/iowastateuniversity_thinkcspy_summer25/PythonModules/Therandommodule.html
# CITATION - Source: Runestone
# CITATION - Date Accessed: 06-29-2025

import random

def randomProduct(a, b, c):
    product = 1
    for i in range(a):
        rand_num = random.randrange(b, c + 1)
        product *= rand_num
    return product

def main():
    a = int(input("Enter how many random numbers to multiply (a): "))
    b = int(input("Enter lower bound of range (b): "))
    c = int(input("Enter upper bound of range (c): "))
    answer = randomProduct(a, b, c)
    print("The answer is:", answer)

if __name__ == "__main__":
    main()
