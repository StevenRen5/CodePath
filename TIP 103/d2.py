# 9/17/26: Foundations

# Instructor demo
# Fuel Stop Optimizer
"""
You are planning a cross-country road trip in an electric vehicle (EV). You are currently at the start of a long highway (index 0) and your goal is to reach the final charging hub located at the last index of the array.

Each element in the integer array battery_life represents your maximum driving range (in miles/indices) from that particular position. For example, if you are at battery_life[i] = 3, you can "jump" or drive to any index from i + 1 up to i + 3.

Return true if you can reach the final charging hub, or false otherwise.

Example 1:

Input: battery_life = [2, 3, 1, 1, 4]
Output: true
Explanation: Start at index 0 (range = 2). You can drive to index 1. At index 1, your range is 3. You can drive directly to the last index (index 4).
Example 2:

Input: battery_life = [3, 2, 1, 0, 4]
Output: false
Explanation: No matter what, you will always arrive at index 3. However, its range is 0, which means you're stuck at a "dead" charging station and can never reach the final hub.
Constraints:

1 <= battery_life.length <= 10^4
0 <= battery_life[i] <= 10^5
"""

"""
Understand:
input: list
Output: boolean
edge cases:
- [] -> true

Plan: 
create a max distance var
go through battery_life:
  update the max distance we can travel based on the amount of fuel available at each stop

Review:
O(n) run time
O(1) space


 [2, 3, 1, 1, 4]
"""

def can_reach_destination(battery_life):
  # track max distance
  max_reach = 0 

  # note: we're not saying jump to i. We're calculating if i is reachable based on the max_reach we have
  for i in range(len(battery_life)):
    if i > max_reach:
      return False
    max_reach = max(max_reach, i+battery_life[i])

  # if the max distance takes us to the end of the array or further, then we return true (othwerwise false)
  if max_reach >= len(battery_life) - 1:
    return True
  return False

  
