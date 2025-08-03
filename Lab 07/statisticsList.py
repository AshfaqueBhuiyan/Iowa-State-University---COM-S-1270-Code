# Ash Bhuiyan                                        07-16-2025
# Lab #7 - This program generates a random list and computes mean and median.

import random

def generateInput():
    size = random.randint(200, 500)
    return [random.randint(1, 2000) for _ in range(size)]

def findMean(lst):
    total = 0
    for num in lst:
        total += num
    return total / len(lst)

def findMedian(lst):
    lst.sort()
    n = len(lst)
    mid = n // 2
    if n % 2 == 1:
        return lst[mid]
    else:
        return (lst[mid - 1] + lst[mid]) / 2

def main():
    randList = generateInput()
    mean = findMean(randList)
    median = findMedian(randList)
    print("Mean: {0:.2f} Median: {1:.2f}".format(mean, median))

if __name__ == "__main__":
    main()
