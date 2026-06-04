# 6/4/26

# Set 1, #1
"""
UNDERSTAND:
> Input:
> Output:
> Edge cases:

PLAN:

1. Split the sentence on spaces
2. Accumulate in reverse order to new array

"""

def reverse_sentence(sentence):
    list_words = sentence.split(" ")
    reversed= ""

    for i in range (len(list_words)-1, -1, -1):
        reversed += list_words[i]
        reversed += " "
    return reversed

sentence = "tubby little cubby all stuffed with fluff"
print(reverse_sentence(sentence))

# Set 1, #2
"""
UNDERSTAND:
> Input: list of integers
> Output: an integer
> Edge cases: 
  - empty list -> -1
  - 2 values -> -1

PLAN:
1. Create two variables, one to store max value, another for min value
2. Go through list to find those values
2. Go through list again to determine there's a value that's neither max or min to be returned
"""
def goldilocks_approved(nums):
    if len(nums) == 0 or len(nums) == 1 or len(nums) == 2:
        return -1
    max_val = nums[0]
    min_val = nums[0]
    for num in nums:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num

    for num in nums:
        if num != max_val and num != min_val:
            return num
    return -1
nums = [3, 2, 1, 4]
print(goldilocks_approved(nums))

nums = [1, 2]
print(goldilocks_approved(nums))

nums = [2, 1, 3]
print(goldilocks_approved(nums))

# set 1, #3

"""
UNDERSTAND:
> Input: list of integars
> Output: list integars
> Edge cases:

PLAN:

1. Split the sentence on spaces
2. Accumulate in reverse order to new array

"""
def delete_minimum_elements(hunny_jar_sizes):
    res = []
    while len(hunny_jar_sizes) > 0:
        res.append(min(hunny_jar_sizes))
        hunny_jar_sizes.remove(min(hunny_jar_sizes))
    return res

hunny_jar_sizes = [5, 3, 2, 4, 1]
print(delete_minimum_elements(hunny_jar_sizes))

hunny_jar_sizes = [5, 2, 1, 8, 2]
print(delete_minimum_elements(hunny_jar_sizes))

def sum_of_digits(num):
    total_num = 0

    while num > 0:
        total_num += num % 10
        num //= 10
    return total_num
print(sum_of_digits(423))  


""""
UNDERSTAND:
> Input: list of operations
> Output: final value of tigger variable
> Edge cases: Invalid operations > Error 

PLAN:

1. Loop through list operations
    1.1 Check if operation is valid.
         If valid:
        1.2 Perform each operation sequentially
        If not valid:
        Throw error.
2. Accumulate in reverse order to new array

"""

def final_value_after_operations(operations):
    tigger = 1
    valid_operations = {"trouncy","flouncy", "bouncy", "pouncy"}
    for operation in operations:
        if operation in valid_operations:
            if operation == "flouncy" or operation == "bouncy":
                tigger+=1
            else:
                tigger-=1
        else:
            print(f"Error: Invalid operation - {operation}" )
    return tigger

