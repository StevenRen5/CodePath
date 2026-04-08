# 4/7/26 Recursion & Divide & Conquer
# base ca

# Demo 
def recursive_sum(num):
    if num <= 1: # base case - instance when a recursive call returns a value rather than calling itself
        return num
    return num + recursive_sum(num - 1) # recursive step is when we call the function

# Example usage
result = recursive_sum(5)
# print( result)  # Output will be 15

# V1 Q1
def repeat_hello(n):
	if n > 0:
		print("Hello")
		repeat_hello(n - 1)
		
# repeat_hello(5)

#for each element in range(n):
#print "Hello"

def repeathello(n):
    for i in range(n):
          print("Hello")

# repeathello(5)

# V1 Q2
"""
U: 
Recursive function 
Factorial computation

P:
Base case: if we get n = 1, return n
Recursive step: n * factorial(n-1)
"""
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

# print(factorial(5))

# V1 Q3

"""
input: list
goal: sum every i in list
function: recursive

Base case: list is empty
recursive step: 
- sum first element of list + slice list (exclude first element) [1:]
"""

[1]

def sum_list(lst):
    if not lst:
         return 0
    else:
         return lst[0] + sum_list(lst[1:]) 

lst = [1,2,3,4,5]
# print(sum_list(lst))

# V1 Q4
"""
U: 
recursive function
find if n is a power of 2
Return a boolean value
Divisible 2 if n is a power of 2


P:
recursive step: keep dividing n / 2 

"""

def is_power_of_two(n):
    if n == 1:
        return True
    elif n % 2 != 0:
        return False
    return is_power_of_two(n/2)

# print(is_power_of_two(16)) #  true
# print(is_power_of_two(18)) #  false
# print(is_power_of_two(1)) # true (actually false)

# V1 Q5

"""


"""

def binary_search(lst, target):
	# Initialize a left pointer to the 0th index in the list
	# Initialize a right pointer to the last index in the list
    left_pointer = 0
    right_pointer = len(lst) - 1 
	
	# While left pointer is less than right pointer:
		# Find the middle index of the array
    while left_pointer < right_pointer:

        if right_pointer - left_pointer 
        left_pointer += 1
        right_pointer -= 1
    
        middle_index = left_pointer - 1
        if target == lst[middle_index]:
            return middle_index
        
        elif lst[middle_index] < target:
            left_pointer = middle_index
            right_pointer = len(lst) - 1

        else:
            left_pointer = 0
            right_pointer = middle_index

		# If the value at the middle index is the target value:
			# Return the middle index
        
		# Else if the value at the middle index is less than our target value:
			# Update pointer(s) to only search right half of the list in next loop iteration
		# Else
			# Update pointer(s) to only search left half of the list in next loop iteration
	
	# If we search whole list and haven't found target value, return -1

#.    0   1 2. 3.  4  5. 6   7
lst = [1, 3, 5, 7, 9, 11, 13, 15]
lst = [1, 3, 5, 7, 9, 11]