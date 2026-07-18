# 6/14/26: Recursion II & Divide & Conquer Algorithms

# Binary Search
nums = [1, 3, 5, 7, 9, 11]
target = 5

def binary_search(numbers, value):
  low = 0
  high = len(numbers) - 1
  while low <= high:
      mid = (low + high) // 2
      if numbers[mid] > value:
          high = mid - 1
      elif numbers[mid] < value:
          low = mid + 1
      else:
          return mid
  return None


def find_left(numbers, value):
  low = 0
  high = len(numbers) - 1
  index = -1
  while low <= high:
      mid = (low + high) // 2
      if numbers[mid] > value:
          high = mid - 1
      elif numbers[mid] < value:
          low = mid + 1
      else:
          index = mid
          high = mid - 1
          # low = mid + 1 for finding right 
  return index

nums = [1, 3, 3, 7, 9, 11]
target = 1
print(find_left(nums, target))

def binary_search_recursive(nums, target, low, high):
  if low > high:
    return -1
  mid = (low + high) // 2
  if nums[mid] > target:
    return binary_search_recursive(nums, target, low, mid-1)
  elif nums[mid] < target:
    return binary_search_recursive(nums, target, mid+1, high)
  else:
      return mid

print(binary_search_recursive(nums, target, 0, len(nums)-1))

   
   



"""
Set1, #1
UNDERSTAND:
> Input: list of strings
> Output: integer
> Edge cases:
MATCH:
Iteration and recursive implementation
PLAN:
Iteration: loop through the list
Recursion: 
- base case: arr = [] 
- recursive step: [] 
"""
def count_suits_iterative(suits):
  count = 0
  for suit in suits:
    count += 1
  return count

def count_suits_recursive(suits):
  if len(suits) == 0:
    return 0
  return 1 + count_suits_iterative(suits[1:])
# print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
# print(count_suits_recursive(["Mark I", "Mark II", "Mark III"]))

# 6/4/26

"""
Set1, #2
UNDERSTAND:
> Input: array of integers
> Output: integer
> Edge cases: [] -> 0
MATCH:
Recursive implementation
PLAN:
base case: [] -> 0
recursive step: return arr[1:]
"""
def sum_stones(stones):
  if len(stones) == 0:
    return 0
  return stones[0] + sum_stones(stones[1:])
# print(sum_stones([5, 10, 15, 20, 25, 30]))
# print(sum_stones([12, 8, 22, 16, 10]))

"""
Set1, #3
UNDERSTAND:
> Input: list of strings
> Output: integer
> Edge cases: [] -> 0
MATCH:
iterative and recursive solution
PLAN:
Iterative:
- Use a set to determine if suit has been seen before
Recursive:
- Need a global set to determine if suit has been seen before
"""

def count_suits_iterative(suits):
  suit_set = set()
  for suit in suits:
    if suit not in suit_set:
      suit_set.add(suit)
  return len(suit_set)

def count_suits_recursive(suits):
  if len(suits) == 0:
    return 0
  if suits[0] in suits[1:]:
    return count_suits_recursive(suits[1:])
  else:
    return 1 + count_suits_recursive(suits[1:])
  """
  O(n) cost for each recursive call, n times so O(n^2) run time
  O(n) space for list created using suits[1:] 
  """

# print(count_suits_iterative(["Mark I", "Mark/ I", "Mark III", "Mark I"]))
# print(count_suits_recursive(["Mark I", "Mark I", "Mark III"]))

"""
Set1, #4
UNDERSTAND:
> Input: integer
> Output: integer
> Edge cases: 0 -> 0, 1 -> 1
MATCH:
recursion
PLAN:
base case: 0-> 0, 1 -> 1
recursive step return F(n-1) + F(n - 2)
"""
def fibonacci_growth(n):
  if n == 0:
     return 0
  if n == 1:
     return 1
  return fibonacci_growth(n-1) + fibonacci_growth(n-2)
# print(fibonacci_growth(5))
# print(fibonacci_growth(8))

"""
Set1, #5
UNDERSTAND:
> Input: integer
> Output: integer
> Edge cases: 
MATCH:
recursion
PLAN:
base case: n == 1 return 4 
recursive return 4 * function(n-1)
"""
def power_of_four(n):
  if n < 0:
    return (1/4) * power_of_four(n+1)
  if n == 0:
     return 1
  if n == 1:
     return 4
  return 4 * power_of_four(n-1)

# print(power_of_four(-2))

"""
Set1, #6
UNDERSTAND:
> Input: list of integers
> Output: max integer
> Edge cases: [] -> 0
MATCH:
recursion
PLAN:
base case:
"""
# def strongest_avenger(strengths):
#    if len(strengths) == 1:
#       return strengths[0]
   
#    max_of_rest = strongest_avenger(strengths[1:])

#    if strengths[0] > max_of_rest:
#       return strengths[0]
#    else:
#       return max_of_rest
# run time is O(n^2), n recursive call, each creating an array of ~n size


def helper(strengths, index, max):
   if index == len(strengths):
      return max
   elif strengths[index] > max:
      max = strengths[index]
   return helper(strengths, index+1, max) 
# n recursive call, each cost o(1) operation. O(n) time.

def strongest_avenger(strengths):
   return helper(strengths, 0, strengths[0])

print(strongest_avenger([88, 92, 95, 99, 97, 100, 94]))
print(strongest_avenger([50, 75, 85, 60, 90]))


