# 3/10 day 5

""" String operations:
concatenation, slicing, formatting
useful methods: .lower(), .upper(), .split(), .replace()

"""
# Methods
s = "Hello"
sentence = "Hello. World"
sample = "This is our fourth sample string for day."
s.lower() # "hello"
s.upper() # "HELLO"
s.split() # ["Hello"]
sentence.split(".") # ["Hello", "World"] 
sample.replace("sample", "REPLACED") # "This is our fourth REPLACED string for day." 
# note: if sample was written as sampless, it would not get replaced. So do .replace("sample ", "REPLACED"),

# Slicing: returns a portion of a string based on provided indices

exampleString = "This is our fifth sample string for the day"
#[slice begins: slice ends (exclusive)]
value0 = exampleString[0:5]
value1 = exampleString[:5] # without providing left index, default to 0:5 
value2 = exampleString[4:] 
value3 = exampleString[2:8]
value4 = exampleString[0:10:2]   #optional “step” value (step size you're taking). In this case, gives first 10 values, but every other character.
value5 = exampleString[10:0:-1]
# Note: value5 = exampleString[10:1:-1] counts backwards; returns the first characters but in reverse; 10 to 0 (exclusive)

# Instructor Demo
""" Problem
A pangram is a sentence that contains every letter of the English alphabet at least once, regardless of case. Write a function to determine if a given sentence is a pangram.
Input: sentence = "The quick brown fox jumps over the lazy dog"
Output: True

Plan:
Look for all 26 letters in dictionary
Track by using a dictionary
For loop to iterTe through string 
Count # of keys in our dictionary, if == 26 (return value)
"""

def is_pangram(sentence):
    lowercase_sentence = sentence.lower()
    letter_count = {} #key letter, value T/F

    for char in lowercase_sentence:
        if char.isalpha() == False: # dictionary will count a space as a key so we use isalpha() to skip it
            continue

        if char not in letter_count: # first time encountering char in dictionary
            letter_count[char] = True
    
    if (len(letter_count) == 26):
        return True
    return False

# print(is_pangram("The quick brown fox jumps over the lazy dog")) # True

####

# Version 1, #1

def count_mississippi(limit):
    for num in range(1, limit):
        print( f"{num} mississippi")

# count_mississippi(6)
# 1 mississipi
# 2 mississipi
# 3 mississipi
# 4 mississipi
# 5 mississipi

# Version 1, #2
def swap_ends(my_str):
    end = my_str[-1]
    start = my_str[0]
    mid = my_str[1:-1]
    return end + mid + start

my_str = "boat"
swapped = swap_ends(my_str)
# print(swapped) #toab


# V1, #4
def reverse_string(my_str): # 3 ways
    # return my_str[::-1]

    # reverse_str = ""
    # for i in range(len(my_str) -1, -1, -1):
    #     reverse_str += my_str[i]
    # return reverse_str
    
    reverse_string = ""
    i = len(my_str) - 1

    while (i >= 0):
        reverse_string += my_str[i]
        i -= 1
    return reverse_string


my_str = "live"
# print(reverse_string(my_str))

# version 1 #6
def min_distance(words, word1, word2):

    for i in range(len(words)):
        for j in range(len(words)):
            if words[i] == word1 and words[j] == word2:
                distance = abs(j-i)
    return distance 
    
words = ["the", "quick", "brown", "fox", "jumped", "the"]
dist1 = min_distance(words, "quick", "jumped")
dist2 = min_distance(words, "the", "jumped")
# print(dist1) # 3
# print(dist2) # 1

words2 = ["code", "path", "code", "contribute",  "practice"]
dist3 = min_distance(words2, "code", "practice")
# print(dist3) # 2


# Version #4: Reverse Sentence

def reverse_sentence(sentence):
    word_arr = sentence.split()
    reverse_sentence = ""

    i = len(word_arr) - 1
    while (i >= 0):
        reverse_sentence += word_arr[i]
        reverse_sentence += " "
        i -= 1
    return reverse_sentence

sentence = "I solemnly swear I am up to no good"
print(reverse_sentence(sentence)) # "good no to up am I swear solemnly I"

# Version 3, #1: Choose Your Pokemon

def choose_pokemon(my_pokemon):
	for pokemon in my_pokemon:
		print(f"{pokemon} I choose you!")

# choose_pokemon(["1", "2", "3"])
# choose_pokemon(["Pikachu", "Charizard", "Eevee"])

# V3, #6 Roman to Integer
"""
I = 1 V = 5
X = 10 L = 50
C = 100 D = 500
M = 1000

Implementation:
counter_sum
loop through roman numerals by char
if char is I or X or C, check the next char if it's

"""

def roman_to_int(s):
    # attempt 1
    # s = 0
    # for i in range(len(s)):
    #     if s[i] == "I":
    #         if s[i] == "V":
    #             s += 5
    #         elif s[i] == "X":
    #             s+= 10
    #     elif s[i] == "X":
    #         if s[i] == "L":
    #             s+= 50
    #         else if s[i] == "C":
    #             s+= 100
    #     elif s[i] == "C":
    #     else:

    # attempt 2
    roman_integral = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
        }
    
    total = 0
    for i in range(len(s)):
        
        if i+1 < len(s) and roman_integral[s[i]] < roman_integral[s[i+1]]:
            # print(roman_integral[s[i]])
            # print(roman_integral[s[i+1]])
            total -= roman_integral[s[i]]
        else:
            total += roman_integral[s[i]]
    return total

s = "XL"
print(roman_to_int(s)) #40

# s2 = "LVIII"
# print(roman_to_int(s2)) #58

# s3 = "MCMXCIV"
# print(roman_to_int(s3)) #1994