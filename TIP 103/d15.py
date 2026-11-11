# 11/10 Greedy Algorithm

"""
Set1, #1
UNDERSTAND:
> Input: intervals - list of list, where list ele is [start, end]
> Output: integer - min number of requests canceled
> Edge cases:

MATCH:
Sort, then scan
Sort the items by a key, such as end time or size. Then go through the items in order and decide whether to take each one

PLAN:

prev_end = 0
canceled = 0
sort list - using end time from least to greatest 

for start, end in intervals:
    if start < prev_end:
        canceled += 1
    else:
        prev_end = end

return canceled



REVIEW:
EVALUATE: 
sort -> O(nlogn) time complexity
O(1) space complexity
"""

def erase_overlap_intervals(intervals):
  canceled = 0

  # intervals = sorted(intervals, key=lambda x: x[1]) 
  intervals.sort(key=lambda x: x[1])

  prev_end = intervals[0][1]

  for start, end in intervals[1:]:
      if start < prev_end: 
            canceled += 1
      else:
          prev_end = end

  return canceled

# [1, 2],[2,3],[1,3], [3,4]
print(erase_overlap_intervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
print(erase_overlap_intervals([[1, 2], [1, 2], [1, 2]]))
print(erase_overlap_intervals([[1, 2], [2, 3]]))

"""
Set1, #2
UNDERSTAND:
get from beginning to end of array
determine starting point so you'll have enough gas to make it all the way around (loop)

> Input: 
- gas - list of fuel available at station gas[i]
- cost - cost of fuel to drive form i to station i + 1
> Output: int - -1 for impossible or the starting point i

> Edge cases:
MATCH:
"Track the Best So Far"
|_Keep one or two values that you update at every step of a single pass, 
  such as the farthest index you can reach or the sum so far.

PLAN:

greedy way:
initialize start
initialize 
- net = gas[i] - cost[i], if net < 0, we must move i to i+1

REVIEW:
EVALUATE: 
"""

def can_complete_circuit(gas, cost):
  start = 0
  net = 0
  for i in range(len(gas)):
    net = gas[i] - cost[i]

    if net < 0:
      start = i + 1


print(can_complete_circuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
print(can_complete_circuit([2, 3, 4], [3, 4, 3]))

[1, 2, 3, 4, 5][4, 3, 2, 1]