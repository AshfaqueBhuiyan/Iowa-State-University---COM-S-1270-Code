# Ash Bhuiyan                                   07-16-2025
# Lab #7 - This program checks if a list of strings forms a palindrome.

def listInput():
    inputList = []
    while True:
        user_input = input("Enter a string (* to stop): ")
        if user_input == "*":
            break
        inputList.append(user_input)
    return inputList

def palindromeList(lst):
    length = len(lst)
    for i in range(length // 2):
        if lst[i] != lst[length - 1 - i]:
            return False
    return True

def main():
    palList = listInput()
    print("Is the list palindromic?", palindromeList(palList))

if __name__ == "__main__":
    main()
