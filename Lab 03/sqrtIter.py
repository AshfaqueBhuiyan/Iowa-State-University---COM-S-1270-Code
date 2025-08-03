# Ash Bhuiyan                                       06-29-2025
# Lab 3 - Finding square root using the iteration method.

# CITATION - URL: https://www.cuemath.com/algebra/square-root-of-2/
# CITATION - Author: Cuemath
# CITATION - Date Accessed: 06-28-2025

def sqrtIter(x, iterations):
    y = (x + 1) / 2  # initial guess
    for i in range(iterations):
        y = ((x / y) + y) / 2
    return y

def main():
    x = int(input("Enter number to approximate square root of (x): "))
    iterations = int(input("Enter number of iterations to run: "))
    answer = sqrtIter(x, iterations)
    print(f"The answer is: {answer:.5f}")

if __name__ == "__main__":
    main()
