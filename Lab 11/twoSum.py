# Ash Bhuiyan                  08-01-2025
# Lab #11 - This program solves the classic Two Sum problem using both brute-force loops
# and a dictionary-based method. It also includes versions that find all matching index pairs.

def twoSumLoops(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

def twoSumDict(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

def twoSumLoopsAll(nums, target):
    results = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                results.append([i, j])
    return results

def twoSumDictAll(nums, target):
    results = []
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            for j in seen[complement]:
                results.append([j, i])
        if num in seen:
            seen[num].append(i)
        else:
            seen[num] = [i]

    return results

def main():
    nums = [2, 7, 11, 15, 3, 6]
    target = 9

    print("Input List:", nums)
    print("Target:", target)

    print("\n--- One Match (Brute Force) ---")
    result1 = twoSumLoops(nums, target)
    print("Indices:", result1)

    print("\n--- One Match (Dictionary) ---")
    result2 = twoSumDict(nums, target)
    print("Indices:", result2)

    print("\n--- All Matches (Brute Force) ---")
    result3 = twoSumLoopsAll(nums, target)
    print("All Pairs:", result3)

    print("\n--- All Matches (Dictionary) ---")
    result4 = twoSumDictAll(nums, target)
    print("All Pairs:", result4)

if __name__ == "__main__":
    main()
