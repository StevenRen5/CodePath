# 11/3/26 Dynamic Programming & Backtracking

""" Instructor demo
The Goal: Find the absolute minimum number of coins (use the fewest coins possible to make a given amount)
Greedy Logic: Take the biggest coin first, no matter what.
DP Logic: Try every coin as a first step and see which one leads to the best future.
"""

def greedy_coins(amount,coins):
  coins = sorted(coins, reverse=True)
  count = 0
  for coin in coins:
    while amount >= coin:
      amount -= coin
      count += 1
  return count

# print(f"The result for 6 cents is {greedy_coins(6, [1,3,4])}")

def dp_coins(amount, coins):
  dp = [float('inf')] * (amount + 1) 
  # [inf,inf,inf,inf,inf,inf,inf] for amount = 6 
  # index of dp represents the amount of cents, value represents the number of coins needed 
  dp[0] = 0 # min coins needed to make 0 cents
  # solve for the subproblem for every amount starting from 1 cent working up to 6 cent. i is the amount.
  for i in range(1, amount+1):
    for coin in coins:
      if i >= coin: # is this coin less than or greater than amount (can this coin fint into amount)
        dp[i] = min(dp[i], dp[i-coin]+1) # dp[i-coin]+1 The minimum number of coins needed to make the remaining amount, plus 1 coin that we're currently considering.


# i = The amount we're trying to make.
# coin = The coin we're considering using.
# i - coin = The remaining amount after using that coin.
# dp[i - coin] = The minimum number of coins needed to make that remaining amount. We found the optimized sol for i - coin already
# + 1 = Counts the coin we're currently using.

""" instructor demo for back tracking
A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 inclusive. No leading zeros.
Given: A string s containing only digits
Goal: Return all possible valid IP addresses that can be formed by inserting dots into s without reordering or removing any digits
Example: “25525511135” should return [“255.255.11.135”, “255.255.111.35”]

"""

def validIpAddress(s):
  res = []
  if len(s) < 4 or len(s) > 12:
    return res

  def backtrack(i, dots, currentIp):
    if dots == 4 and i == len(s):
      res.append(currentIp[:-1])
      return 
    if dots > 4:
      return 

    for j in range(i, min(i+3), len(s)):
      # no leading zeros
      if i != j and s[i] == "0":
        continue 

      # check if we're within range of 0 to 256 inclusive
      if int(s[i:j+1]) < 256:
        backtrack(j+1, dots+1, currentIp + s[i:j(j+1)] + ".")

  backtrack(0,0, "")
  return res

string = "101023"
# print(f"The valid IPs for {string} are {validIpAddress(string)}")
  


"""
Set1, #1
UNDERSTAND:
> Input: integer (wsidomLevel)
> Output: a list of the elements at the wisdomLevel
> note: 
 - hexagons externally are 1 (each row starts and ends with a 1)
 - first two rows: it's just 1 (base case)
> Edge cases:
MATCH:
1D dynamic programming
PLAN:

always start w [1], [1, 1]

check when depth == row we want to return



initialize prev row = [1]
track prev and curr rows

iterate until depth == desired row

--

for loop: 0th level to wisdom level 

REVIEW:
EVALUATE: 
"""

def wisdom_pyramid(wisdomLevel):
  prev = [1]
  curr = []

  depth = 1
  while depth < wisdomLevel+1: # start ar depth 1
    # take prev row
    # add the elements next to each other and append it to curr row array
    # have 1 at beginning and end of curr array
    curr.append(1)
    for i in range(len(prev)-1): # curr arr will be one element larger than prev
      if len(prev) != 1:
        curr.append(prev[i]+prev[i+1])

    curr.append(1)
    prev = curr
    curr = []

    depth+=1

  return prev

"""
        1
       1. 1
      1. 2. 1
    1   3. 3  1
"""
# print(wisdom_pyramid(3))
# print(wisdom_pyramid(0))
# print(wisdom_pyramid(5))

