# 3/3/26 Unit 2

# Demo
# Understand:
# Plan:
'''
1. takes in a list of words
2. create an empty dictionary
3. iterate through list
4. check if current word is an anagram of something else
4b. figure how to assess anagrams
5. keep track / update dictionary with new decisions
6. return a list of grouped words

return a list

'''
words = ["eat", "tea", "tan", "ate", "nat", "bat"] 
# output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

# Implement
def group_anagrams(words):
    anagram_dictionary = {} # aet -> [tea, eat, ate]; this line makes clear after line 26

    for word in words:
        sorted_word = str(sorted(word)) # eat -> aet, tea -> aet, ate -> aet
        # sorted word will be used as an anagram key
        # note: sorted() returns a list so use str() for string sorting

        if  sorted_word not in anagram_dictionary: #if item in dictionary
            anagram_dictionary[sorted_word] = [word]
        else:
            anagram_dictionary[sorted_word].append(word)
    
    return list(anagram_dictionary.values())
        
# print(group_anagrams(words))
    
# Q1 (version 2)

def is_monotonic(nums):
    monoIncreasing = True
    monoDecreasing = True

    # 1,2,3,4,5
    for i in range(len(nums)-1):
        if not(nums[i] <= nums[i+1]):
            monoIncreasing = False
            break
    
    for i in range(len(nums)-1):
        if not(nums[i] >= nums[i+1]):
            monoDecreasing = False
            break
    
    return monoDecreasing or monoIncreasing

# nums1 = [1,2,2,3,10]
# print(is_monotonic(nums1))

# nums2 = [12,9,8,3,1]
# print(is_monotonic(nums2))

# nums3 = [1,1,1]
# print(is_monotonic(nums3))

# nums4 = [1,9,8,3,5]
# print(is_monotonic(nums4))


# Q2 (version 2)
def student_directory(student_names):
    student_dictionary = {}
    for i in range(len(student_names)):
        student_dictionary[student_names[i]] = i+1

    return student_dictionary

student_names = ["Ada Lovelace", "Tu Youyou", "Mae Jemison", "Rajeshwari Chatterjee", "Alan Turing"]
# print(student_directory(student_names))


# Q3 (version 1, rest below version 1)
def print_pair(dictionary, target):
    val = dictionary.get(target)
    if val:
        print("Key", target)
        print("Value", val)
    else:
        print("That pair does not exist!")

dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
# print_pair(dictionary, "patrick")
# print_pair(dictionary, "plankton")
# print_pair(dictionary, "spongebob")

# Q4
def keys_v_values(dictionary):
    sum_key = 0
    sum_val = 0

    for key in dictionary:
        sum_key += key
        sum_val += dictionary[key]
    
    if sum_val == sum_key:
        print("Balanced")
    elif sum_val > sum_key:
        print("Values")
    else:
        print("Keys")

dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
# keys_v_values(dictionary1)

dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
# keys_v_values(dictionary2)


# Q5 
def restock_inventory(current_inventory, restock_list):
    
    for key in restock_list:
        if current_inventory.get(key):
            current_inventory[key] += restock_list[key]
        else:
            current_inventory[key] = restock_list[key]

    return current_inventory

current_inventory = {
    "apples": 30,
    "bananas": 15,
    "oranges": 10
}

restock_list = {
    "oranges": 20,
    "apples": 10,
    "pears": 5
}

# print(restock_inventory(current_inventory, restock_list))

# Q6
def calculate_gpa(report_card):
    gpa = 0
    num_grade = 0
    for course in report_card:
        if report_card[course] == "A":
            gpa += 4
        elif report_card[course] == "B":
            gpa += 3
        elif report_card[course] == "C":
            gpa += 2
        elif report_card[course] == "D":
            gpa += 1
        num_grade += 1

    print(gpa/num_grade)

report_card = {"Math": "A", "Science": "C", "History": "A", "Art": "B", "English": "B", "Spanish": "A"}
# calculate_gpa(report_card)


# Q7
def highest_rated(books):
    best_book = books[0]

    for book in books:
        if book["rating"] > best_book["rating"]:
            best_book = book
    
    return best_book

books = [
    {"title": "Tomorrow, and Tomorrow, and Tomorrow",
     "author": "Gabrielle Zevin",
     "rating": 4.18
    },
    {"title": "A Fortune For Your Disaster",
     "author": "Hanif Abdurraqib",
     "rating": 4.47
    },
    {"title": "The Seven Husbands of Evenlyn Hugo",
     "author": "Taylor Jenkins Reid",
     "rating": 4.40
    }
]

# print(highest_rated(books))


# Q8

def index_to_value_map(lst):
    d = {}

    for i in range(len(lst)):
        d[i] = lst[i]
    
    return d

lst = ["apple", "banana", "cherry"]
print(index_to_value_map(lst))



