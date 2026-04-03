# 4/2/26 

""" Demo 1
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
Examples:
Input: s = "leetcode"
Output: 0
Input: s = "loveleetcode"
Output: 2
Input: s = "aabb"
Output: -1

"""

def findFirstUnique(s):
    unique_chars = {}

    # for char in s:
    #     if char not in unique_chars:
    #         unique_chars[char] = char
    #     else:
    #         return unique_chars[char]
    
Input = "leetcode"
# Output: 0
# Input: s = "loveleetcode"
# Output: 2
# Input: s = "aabb"
# Output: -1

input = "leetcode"
# print(findFirstUnique(input))

""" Demo 2
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Understand:
Give two sorted linked lists list1 & list2 
Merge two lists into one sorted list 
return head of merged linked list
Restriction: use existing node. Allow changing .next except one dummy helper node

Plan:
List1's head to be returned and we'll use values of list2 to add to list1

"""

class Node:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

def mergeSortedLists(list1, list2):
    curr1 = list1
    curr2 = list2

    # current = 

    # while 

# a = Node(1)
# b = Node(3)
# c = Node(5)
# a.next = b
# b.next = c

# x = Node(2)
# y = Node(4)
# z = Node(6)
# x.next = y
# y.next = z

# newList = mergeSortedLists(a, x)
# while(newList):
#     print(newList.val)
#     newList = newList.next

# V1 Q1
def is_circular(head):
    current = head
    while current:
        if current.next == head:
            return True
        current = current.next
    return False

# circular list is more than just a cycle - specifically connecting the first and last nodes.
# a -> b -> c -> d -> a
a = Node(1)
b = Node(3)
c = Node(5)
d = Node(7, a) 
a.next = b
b.next = c
c.next = d
# print(is_circular(a)) 

# V1 Q2
def find_last_node_in_cycle(head):
    current = head
    seen_node = [head]

    while current:
        print(seen_node)
        if current.next not in seen_node:
            seen_node.append(current.next)
        elif current.next in seen_node:
            return current
        current = current.next
    return None

# print(find_last_node_in_cycle(a))

# V1 Q3

"""
U: Given head of a linked list, these nodes have values. 
We want to partition a linked list around val and compare them if they are
less than or greater than or equal to
Output: linked list in order after comparing (less than and greater than
and equal to)

# Example:
Input: 1 -> 4 -> 3 -> 2 -> 5 -> 2
head = 1, val = 3
1 -> 2 -> 2 -> 4 -> 3 -> 5

P: have a temp head can be used as like previous
during certain partitions we update previous and head accordingly
so if the val is less than, update temp
if val is greater than, update head


I:
"""


# Example:
# Input: 1 -> 4 -> 3 -> 2 -> 5 -> 2
# head = 1, val = 3
# Output: 1 -> 2 -> 2 -> 4 -> 3 -> 5 OR 2 -> 2 -> 1 -> 5 -> 4 -> 3

def partition(head, val): # 1 -> 2 -> 4
    temp = Node(0)
    temp.next = head 

    # traverse list
    previous = temp 
    current = head # 1-> 2 -> 4
    while current:
        if current.val < val: # 1 < 4
            

            

            
