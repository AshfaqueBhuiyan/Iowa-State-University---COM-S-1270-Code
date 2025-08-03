# Ash Bhuiyan                  08-01-2025
# Lab #11 - This program checks if a given string is a palindrome using two methods:
# an iterative approach and a recursive one. It prints True or False accordingly.

def isPalindromeIterative(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def isPalindromeRecursive(s):
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return isPalindromeRecursive(s[1:-1])

def main():
    s = input("Enter a word or phrase: ").strip().lower().replace(" ", "")

    print("\n--- Iterative Check ---")
    result1 = isPalindromeIterative(s)
    print("Is Palindrome (Iterative)?", result1)

    print("\n--- Recursive Check ---")
    result2 = isPalindromeRecursive(s)
    print("Is Palindrome (Recursive)?", result2)

if __name__ == "__main__":
    main()
