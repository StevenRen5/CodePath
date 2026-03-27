# 3/26/26 

# Write a function to reverse a singly linked list. The function should take the head of a linked list as input and return the new head of the reversed linked list.

# Examples:
# Input: head = [1 -> 2 -> 3 -> 4 -> 5]
# Output: [5 -> 4 -> 3 -> 2 -> 1]
# Input: head = [1]
# Output: [1]
# Input: head = None
# Output: None



""" 
Understand:
Input: head of a linked list
Output: head of a linked list 


Plan:
If there's one element in linkedin list, return it
If there's no element in linked list, return None

current variable for current element in linked list set to head
while loop:
    logic 
"""

class Node:
    def __init__(self, value=0, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev # this means we can. create a doubly linked list. Ignore for problems 1-8. 

def reverse_linked_list(head):
    if head == None:
        return None
    if head.next == None:
        return head
    
    current = head
    # while current != None:


e = Node("5")
d = Node("4", e)
c = Node("3", d)
b = Node("2", c)
a = Node("1", b)

# Write a function to remove all duplicate values from a sorted linked list. After removing duplicates, each element in the list should appear only once.
# Examples:
# Input: head = [1 -> 1 -> 2]
# Output: [1 -> 2]
# Input: head = [1 -> 1 -> 2 -> 3 -> 3]
# Output: [1 -> 2 -> 3]
# Input: head = []
# Output: []

""" 
Plan:
If head is empty, return none
if head's next is None, return head
Create an empty list. 
Go through linked list and append values to list that we've not seen before

Construct unique linked list:
Loop through elements in list and construct the Nodes and logic 
"""

def remove_duplicates(head):
    if head == None:
        return None
    if head.next == None:
        return head
    
    lst = []
    current = head
    while current != None:
        if current.value not in lst:
            lst.append(current.value)
        current = current.next
    
    # new_current = lst[0]
    # for num in nums:
    #     new_node = Node(num, )


# V1 Q1

class Pokemon():
  def  __init__(self, name, hp, damage):
    self.name = name
    self.hp = hp # hit points
    self.damage = damage # The amount of damage this pokemon does to its opponent every attack
    
  def attack(self, opponent):
    opponent.hp = opponent.hp - self.damage
    if opponent.hp <= 0:
      opponent.hp = 0
      print(f"{opponent.name} fainted")
    else:
      print(f"{self.name} dealt {self.damage} damage to {opponent.name}")

pikachu = Pokemon("Pikachu", 35, 20)
bulbasaur = Pokemon("Bulbasaur", 45, 30) 

opponent = bulbasaur
pikachu.attack(opponent)

# V1 Q2		
lst= ["Jigglypuff", "Wigglytuff"]

node_2 = Node("Wigglytuff")  
node_1 = Node("Jigglypuff", node_2)  

# print(node_1.value, "->", node_1.next.value)
# print(node_2.value, "->", node_2.next)

# V1 Q3

def add_first(head, new_node):
    new_node.next = head
    # head = new_node
    
# Using the Linked List from Problem 2
# print(node_1.value, "->", node_1.next.value)

# new_node = Node("Ditto")
# node_1 = add_first(node_1, new_node)

# # print(new_node.value, "->", new_node.next.value)

# # V1 Q4
# def get_tail(head):
#     if head == None:
#         return None

#     current = head
#     while current!=None:
#         if current.next==None:
#             return current.value
#         current=current.next

# # Build: num1 -> num2 -> num3
# num1 = Node("num1")
# num2 = Node("num2")
# num3 = Node("num3")
# num1.next = num2
# num2.next = num3

# head = num1
# tail = get_tail(head)   # or get_tail(num1)
# print(tail)             # expected: num3

# V1 Q5
def ll_replace(head, original, replacement):
    current = head
    while current != None:
        if current.value == original:
                current.value = replacement
        current = current.next 
    return None

# num3 = Node(5)
# num2 = Node(6, num3)
# num1 = Node(5, num2)
# # initial linked list: 5 -> 6 -> 5

# head = num1
# ll_replace(head, 5, "banana")
# # updated linked list: "banana" -> 6 -> "banana"

# num3 = Node(5)
# num2 = Node(6, num3)
# num1 = Node(5, num2)
# # initial linked list: 5 -> 6 -> 5

# head = num1
# ll_replace(head, 5, "banana")
# # updated linked list: "banana" -> 6 -> "banana"

def print_linked_list(head):
    current = head
    while current != None:
        print(current.value, "->", end=" ")
        current = current.next

# print_linked_list(num1)

# Q7
"""
Understand:
4 situations where to insert node:
First index 
Middle or Last index
> Last index

Plan:
Create a variable counter
Use while loop to loop through linked list to count the number of elements in list
If i > counter, insert new node at end of list
Otherwise
"""

def ll_insert(head, val, i):

    if i == 0:
        new_node = Node(val, head)
        head = new_node
        return head # note: after function ends, variable new_node disappears, but object remains b/c the returend head still references it. Python removes object only when nothing references it anymore.

    c = 0 # match counter with i 
    current = head # current node
    prev = None # previous node
    
    while current != None:
        if i == c: # case 2: middle or last index
            prev.next = Node(val, current)
            return head
        
        if current.next != None:
            c += 1 
        if current.next == None and i > c: #case 3: greater than last index
            current.next = Node(val)
            return head

        prev = current
        current = current.next


# num4 = Node(9)
# num3 = Node(12, num4)
# num2 = Node(8, num3)
# num1 = Node(3, num2)

# print_linked_list(ll_insert(num1, 20, 2)) # 3 -> 8 -> 20 -> 12 -> 9

# V1 Q8
"""
Understand:
input: list
output: head of a linked list
core logic: list --> linked list

Plan:
list is empty, return None
list length is 1, return a node with that value 
current node, prev node variables
for loop logic to go through each num, creat node, and linking by using prev and current node
return head

"""

def list_to_linked_list(lst):
    if len(lst) == None:
        return None
    if len(lst) == 1:
        return Node(lst[0])
    
    # lst = [1,2,3]
    head = Node(lst[0]) # 1 
    current = head
    for i in range(1, len(lst)):
        current.next = Node(lst[i])
        current = current.next
    return head
    
normal_list = ["Betty", "Veronica", "Archie", "Jughead"] # Betty -> Veronica -> Archie -> Jughead
linked_list = list_to_linked_list(normal_list)
# print_linked_list(linked_list)

# V1 Q9

poliwag = Node("poliwag")
poliwrath = Node("poliwrath")
poliwhirl = Node("poliwhirl", poliwrath, poliwag)

poliwag.next = poliwhirl
poliwrath.prev = poliwhirl

# print(poliwhirl.prev.value, "<->", poliwhirl.value, "<->", poliwhirl.next.value)

# V1 Q10
def print_reverse(tail):
    current = tail
    while current != None:
        print(current.value, end=" ")
        current = current.prev

#              (head)                       (tail)
# Linked List: Poliwag <-> Poliwhirl <-> Poliwrath
print_reverse(poliwrath)