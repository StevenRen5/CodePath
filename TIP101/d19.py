# V1 Q1
def contains_duplicate(nums):
    for i in nums:
        counter = 0
        for j in range(len(nums)):
            if i == nums[j]:
                if counter == 0:
                    counter = 1
                else:
                    return True
    return False

#for i in list
#for j in range len(list)
#check if i == list[j]
#if so, return True

#if it goes all the way through all elements
#return False
nums = [1,2,3,1] #True
# print(contains_duplicate(nums))

nums2 = [1,2,3,4] #False
# print(contains_duplicate(nums2))

nums3 = [1,1,1,3,3,4,3,2,4,2] #True
# print(contains_duplicate(nums3))

# V1 Q2
"""
P:
Go through the list and see how many occurences of val and we'll know how many _ to append to the list
Go through the list again and pop the integers that are equal to val 
Append the # of _
"""

def remove_element(nums, val):
    count_val = 0

    index_val = []
    for i in range(len(nums)):
        if val == nums[i]:
            count_val += 1
            index_val.append(i)


    for i in reversed(index_val):
        nums.pop(i) 

    for i in range(count_val):
        nums.append("_")
    print(nums)
    return len(nums) - count_val

arr = [3,2,2,3]
print(remove_element(arr, 3))



    
        