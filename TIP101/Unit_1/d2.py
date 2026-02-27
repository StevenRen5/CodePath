# 2/26
# Instructor Demo

# create structure of function including input & output
# create a new list to be returned
# iterate through list of nums, for loop
# if statement, check against threshold
# return new list

# Input: lst = [8,2,13,11,4,10,14], threshold = 10
# Output: [13,11,14]

def above_threshold(nums, threshold):
    final_list = []

    for num in nums:
        if num > threshold:
            final_list.append(num)

    return final_list

print("Test run", above_threshold([8,2,13,11,4,10,14], 10))

# Q1
def print_list(lst):
    for i in lst:
        print(i)

lst = ["squirtle", "gengar", "charizard", "pikachu"]
print_list(lst)

# Q2

def doubled(lst):
    for num in lst:
        print(num * 2)

lst = [1,2,3]
doubled(lst)

# Q3
def doubled(lst):
    new_lst = []
    for num in lst:
        new_lst.append(num * 2)
    return new_lst

lst = [1,2,3]
print(doubled(lst))


# Q4
def flip_sign(lst):
    flip_list = []
    for i in lst:
        flip_list.append(i * -1)
    return flip_list

lst = [1,-2,-3,4]
print(flip_sign(lst))

# Q5

def max_difference(lst):

    low = lst[0]
    high = lst[0]

    for num in lst:
        if num < low:
            low = num
        if num > high:
            high = num

    max_diff = high - low
    return max_diff

lst = [5,22,8,10,2]
print(max_difference(lst))


# Q6

def count_less_than(numbers, threshold):
    counter = 0
    for i in numbers:
        if i < threshold:
            counter += 1
    return counter

numbers = [12,8,2,4,4,10]
threshold = 5
print(count_less_than(numbers, threshold))

# Q7 
def get_evens(lst):
    even_list = []
    for num in lst:
        if num % 2 == 0:
            even_list.append(num)
    return even_list

lst = [1,2,3,4]
print(get_evens(lst))

# Q8
def multiples_of_five():

    for num in range(1, 101):
        if num % 5 == 0:
            print(num)

multiples_of_five()


# Q9
def find_divisors(n):
    lst = []
    for i in range(1, n+1):
        if n % i == 0:
            lst.append(i)
    return lst

lst = find_divisors(6)
print(lst)

# Q10

def fizzbuzz(n):
    for num in range(1,n+1):
        if num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

fizzbuzz(13)

# Q11
def print_indices(lst):
    for i in range(len(lst)):
        print(i)

# Q12
def linear_search(lst, target):
    index = -1

    for i in range(len(lst)):
        if lst[i] == target:
            index = i
    return index

lst_12 = [1,4,5,2,8]
print(linear_search(lst_12,5))



# print(Q#, )
