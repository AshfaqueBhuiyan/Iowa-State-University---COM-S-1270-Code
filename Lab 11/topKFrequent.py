# Ash Bhuiyan                  08-03-2025
# Lab #11 - solution for "topKFrequent"

def top_k_frequent(nums, k):
    freq = {}
    for n in nums:
        if n in freq:
            freq[n] += 1
        else:
            freq[n] = 1

    buckets = [[] for _ in range(len(nums) + 1)]

    for key in freq:
        count = freq[key]
        buckets[count].append(key)

    result = []

    for i in range(len(buckets) - 1, -1, -1):
        for val in buckets[i]:
            result.append(val)
            if len(result) == k:
                return result

# Tests
if __name__ == "__main__":
    print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))
    print(top_k_frequent([1], 1))
    print(top_k_frequent([4, 4, 4, 5, 5, 6], 1))
