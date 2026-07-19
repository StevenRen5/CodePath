# 7/16/26: Binary seaarch and Divide & Conquer

"""
Linked List Problem:

Write a function that deletes the middle node of a singly linked list and returns the head. If the list has an even number of nodes, delete the second middle node.
Input: head = [1, 2, 3, 4, 5]
Output: [1, 2, 4, 5]
Input: head = [1, 2, 3, 4, 5, 6]
Output: [1, 2, 3, 5, 6]
"""

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return 
        current = self.head
        # while loop brings us to the last element 
        while current.next:
            current = current.next
        current.next = new_node
    
    def print(self):
        curr = self.head
        while curr:
            print(curr.value, " -> ", end="")
            curr = curr.next
        print()

lst1 = [1, 2, 3, 4, 5]
linkedlst = LinkedList()
for value in lst1:
    linkedlst.add(value)
# linkedlst.print()

lst2 = [1, 2, 3, 4, 5, 6]
linkedlst2 = LinkedList()
for value in lst2:
    linkedlst2.add(value)
# linkedlst2.print()

def del_mid_node(head):
    slow = head
    fast = head
    prev = None
    
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    prev.next = prev.next.next
    return head

del_mid_node(linkedlst.head)
linkedlst.print()
del_mid_node(linkedlst2.head)
linkedlst2.print()

"""
Set1, #1
UNDERSTAND: Do binary search to find vacation length in cruise_lengths
> Input: a list of lengths, and a target length
> Output: True/False
> Edge cases: If cruise_lengths == 0: return False
MATCH: binary search
PLAN: 
low and high index pointer
constantly calculate our midpoint from low and high
check if midpoint value is our target
if it is, return True
if not --> check midpoint value > target:
    high = midpoint - 1
else:
    low = midpoint + 1
"""

def find_cruise_length(cruise_lengths, vacation_length):
    low = 0
    high = len(cruise_lengths) - 1

    while low <= high:
        midpoint = (low + high) // 2
        if cruise_lengths[midpoint] == vacation_length:
            return True
        elif cruise_lengths[midpoint] > vacation_length:
            high = midpoint - 1
        else:
            low = midpoint + 1
    
    return False

# print(find_cruise_length([9, 10, 11, 12, 13, 14, 15], 13))

# print(find_cruise_length([8, 9, 12, 13, 13, 14, 15], 11))


"""
Set1, #2
UNDERSTAND:
> Input: list of integers, sorted in ascending order, and integer
> Output: index integer
> Edge cases: [] -> 1
MATCH:
recursive function
PLAN:

"""

def helper(cabins, preferred_deck, left, right):
    if left > right:
        return left
    
    mid = (left+right)//2
    if cabins[mid] == preferred_deck:
        return mid
    elif cabins[mid] > preferred_deck:
        return helper(cabins, preferred_deck, left, mid-1)
    else:
        return helper(cabins, preferred_deck, mid+1, right)


def find_cabin_index(cabins, preferred_deck):
    return helper(cabins, preferred_deck, 0, len(cabins)-1)
        


# print(find_cabin_index([1, 3, 5, 6], 5))
# print(find_cabin_index([1, 3, 5, 6], 2))
# print(find_cabin_index([1, 3, 5, 6], 7))