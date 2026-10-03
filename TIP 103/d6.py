# 10/1/26 Stacks, Queues & OOP | Stacks, Queues, Two-Pointer

from collections import deque

"""
Stack (FILO)
stack = []
stack.append(), stack.pop(), stack[-1]

Queue (FIFO)
from collections import deque
q = deque(lst)
q.append(), q.popleft(), q[0]
"""

"""
Set1, #1
UNDERSTAND:
> Input:
> Output:
> Edge cases:
MATCH:
PLAN:
REVIEW:
EVALUATE: 
"""



# Problem 1: Blueprint Approval Process
# You are in charge of overseeing the blueprint approval process for various architectural designs. Each blueprint has a specific complexity level, represented by an integer. Due to the complex nature of the designs, the approval process follows a strict order:

# Blueprints with lower complexity should be reviewed first.
# If a blueprint with higher complexity is submitted, it must wait until all simpler blueprints have been approved.
# Your task is to simulate the blueprint approval process using a queue. You will receive a list of blueprints, each represented by their complexity level in the order they are submitted. Process the blueprints such that the simpler designs (lower numbers) are approved before more complex ones.

# Return the order in which the blueprints are approved.

# Plan:
# have a queue
# sort and loop through the sorted list and append to the queue
# add the sorted list from the queue to the result

def blueprint_approval(blueprints):
    queue = deque(sorted(blueprints))
    # sorted_bp = sorted(blueprints)
    # for blueprint in sorted_bp:
    #     queue.append(blueprint)

    result_order_approved = []

    while queue:
        cur_front = queue.popleft()
        result_order_approved.append(cur_front)

    return result_order_approved

# Example Usage:

print(blueprint_approval([3, 5, 2, 1, 4])) 
print(blueprint_approval([7, 4, 6, 2, 5])) 

# Example Output:

# [1, 2, 3, 4, 5]
# [2, 4, 5, 6, 7]

"""
Set1, #2
UNDERSTAND:
> Input: lst of integers
> Output: integer - representing the # of skyscrapers
> Edge cases: 
- [] -> 0, [one element] -> 1
MATCH:
queue 
PLAN:
- create a queue and initialize it with the lst
- create a variable to store previous popped element
- create variable to store number of skyscrapers
- while queue not empty:
- popleft()
- keep popping if prev is greater than current one until that's not the case. Then we increment skyscraper. 
- Update the prev popped with current popped
REVIEW:
EVALUATE: 
"""

def build_skyscrapers(floors):
    counter = 0 # 1
    prev_popped = -1
    q = deque(floors)
    
    while q:
        curr_popped = q.popleft()
        if prev_popped < curr_popped: # RDA: this should be >=, but let's see
            counter += 1
        prev_popped = curr_popped
    return counter

print(build_skyscrapers([10, 5, 8, 3, 7, 2, 9])) #4
print(build_skyscrapers([7, 3, 7, 3, 5, 1, 6])) #4 
print(build_skyscrapers([8, 6, 4, 7, 5, 3, 2])) #2

"""
Set1, #3
UNDERSTAND:
> Input: list of integers
> Output: integer - max area
> Edge cases:
- <= 1 element, return 0; 2 element, return the area
MATCH:
2 ptrs
PLAN:
left, right ptrs at ends of list
variable for tracking max area
while left < right:
    compute area and compare with max_area

REVIEW:
EVALUATE: 
"""

def max_corridor_area(segments):
    left = 0
    right = len(segments) - 1
    max_area = 0
    while left < right:
        distance = abs(left - right)
        local_area = min(segments[left], segments[right]) * distance
        if local_area > max_area:
            max_area = local_area
        if segments[left] < segments[right]:
            left += 1
        else:
            right -= 1
    return max_area

print(max_corridor_area([1, 8, 6, 2, 5, 4, 8, 3, 7])) 
print(max_corridor_area([1, 1])) 




