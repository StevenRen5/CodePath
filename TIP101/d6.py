# 3/12 String Formatting (Two ways):
userName = "Cory2026"
currentTime = "March 10th, 8:15pm"
# 1st way: 
# print(f"{userName} has signed in at {currentTime}.")
# 2nd way: 
# print("{} has signed in at {}.".format(userName, currentTime))

""" Instructor Demo
# Given a string s containing words separated by spaces, reverse the order of the words. Remove extra spaces and ensure that words are separated by a single space in the output. Let’s investigate VS Code debugging features!
# Input: s = "  the sky is  blue  "
# Output: "blue is sky the"

Understand:
Need to remove white spaces when splitting words, then spacking back in at the end, reverse them.
input and output are both strings

Plan:
1. Break up words into individual components
2. reverse them somehow (maybe using built-in functions)
3. glue the words back ogether in reverse order ,adding spacing bak in
4. return final string

Implement:

"""

def reverse_words(s):
    word_list = s.split() # split by default at every space ['the', 'sky', 'is', 'blue']
    print(word_list)

    word_list.reverse() # reverses the list, but returns None. print(word_list) again

    print(" ".join(word_list))

    # return word_list

s = "  the sky is  blue  "
# reverse_words(s)

# Version 1, Q1
def sum_of_number_strings(nums):
    total = []
    for num in nums:
        total.append(int(num))
    return sum(total)


    
nums = ["10", "20", "30"]
sum = sum_of_number_strings(nums)
# print(sum)


# V1, Q2
def remove_duplicates(nums):
    d = {}
    l = []
    for num in nums:
        if num not in d:
            d[num] = num
    
    for key in d:
        l.append(key)
    
    return l

# V1, Q3
"""
Plan:
1. Create a new string in reverse excluding the '-'
2. Store the indices of the dashes in a dictionary 
3. Loop through the string by index
4. Use conditional to see if current index is not in dictionary, include char from reverse string 
"""

def reverse_only_letters(s):
    d = {}
    initial_reverse_string = ''
    c = 0 # counter for initial_reverse_string
    final_reverse_string = ''

    # s = "ab-c"
    # range(3, -1, -1) --> 3,2,1,0
    for i in range(len(s)-1, -1, -1):
        if s[i] == '-':
            d[i] = '-'
        else:
            initial_reverse_string += s[i]
    
    # using s = "abc"
    for i in range(len(s)): # 4 iterations
        if i in d:
            final_reverse_string += '-' # runs once 
        else:
            final_reverse_string += initial_reverse_string[c] # runs three times
            c += 1
    
    return final_reverse_string

s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
# print(reversed_s) #j-Ih-gfE-dCba

# V1, Q4
"""
Problem: 
Write a function longest_uniform_substring() that takes in a string s and returns the length of the longest uniform substring. A uniform substring consists of a single repeated character.

Plan: 
Loop through string
Use a dictionary to store number of consecutive appearances of a character as character:number pair
Return greatest value in dictionary 
"""

def longest_uniform_substring(s):
    count = 1
    max_length = 1

    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count += 1
        else:
            if count > max_length:
                max_length = count
            count = 1
    
    if count > max_length: # situation where we have only a unique letter in s or longestive consecutive letter is at the end
        max_length = count

    return max_length
    # ex: abc -> 1, aaa -> 3      


s1 = "aabbbbCdAA"
l1 = longest_uniform_substring(s1)
# print(l1)

s2 = "abcdef"
l2 = longest_uniform_substring(s2)
# print(l2)

# V1, Q5

"""
Problem:
In the game League of Legends, Teemo attacks his enemy Ashe with poison arrows. Write a function find_poisoned_duration() that takes in two parameters: time_series (the time at which Teemo's attacks hits Ashe) and time_duration (the duration of the poisoning effect). The function returns the total time that Ashe is in a poisoned condition.

time_series is a list of integers that represents the times at which Teemo attacks and makes Ashe poisoned for the exact time_duration.

If Teemo hits Ashe while she is still poisoned, the poison's duration starts over. For example, if Teemo attacks at times 1 and 4 for 3 seconds, the states at each time would be:

1: attacked
2: in poison state
3: in poison state
4: attacked, poison duration resets to 3
5: in poison state
6: in poison state
7: in poison state 
8: in normal state

Total time in poisioned condition is 5

# Understand:
time_series is a increasing list
duration >= 1


Plan:
Create a counter for the total time in poisoned state
Loop through time_series 
    Compare current time to next time and subtract by duration. If it's > 0, update counter by computation
Return counter
"""

def find_poisoned_duration(time_series, duration):
    poision_total = 0

    # time_series = [1,4,9], dur = 3

    for i in range(len(time_series)-1):
        poision_counter = 0
        initial = time_series[i]
        while initial < time_series[i+1] - 1:
            if poision_counter < duration: 
                poision_counter += 1 
            initial += 1
        poision_total += poision_counter
    
    poision_total += duration # accounts for the last attack-poisoned duration
    return poision_total

# time_series = [1,4,9]
time_series = [1,4,6]
damage = find_poisoned_duration(time_series, 3)
# print(damage) #8

"""
Attack 1
P 2
P 3
A 4
P 5
P 6
P 7
8 normal
A 9
P 10
P 11
P 12
"""

# V1 Q6

"""
Plan:
Create a sum_counter
Create a dictionary to track whether we've seen a duplicate number in lst 1 by using the boolean value
Go through dictionary by key and if the value is false (not seen), if it appears in lst 2, increment value to sum_counter
"""


def sum_of_unique_elements(lst1, lst2):
    d = {} 
    sum = 0

    for num in lst1:
        if num not in d:
            d[num] = False
        else:
            d[num] = True
    
    for key in d:
        if key not in lst2 and d[key] == False:
            sum += key
    
    return sum

lstA = [1, 2 ,3, 4] 
lstB = [3, 4, 5, 6]
lstC = [7, 7, 7, 7]

sum1 = sum_of_unique_elements(lstA, lstB)
print(sum1) # 3

sum2 = sum_of_unique_elements(lstC, lstB)
print(sum2) # 0