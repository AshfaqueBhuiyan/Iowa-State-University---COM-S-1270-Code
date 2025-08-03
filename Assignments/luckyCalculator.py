# Ash Bhuiyan                                                                       06-27-2025
# Assignment #2
# 
# A calculator using user input to practice mathematical operations, functions, and the random module.

#Introduction
print()
print("Lucky Calculator!")
print()
print("By: Ash Bhuiyan")
print("[COM S 1270 A]")
print()

import random

# Function to get an integer input from the user
def get_integer_input(prompt):
    value = int(input(prompt)) 
    return value

# Function for Addition operation
def add(a, b):
    return a + b

# Function for Subtraction operation
def subtract(a, b):
    return a - b

# Function for Multiplication operation
def multiply(a, b):
    return a * b

# Function for Division operation
def divide(a, b):
    if b == 0:
        print("ERROR in / Function: b = 0")
        b = 1
    return a / b

# Function for Integer Division operation
def integer_divide(a, b):
    if b == 0:
        print("ERROR in // Function: b = 0")
        b = 1
    return a // b

# Function for Modulus Operation
def modulus(a, b):
    if b == 0:
        print("ERROR in % Function: b = 0")
        b = 1
    return a % b

# Function for Exponentiation operation
def exponentiate(a, b):
    return a ** b

# Function to calculate a Lucky number
def lucky_number(a, b):
    if a < b:
        low = a
        high = b
    else:
        low = b
        high = a
    return random.randint(low, high + 1)

# Main function to determine user choice
print("What would you like to do?\n")
print("[c]alculator, [l]ucky number, [q]uit: ", end='')
choice = input().strip().lower()
print()

if choice == 'c':
    operation = input("Please Choose a Calculation [+], [-], [*], [/], [//], [%], [**]: ").strip()

    if operation not in ('+', '-', '*', '/', '//', '%', '**'):
        print('ERROR: You must enter either "+", "-", "*", "/", "//", "%", or "**"')
        print()
    else:
        left_operand = get_integer_input("Please Enter An Integer: ")
        right_operand = get_integer_input("Please Enter An Integer: ")
        if operation == '+':
            answer = add(left_operand, right_operand)
        elif operation == '-':
            answer = subtract(left_operand, right_operand)
        elif operation == '*':
            answer = multiply(left_operand, right_operand)
        elif operation == '/':
            answer = divide(left_operand, right_operand)
        elif operation == '//':
            answer = integer_divide(left_operand, right_operand)
        elif operation == '%':
            answer = modulus(left_operand, right_operand)
        elif operation == '**':
            answer = exponentiate(left_operand, right_operand)
        print(f"The result of your calculation was: {answer}")
        print()

elif choice == 'l':
    a = get_integer_input("Please Enter An Integer: ")
    b = get_integer_input("Please Enter An Integer: ")
    answer = lucky_number(a, b)
    print(f"Your lucky number is: {answer}")
elif choice == 'q':
    print("Goodbye!")
    print()
else:
    print("ERROR: I did not understand your input... Please try again...")
    print()
