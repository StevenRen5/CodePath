# 9/15/26: Foundations

"""
Set1, #5
UNDERSTAND:
> Input: unique integer arr
> Output:
> Edge cases:
MATCH:
PLAN:
REVIEW:
EVALUATE: 
"""

def find_missing_clues(clues, lower, upper):
  res = []
  #edge clase:
  if clues[0] > lower:
    res.append([lower, clues[0] - 1])
  for i in range(len(clues)-1):
    if clues[i] + 1 != clues[i+1]:
      res.append([clues[i]+1, clues[i+1]-1])
  if clues[len(clues)-1] < upper:
    res.append([clues[len(clues)-1]+1, upper])
  return res
	
clues = [0, 1, 3, 50, 75]
lower = 0
upper = 99
print(find_missing_clues(clues, lower, upper))
