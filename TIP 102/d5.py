# 6/16 - Stack, queue, two ptrs, big O
from collections import deque

# stack
stack = []
stack.append(1)
stack.append(2)
# print(stack)
# popped = stack.pop()
# print(stack, popped)
# print(stack[-1])

# queue
from collections import deque
queue = deque()
queue.append("Bob")
queue.append("John")
# print(queue)
firstpopped = queue.popleft()
# print(queue)

"""
Set1, #1
UNDERSTAND:
> Input: str
> Output: boolean
> Edge cases:
  [] -> true
  odd str length -> false
PLAN:
> Create a dictionary for the bracket pairs
> Use a stack for every open bracket encountered. Pop if encountered a closing bracket.
"""

def is_valid_post_format(posts):
  stack = []
  d = {")": "(", "]":"[", "}":"{"}
  for char in d:
      if char in "({[":
          stack.append(char)
      else:
          if not stack:
              return False
          if d[char] != stack[-1]:
              return False
          stack.pop()
  return len(stack) == 0

# print(is_valid_post_format("()"))
# print(is_valid_post_format("()[]{}")) 
# print(is_valid_post_format("(]"))

"""
Set1, #2
UNDERSTAND:
> Input: 
> Output: 
> Edge cases:
  [] -> []
  len(queue) = 1 -> return list 
PLAN:
> Create a dictionary for the bracket pairs
> Use a stack for every open bracket encountered. Pop if encountered a closing bracket.
"""

def reverse_comments_queue(comments):
  ans = []
  stack = []
  for c in comments:
      stack.append(c)
  while stack:
    ans.append(stack.pop())
  return ans

# print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))
# print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))

       
"""
Set1, #3
UNDERSTAND:
> Input: str
> Output: boolean
> Edge cases: 

PLAN:
two pointers on ends of str

"""
def is_symmetrical_title(title):
  title = title.lower()
  new_t = ""
  for char in title:
     if char.isalpha():
        new_t += char
  left = 0
  right = len(new_t) - 1
  while left < right:
    if new_t[left] != new_t[right]:
      return False
    left += 1
    right -= 1
  return True

# print(is_symmetrical_title("A Santa at NASA"))
# print(is_symmetrical_title("Social Media"))

# Set 1, #4
def engagement_boost(engagements):
  squared_engagements = [0] * len(engagements)
  position = len(engagements) - 1

  left = 0
  right = len(engagements) - 1
  while left <= right:
    if abs(engagements[left]) < abs(engagements[right]):
      squared_engagements[position] = engagements[right] ** 2
      right -= 1
    else:
      squared_engagements[position] = engagements[left] ** 2
      left += 1
    position -= 1
  return squared_engagements

# print(engagement_boost([-4, -1, 0, 3, 10,10]))
# print(engagement_boost([-7, -3, 2, 3, 11]))
















"""
Set1, #1
UNDERSTAND:
> Input:
> Output:
> Edge cases:

PLAN:

"""

