# 6/18/26: Big(O) | Stacks, Queues, and Two Pointer

from collections import deque

"""
Set1, #1
UNDERSTAND:
> Input: list of strings 
> Output: a list 
> Edge cases:
MATCH: stack 
PLAN:
create two stacks - one storing most recently canceled and one storing the schedule 
go through each item and check for each keyword 
"""

def manage_stage_changes(changes):
  schedule = []
  canceled = []

  for situation in changes:
    if "Schedule" in situation:
      schedule.append(situation[-1])
    elif "Cancel" in situation:
      if schedule:
        canceled.append(schedule.pop())
    else:
      if canceled:
        schedule.append(canceled.pop())
  return schedule

print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) 

"""
Set1, #2
UNDERSTAND:
> Input: list of tuples
> Output: list 
> Edge cases:
MATCH:  
queue
PLAN:
sort requests
create a new list and pop from requests to add in list
"""
def process_performance_requests(requests):
  requests.sort()
  requests.reverse()
  queue = deque(requests)
  ret_list = []
  while queue:
    ret_list.append(queue.popleft()[1])
  return ret_list

# print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
# print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
# print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))

"""
Set1, #3
UNDERSTAND:
> Input: list of integers
> Output: integer
> Edge cases:
  - [] -> 0
  - len(lst) = 1 --> num[0]
MATCH:
stack
PLAN:
loop through each num 
  append to stack
Until stack is empty:
  pop and add to total
"""
def collect_festival_points(points):
  stack = []
  total = 0
  for point in points:
    stack.append(point)
  while stack:
    total += stack.pop()
  return total

# print(collect_festival_points([5, 8, 3, 10])) 
# print(collect_festival_points([2, 7, 4, 6])) 
# print(collect_festival_points([1, 5, 9, 2, 8]))

"""
Set1, #4
UNDERSTAND:
> Input: list 
> Output:
> Edge cases:
MATCH:
stack
PLAN:
go through each element
  if it's a num append to stack
  if it's a "back" & stack isn't empty, pop from it
"""
def booth_navigation(clues):
  stack = []
  for clue in clues:
    if clue == "back":
      if stack:
        stack.pop()
    else:
      stack.append(clue)
  return stack

clues = [1, 2, "back", 3, 4]
# print(booth_navigation(clues)) 

clues = [5, 3, 2, "back", "back", 7]
# print(booth_navigation(clues)) 

clues = [1, "back", 2, "back", "back", 3]
# print(booth_navigation(clues)) 

