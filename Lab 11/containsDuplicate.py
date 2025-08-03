# Ash Bhuiyan                  08-03-2025
# Lab #11 - solution for "containsDuplicates"

def contains_duplicate(nums):
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False

# Tests
if __name__ == "__main__":
    print(contains_duplicate([1, 2, 3, 1]))
    print(contains_duplicate([1, 2, 3, 4]))
    print(contains_duplicate([1, 1, 1, 3, 3, 4, 2, 4, 2]))
