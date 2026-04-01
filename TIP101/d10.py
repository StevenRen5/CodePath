# 3/31/26 

"""Instructor Demo & fast-slow pointer technique
Write a function to find the middle node of a singly linked list. If the list has an even number of nodes, return the second middle node.
Examples:
Input: head = [1, 2, 3, 4, 5]
Output: Node with value 3
Input: head = [1, 2, 3, 4, 5, 6]
Output: Node with value 4

Understand: 
can't go backwards
maybe keep track of head, maybe need a counter, maybe 2 pointers
input: head node
output: middle node (not the value)
may be some edge cases, NONE, check if head has a value, 

Match:
navigating through linked list, find middle (fixed point, need to know how long linked list is / go to the end). how do i get back?
head node

two pointers -> middle  = 1/2. slow = 1, fast = 2.

Plan:
1. working with head node, keep track in the beginning (can delete if we dont need)
2. make 2 pointers (slow and fast), start all our nodes at Head.
3. fast is move 2x faster than slow to give us middle.
4. we only know the middle when fast reaches the end 
5. return the node object (not value)
"""
class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def print_linked_list(head):
    current = head
    while current != None:
        print(current.value, "->", end=" ")
        current = current.next

def findMiddleNode(head):

    if head == None:
        return None

    # bruteforce approach 
    # tempHead = head
    # count = 1
    slow = head
    fast = head

    # how do we know we've reached the end
    while (fast is not None and fast.next is not None): # two conditions to deal with even or odd linked list length
        fast = fast.next.next # no error since we've checked in the while loop
        slow = slow.next
    return slow 


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
# f = Node(6)

a.next = b
b.next = c
c.next = d
d.next = e
# e.next = f
# print(findMiddleNode(a).value)

# V1 Q1

# 4 -> 3 -> 2
head = Node(4, Node(3, Node(2)))
# print_linked_list(head)

# V1 Q2
# Input List: 3 -> 1 -> 2 -> 1
# Input: head = 3, val = 1
# Output: 2
def count_element(head, val):
    count = 0
    cur = head
    while cur:
        if cur.value == val:
            count += 1
        cur = cur.next
    return count
 
# head = Node(3, Node(1, Node(2, Node(1))))
# print(count_element(head, 1))

# V1 Q3
        
# Helper function to print the linked list
def print_list(node):
    current = node
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

# I have a bug! 
def remove_tail(head):
    if head is None: # If the list is empty, return None
        return None
    if head.next is None: # If there's only one node, removing it leaves the list empty
        return None 
		
	# Start from the head and find the second-to-last node
    current = head
    while current.next.next: # checks to see there's two more nodes after current. If not the curr is 2nd to last node.
        current = current.next

    current.next = None # Remove the last node by setting second-to-last node to None
    return head

# head = Node(1, Node(2, Node(3, Node(4))))
# print_list(head)
# head = remove_tail(head)
# print_list(head)

# V1 Q5
# fast-slow pointers method
# Push elements from s to n/2 elements to stack. 
# Pop element from S to the end while comparing. If different, return false.
def is_palindrome(head):
    stack = []
    slow = head
    fast = head
    
    if head == None:
        return None
    
    while (fast is not None and fast.next is not None):
        stack.append(slow.value)
        fast = fast.next.next 
        slow = slow.next

    if fast != None:
        slow = slow.next
    
    while slow != None:
        if slow.value != stack.pop():
            return False
        slow = slow.next
    return True

# head = Node(1, Node(2, Node (1)))
head = Node(1, Node(2, Node (2, Node(1))))
# print(is_palindrome(head))

# Stack = [1,2,2]
# 1 -> 2 -> 2 -> 3 -> 2 -> 2 -> 1
#                S              
#                          F                             
# [1,2]
# 1 -> 2 -> 2 -> 0
#                S     
#                F  


#V1 Q6
# two pointers - curr, prev
# h
# 1 -> 2 -> 3 <- 4

def reverse(head):

    if head == None:
        return None
    if head.next == None:
        return head
    
    current = head.next # 2nd node
    prev = head # 1st node 
    prev.next = None # since this 1st node will be the last node of the reversed list, set it to none

    while current:
        temp = current
        current = current.next
        temp.next = prev
        prev = temp

    return prev
    
head = Node(1, Node(2, Node(3, Node(4))))
# head = Node(1, Node(2))
print_list(reverse(head))