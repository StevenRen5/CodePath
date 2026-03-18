# 3/17 2 pointers

# Instructor demo
# Problem: Given a string s, determine if it can become a palindrome by removing at most one character.
# A palindrome is a word, phrase, or sequence that reads the same backward as forward.
# Input: s = "abca"
# Output: True

# Plan
"""
1. Given a string
2. Implement the classic plaindrome sol 
3. we need to helper function 
4. we will need to allow for ONLY one invalid character. "aba"
    use a helper function
5. return result
"""

def class_palindrome(s, left, right):
    while (left < right):
        if (s[left] == s[right]):
            left+=1
            right-=1
        else:
            return False
    return True

def valid_palindrome(s):
    left = 0
    right = len(s) - 1

    """
    iterate through letters, if somrthing is wrong, we do our scoot where only 2 of the two choices needs to be valid/
    """
    while (left < right):
        if (s[left] == s[right]):
            left += 1
            right -= 1
            continue
        else:
            return class_palindrome(s, left+1, right) or class_palindrome(s, left, right+1)
            # we will allow for scooting ONCE.
            # we will perform normal palindrome checking on both segments
    return True
        
# V1 Q1
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# V2 Q2

def reverse_list(lst):
    left = 0
    right = len(lst) - 1
    while left < right:
        temp = lst[left]
        lst[left] = lst[right]
        lst[right] = temp
        left += 1
        right -= 1

input = [1,2,3,4,5]
reverse_list(input)
print(input)
#               0   1 2  3  4
# Example Input: [1, 2, 3, 4, 5]
# Example Output: [5, 4, 3, 2, 1]

# V1 Q3

# V1 Q4
def sort_array_by_parity(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        if nums[left] % 2 == 1 and nums[right] % 2 == 0:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
        left += 1
        right -= 1
    return nums

# V1 Q5
def is_palindrome(word):
    left = 0
    right = len(word) - 1
    while left < right:
        if word[left] != word[right]:
            return False
    return True

def first_palindrome(words):
    for word in words:
        if (is_palindrome(word)):
            return word
    return ""










   

