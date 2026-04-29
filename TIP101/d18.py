# Interview Problem 1
# Given a sentence s, remove all words that are too short (3 letters or fewer) or too long (8 letters or more), then return the filtered sentence as a single string. The returned sentence should be all lowercase.
# Example:
# Input: s = "The Quick brown fox Jumped over the LAZY dog"
# Output: "quick brown jumped over lazy"

"""
U:
Input: string
Output: string 

P:
Use .lower() on the string
Use the .split() function to create an array each element representing an individual word
Create an empty string
Go through array and ignore words that are too short or too long, concatenate str to the new str
Return new str
"""

def cleanStr(s):
    s = s.lower()
    new_s = ""
    arrWords = s.split(" ")
    for word in arrWords:
        if len(word) > 3 and len(word) < 8:
            new_s += word
            new_s += " " 
    return new_s

# print(cleanStr("The Quick brown fox Jumped over the LAZY dog"))

# V1 Q1

"""
U:
Input: string containing (,),{,},[,]
Output: boolean value

M:
Stack

P:
Loop through the char in the str
If it's an open bracket, push to stack
If it's a closing bracket, pop from the stack
"""

def is_valid(s):
    stack = []

    for bracket in s:
        if bracket == "(" or bracket == "{" or bracket == "[":
            stack.append(bracket)
        else: # closing bracket
            if len(stack) == 0:
                return False
            if bracket == ")":
                if stack.pop() != "(":
                    return False
            if bracket == "}":
                if stack.pop() != "{":
                    return False
            if bracket == "]":
                if stack.pop() != "[":
                    return False
    return True

# Example #1:
s = "()"
# print(is_valid(s))
# Expected Output: True

# Example #2:
s = "()[]{}"
# print(is_valid(s))
# Expected Output: True

# Example #3: 
s = "(())"
# print(is_valid(s))
# Expected Output: True

# Example #4:
s = "(]"
# print(is_valid(s))
# Expected Output: False

# Example #5:
s = "([)]"
# print(is_valid(s))
# Expected Output: False

#V1 Q2

#You are given a list of integers prices 
# where prices[i] is the price of a given stock on the 
# ith day.

#You want to maximize your profit by choosing a single 
# day to buy one stock and choosing a different day in the 
# future to sell that stock.

#Return the maximum profit you can achieve from this 
# transaction. If you cannot achieve any profit, return 0.


#a list of prices
#we have to choose the best (minimum price) day to purchase
#and match it with the best (maximum price) day to sell - this maximum price day needs to be after the day of purchase
#if no profit is possible, return 0

#create a sub_list from list[0: -2]
#obtain min_val from sub_list

#create new sub_list of only values after min_val
#obtain max_val of the sublist
#if min_val is < than max_val, then return max_val - min_val
#if not, then return 0

def get_index(lst, value):
    for i in range(len(lst)):
        if lst[i] == value:
            return i

def max_profit(prices):
    # edge cases
    if prices == []:
        return 0
    if len(prices) == 1:
        return 0
    
    lst = prices[0:-1] # list from element 0 up to and excluding last element
    min_val = min(lst)

    index = get_index(prices, min_val)

    if index == 0:
        lst2 = prices
    else:
        lst2 = prices[index+1:]
    
    max_val = max(lst2)

    if min_val < max_val:
        return max_val - min_val
    else:
        return 0

"""
outerloop: go over each element (the prices)
inner loop: for each price of the outer loop, do computation with each price after current price in the list
    if max profit from computation > stored max profit:
        stored max profit = max profit
"""

def max_profit(prices):
    max_profit = 0
    for i in range(len(prices)): # go through each price
        for j in range(i+1, len(prices)): # go through each price starting after the price i points to 
            if prices[j] - prices[i] > max_profit:
                max_profit = prices[j] - prices[i]
    return max_profit

prices = [7,1,5,3,6,4]
prices2 = [7,6,4,3,1]

# print(max_profit(prices))
# print(max_profit(prices2))

# V1 Q3

"""
U:
Input: two heads to two linked list
Output: head of a merged linked list

M:
while loop approach with next = current.next

P:
Create two variables pointing to the given 2 heads
Use head_a as to be merged linked list
Use the while loop approach:

"""
def shuffle_merge(head_a, head_b):
    # edge cases
    if head_a == None and head_b == None:
        return None
    if head_a and head_a == None:
        return head_a
    if head_a == None and head_b:
        return head_b
    
    current_a = head_a 
    current_b = head_b


    while current_a:
        


        current_a = current_a.next

    


