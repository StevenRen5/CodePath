# 3/5

# Instructor Demo
''' Understand:
input: typles, always, same size, 0 category, 1 value (item)
output: dictionary, key cateogires, value will be the count
logic: want to group and count by category
'''

# Plan:

def count_by_category(items):
    count_dictionary = {}

    for item in items:
        if count_dictionary.get(item[0]):
            count_dictionary[item[0]] += 1
        else:
            count_dictionary[item[0]] = 1
    
    return count_dictionary


items = [("fruits", "apple"), ("vegetables", "carrot"), ("fruits", "banana")]
# print(count_by_category(items))
# output: {"fruits": 2, "vegetables": 1}

# Q1
def cast_vote(votes, candidate):
    # checks if there are no votes cased
    if not votes:
        votes = {candidate: 1}
    else:
        if candidate in votes:
            votes[candidate] += 1
        else:
            votes[candidate] = 1
        
    return votes


# Q2
def common_keys(dict1, dict2):
    lst = []

    for key in dict1:
        if key in dict2:
            lst.append(key)
    return lst
	
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
common_list = common_keys(dict1, dict2)


# Q3
def count_occurrences(nums):
    counts = {}
    for num in nums: 
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    return counts


# Q4
def get_highest_priority_task(tasks):
    highest_task = None

    for task in tasks:
        if highest_task == None:
            highest_task = task
        elif tasks[task] > tasks[highest_task]:
            highest_task = task
    tasks.pop(highest_task)
    return highest_task

# Q5


# Q6
