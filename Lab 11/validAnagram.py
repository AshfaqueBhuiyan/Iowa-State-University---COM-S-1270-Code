# Ash Bhuiyan                  08-03-2025
# Lab #11 - solution for "validAnagram"

def is_anagram(s, t):
    if len(s) != len(t):
        return False

    count1 = {}
    count2 = {}

    for c in s:
        if c in count1:
            count1[c] += 1
        else:
            count1[c] = 1

    for c in t:
        if c in count2:
            count2[c] += 1
        else:
            count2[c] = 1

    return count1 == count2

# Tests
if __name__ == "__main__":
    print(is_anagram("anagram", "nagaram"))
    print(is_anagram("rat", "car"))
    print(is_anagram("hello", "lleho"))
    