"""
Set1, #2
UNDERSTAND:
> Input: integer - n (Strength)
> Output: bool
> note: Ang starts first
> Edge cases:
MATCH:
PLAN:

try every number that's 0 < x < n and n % x == 0
go from i in range 2 to n+1
  nested loop from j in range 1 to i exclusive


REVIEW:
EVALUATE: 
"""
def aang_wins(n):
  dp = [False] * (n+1) # dp[i] stores whether the player whose turn it is can win when the current number is i, assuming both players play optimally. When calculating dp[i], we think generically who's turn it is. It represents whoever is about to play at that number. In this problem for an arbitrary n, Aang always go first. Ex. dp[2] = True (when calculated) --> Ang can win if he starts at 2.
  # dp[1] = False b/c no positive int such that 0 < x < 1. Base case.
  for i in range(2,n+1): # dp[i] working up. i is thr current battlefield number.
    for j in range(1, i): # j - possible value that we can subtract. Rule is 0 < j < i (so 1 to i exclusive)
      if i % j == 0: # checking if j is a valid move
        # If I (ang) can make a valid move that puts my opponent in a losing position, then my current position is a winning position.
        if not dp[i-j]: # i-j the number I'm leaving for my oponent. dp[i-j] is can my oponent win from i-j? not dp[i - j] → My opponent cannot win from that number
          dp[i] = True # Therefore I can win
          break # The break is there because we only need to find one move that guarantees a win; If there's a move that guarantees a win, the player will choose it. We break because we've found a move that guarantees victory. There's no need to check the remaining moves since dp already calculated them.
  return dp[n]

# print(aang_wins(2))
# print(aang_wins(3))

"""
n = 2 
dp[2] = True means the player starting at 2 can win.
If Aang starts at 3 and subtracts 1, Zuko gets 2.
Since Zuko can win from 2, Aang loses (assuming optimal play).

True
Example 1 Explanation: Aang reduces the strength by 1, and Zuko has no more moves.

False
Example 2 Explanation: Aang reduces the strength by 1, then Zuko does the same, leaving 
Aang with no moves.
"""

"""
Set1, #3
UNDERSTAND:
> Input: ingredients - list of int
> Output: int 
> Edge cases:
MATCH:
DP
PLAN:

dp solution:

base case = solutions to the smallest/easiest subproblems

subproblem = what we're solving at a specific index
- max_dp[i] = the largest product of a consecutive subarray that ends exactly at index i.
- min_dp[i] = the smallest product of a consecutive subarray that ends exactly at index i.
- At each index, we can either start a new subarray at i or extend a previous subarray ending at i-1. Sometimes starting a new subarray at index i is better since it's the best option.
-We track both the maximum and minimum products because multiplying a negative product by another negative number can turn the minimum into the new maximum (and vice versa)
recurrence relation = how the sol to larger subproblem is constructed from smaller subproblems.
- 3 options because we don't know if starting a new subarray, extending the previous max, or previous min can give us the best product.
- Start a new subarray: x
- Extend the previous maximum: max_dp[i-1] * x
- Extend the previous minimum: min_dp[i-1] * x
final sol: involves the last index / or whole list
return max(max_dp) and not max_dp[-1] b/c our largest product isn't guranteed to be at the end; max_dp[i] represents the largest product of a consecutive subarray ending exactly at index i, but the overall maximum might end at an earlier index.

EVALUATE: 
O(n) space, time
"""
def strongest_tea(ingredients):
  min_dp = [0] * len(ingredients)
  max_dp = [0] * len(ingredients)

  # base case: the only option at i = 0, is the first element itself.
  min_dp[0] = ingredients[0] # O(n)
  max_dp[0] = ingredients[0]

  for i in range(1, len(ingredients)): # O(n)
    x = ingredients[i]
    min_dp[i] = min(x, min_dp[i-1] * x, max_dp[i-1] * x) #O(1) b/c comparing 3 values constant, independent of len(ingredients)
    max_dp[i] = max(x, min_dp[i-1] * x, max_dp[i-1] * x)

  return max(max_dp)


print(strongest_tea([1, 2, -3, 4]))
print(strongest_tea([-2, -1]))
print(strongest_tea([1, 2, -3, 4,-5,-1])) 
"""
4
Example 1 Explanation: The strongest tea Iroh can brew uses only the last ingredient with strength 4.

2  
Example 2 Explanation: The strongest tea Iroh can brew uses both ingredients: -2 and -1 (-2 * -1 is 2).
"""
