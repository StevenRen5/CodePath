# V1 Q1
# Given a string, return True if it is a nesting of zero or more pairs of parentheses. Return False otherwise. 
# A valid pair of parentheses is defined as (). The input string will only contain the characters ( or ). 
# Your solution must be recursive.

# Evaluate the time and space complexity of your solution.

# Example Usage:

# # Example Input: "(())"
# Example Output:
# Expected Output: True

"""
U: 
recursive function
inputs: a str of ()
output: boolean value

P:
base case:
recursive step: 

"""

def is_nested(s):
    if s == "":
        return True
    
    if len(s) % 2 != 0:
        return False

    if s[0] == "(" and s[-1] == ")":
        return is_nested(s[1:-1])
    return True
s = "((()))"
# print(is_nested(s))

# V1 Q2
# Given a sorted list of integers containing only 0s and 1s, count the total number of 1’s in the array in O(log n) time.
# Example Usage:

'''
U:
    input: sorted list of ints
    output: int of # of 1's

P:
    edge case: test length of list to see if it contains any ints
    find the first position of 1 



'''

def count_ones(lst):
    if len(lst) == 0:
        return 0
    
    left = 0 
    right = len(lst) - 1
    answer = -1
    while left <= right:
        middle = (left+right) // 2

        if lst[middle] == 0:
            left = middle + 1 # everything from middle to left is 0, so we move left by middle + 1 
        elif lst[middle] == 1:
            answer = middle
            right = middle - 1 # we known middle is 1, but there could be a 1 earlier before middle
    return len(lst) - answer

# print(count_ones([0, 0, 0, 0, 1, 1, 1]))
# Example Output: 3
# Example Input: [0, 0, 1, 1, 1, 1, 1]
# Example Output: 3

# V1 Q3
def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    middle = (left+right)//2

    if len(nums) == 1:
        if nums[0] != target:
            return -1 

    if nums[middle] == target:
        return middle
    elif nums[middle] > target:
        # return binary_search(nums[left:middle-1], target)
    else:
        # return binary_search(nums[middle+1:right], target)

nums = [1, 3, 5, 7, 9, 11, 13, 15]
target = 11
print(binary_search(nums, target))