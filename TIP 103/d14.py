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
go from 2 to n+1
  check if ang can win

Choose any x such that 0 < x < n and n % x == 0
  |
  player_nums = set()
  for i in range(1,10):
    if n % i == 0:
      player_nums.append(i)


REVIEW:
EVALUATE: 
"""
def aang_wins(n):
  dp = [False] * (n+1)
  for i in range(2,n+1): # dp[i] working up 
    for j in range(1, i): # j - possible value that Ang can subtract from i
      if i % j == 0: #checking if j is a valid move for Ang
        if not dp[i-j]: #checking if Ang makes this move, he will win or lose
          dp[i] = True
          break
  return dp[n]

# print(aang_wins(2))
# print(aang_wins(3))

"""
True
Example 1 Explanation: Aang reduces the strength by 1, and Zuko has no more moves.

False
Example 2 Explanation: Aang reduces the strength by 1, then Zuko does the same, leaving 
Aang with no moves.
"""
