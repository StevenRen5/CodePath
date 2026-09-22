# 9/22/26: Hashing, Heaps, Big O

"""
Set#, ##
UNDERSTAND:
> Input:
> Output:
> Edge cases:
MATCH:
PLAN:
REVIEW:
EVALUATE: 
"""

"""
Set1, #1
UNDERSTAND:
> Input: dictionary - treasure_map
> Output: integer - total # of treasures 
> Edge cases:
- {} -> 0
MATCH:
dictionary problem
PLAN:
create a variable to store total # of treasures
loop through the dictionary by keys and:
  counter += treasure_map[key]
return counter
REVIEW:
EVALUATE: 
- run time: O(n), space complexity: O(1)
"""

def total_treasure(treasure_map):
  counter = 0
  for location in treasure_map:
    counter += treasure_map[location]
  return counter

treasure_map1 = {
    "Cove": 3,
    "Beach": 7,
    "Forest": 5
}

treasure_map2 = {
    "Shipwreck": 10,
    "Cave": 20,
    "Lagoon": 15,
    "Island Peak": 5
}

# print(total_treasure(treasure_map1)) 
# print(total_treasure(treasure_map2)) 





"""
Set1, #2
UNDERSTAND:
> Input: string containing lowercase English letters and whitespace
> Output: boolean, True if contains all letters of the English alphabet at least once
> Edge cases: 
- empty string: false
- 
MATCH: hashMap 
PLAN:
create a hashMap<character, int> to keep track of the count for each track
iterate through the characters of the string, if not a whitespace, check against hashmap. 
if exists -> increment count on hashamp, else-> insert into hashmap with a count of 1
return if the size of the map is 26. 
REVIEW:
EVALUATE: 
space: O(n)
time: O(n)
"""

def can_trust_message(message):
    map = {}
    for i in range(len(message)):
        character = message[i]
        if character == ' ':
            continue
        elif character in map: 
            map[character] = map[character] + 1
        else:
            map[character] = 1
    return len(map) == 26

message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

# print(can_trust_message(message1))
# print(can_trust_message(message2))



"""
Set#, ##
UNDERSTAND:
> Input: integer array chests
> Output: integer aray of all integers that appear twice
> Edge cases: empty array, 
MATCH: hashmap
PLAN: create hashmap that has chest number for key and count for value/
loop through each chest, if not in chest add the number, if in chest, increment count
REVIEW:
EVALUATE: 
time: O(n)
space: O(n)
"""

def find_duplicate_chests(chests):
    map = {}
    res = []

    for i in range(len(chests)):
        chest = chests[i]
        if chest in map:
            map[chest] += 1
            res.append(chest)
        else:
            map[chest] = 1

    return res

chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

# print(find_duplicate_chests(chests1))
# print(find_duplicate_chests(chests2))
# print(find_duplicate_chests(chests3))    

"""
Set1, #4
UNDERSTAND:
> Input: string 
> Output: boolean value
> Edge cases:
- 1 char -> true
- 0 char -> true
MATCH:
dictionary 
PLAN:
create a dictionary store the count of char in str
go through each char in str:
  add or increment the char in the dictionary
...
REVIEW:
EVALUATE: 
"""

def can_make_balanced(code):
  d = {}
  for char in code:
    if char not in d:
        d[char] = 1
    else:
        d[char] += 1

  # edge case: 2 character keys
  if (len(d.keys())) <= 2:
     return True

  min_value = min(d.values())

  counter = 0
  for k, v in d.items():
    if v > min_value: # > 2
        counter += 1
        
  return counter == 1 # counter = 2
    
code1 = "abbb"
code2 = "haha"

print(can_make_balanced(code1)) 
print(can_make_balanced(code2))    

# cont'd problem 5