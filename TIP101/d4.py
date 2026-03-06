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
        if highest_task is None:
            highest_task = task
        elif tasks[task] > tasks[highest_task]:
            highest_task = task
    tasks.pop(highest_task)
    return highest_task

# Q5
def find_majority_element(elements):
    d = {}
    for ele in elements:
        if ele in d:
            d[ele] += 1
        else:
            d[ele] = 1
    
    for num in d:
        if d[num] > len(elements)/2:
            return num
    return None

elements = [2, 2, 1, 1, 1, 2, 2]
print(find_majority_element(elements))


'''
inputs: list of integers num, positive num k
outputs: true if list contains any duplicate elements within k indices of each other
'''




# Q6 (incomplete)
def has_duplicates(nums, k):
    d = {}
    if k >= len(nums):
        for n in nums:
            if n in d:
                return True
            else:
                d[n] = n # doesn't matter the value
    
    # dictionary d would store d[number] = previous index 
    for i in range(len(nums)):
        if nums[i] in d:
            # [6,0,6] -> encountered 6 already
            if i - d[nums[i]] <= k:
                return True
            else:
                d[nums[i]] = i
        else:
            d[nums[i]] = i
    return False
	

nums = [5, 6, 8, 2, 6, 4, 9]
check1 = has_duplicates(nums, 2)
print(check1) # False
check2 = has_duplicates(nums, 5)
print(check2) # True
check3 = has_duplicates(nums, 3)
print(check3) # True

# Q7

def divide_list(nums):
    d = {}
    for num in nums:
        if num in d:
            d[num] += 1
        else:
            d[num] = 1
    
    for key in d:
        if d[key] % 2 != 0:
            return False
    return True

nums = [3,2,3,2,2,2]
# print(divide_list(nums))
nums2 = [1,2,3,4]
# print(divide_list(nums2))

