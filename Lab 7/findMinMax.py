# Ash Bhuiyan                                     07-16-2025
# Lab #7 - This program collects a list of integers and finds the minimum and maximum values.

# CITATION - URL: https://www2.math.upenn.edu/~ancoop/1070/section-28.html
# CITATION - Author: MATH 1070: Calculus Group
# CITATION - Date Accessed: 07-16-2025

def listInput():
    inputList = []
    while True:
        user_input = input("Enter an integer (* to stop): ")
        if user_input == "*":
            break
        inputList.append(user_input)
    return inputList

def findMin(lst):
    min_val = int(lst[0])
    for num in lst:
        val = int(num)
        if val < min_val:
            min_val = val
    return min_val

def findMax(lst):
    max_val = int(lst[0])
    for num in lst:
        val = int(num)
        if val > max_val:
            max_val = val
    return max_val

def main():
    numbers = listInput()
    numbers = [int(x) for x in numbers]
    print("Minimum value:", findMin(numbers))
    print("Maximum value:", findMax(numbers))

if __name__ == "__main__":
    main()
