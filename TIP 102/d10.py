# 7/2/26

"""
Set1, #1
UNDERSTAND:
> Input: villager instance
> Output: list of common friends
> Edge cases: either friends attribute is [] -> []
MATCH:
Set
PLAN:
Shorter way:
Union sets of both friends lists

longer way:
create empty lst
create set from a villager's friends attribute
go through the other villager's list:
  if friend is in the set
return lst
"""

class Villager:
  def __init__(self, name, species, catchphrase):
      self.name = name
      self.species = species
      self.catchphrase = catchphrase
      self.friends = []

  def get_mutuals(self, new_contact):
    common_friends = set(self.friends) & set(new_contact.friends)
    ret = []
    for friend in common_friends:
       ret.append(friend.name)
    return ret
       
bob = Villager("Bob", "Cat", "pthhhpth")
marshal = Villager("Marshal", "Squirrel", "sulky")
ankha = Villager("Ankha", "Cat", "me meow")
fauna = Villager("Fauna", "Deer", "dearie")
raymond = Villager("Raymond", "Cat", "crisp")
stitches = Villager("Stitches", "Cub", "stuffin")

bob.friends = [stitches, raymond, fauna]
marshal.friends = [raymond, ankha, fauna]
# print(bob.get_mutuals(marshal))

ankha.friends = [marshal]
# print(bob.get_mutuals(ankha))


"""
Set 1, #2
"""

class Node:
  def __init__(self, value, next=None):
      self.value = value
      self.next = next


# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

kk_slider = Node("K.K. Slider")
harriet = Node("Harriet")
saharah = Node("Saharah")
isabelle = Node("Isabelle")

kk_slider.next = harriet
harriet.next = saharah
saharah.next = isabelle

# print_linked_list(kk_slider)

# Set 1, #3
def add_first(head, task):
  new_Task = Node(task)
  new_Task.next = head
  head = new_Task
  return head

task_1 = Node("shake tree")
task_2 = Node("dig fossils")
task_3 = Node("catch bugs")
task_1.next = task_2
task_2.next = task_3


# Linked List: shake tree -> dig fossils -> catch bugs
print_linked_list(add_first(task_1, "check turnip prices"))

# Se1, #4
def halve_list(head):
  current = head
  while current:
    current.value = current.value / 2
    current = current.next
  return head
     
node_one = Node(5)
node_two = Node(6)
node_three = Node(7)
node_one.next = node_two
node_two.next = node_three

# Input List: 5 -> 6 -> 7
# print_linked_list(halve_list(node_one))

# Set1, #5
def delete_tail(head):
  current = head
  while current.next.next:
     current = current.next
  current.next = None
  return head
     
butterfly = Node("Common Butterfly")
ladybug = Node("Ladybug")
beetle = Node("Scarab Beetle")
butterfly.next = ladybug
ladybug.next = beetle

# Input List: butterfly -> ladybug -> beetle
# print_linked_list(delete_tail(butterfly))
     
# Set 1, #6
def find_min(head):
  min_val = head.value
  curr = head
  while curr:
    if curr.value < min_val:
      min_val = curr.value
    curr = curr.next
  return min_val
     
head1 = Node(5, Node(6, Node(7, Node(8))))
head2 = Node(8, Node(5, Node(6, Node(7))))

# Linked List: 5 -> 6 -> 7 -> 8
# print(find_min(head1))

# Linked List: 8 -> 5 -> 6 -> 7
# print(find_min(head2))

"""
 Set 1, #8
UNDERSTAND:
> Input: head of a linked list
> Output: head of the modified linked list
> Edge cases: head = None -> None
MATCH:
Iterate the linked list
PLAN:
Iterate to the last element
set last element.next to the first element
and set head to be the new first element
"""

def tail_to_head(head):
  current = head
  last_node = head
  while current.next.next:
    current = current.next
  last_node = current.next 
  current.next = None
  last_node.next = head
  head = last_node
  return head
  
daisy = Node("Daisy")
mario = Node("Mario")
toad = Node("Toad") 
peach = Node("Peach")
daisy.next = mario
mario.next = toad
toad.next = peach

# Linked List: Daisy -> Mario -> Toad -> Peach
# print_linked_list(tail_to_head(daisy))

# Set 1, #9
class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

head = Node("Isabelle")
tail = Node("K.K. Slider")

head.next = tail
tail.prev = head
# print(head.value, "<->", head.next.value)
# print(tail.prev.value, "<->", tail.value)

# Set 1, #10
def print_reverse(tail):
  current = tail
  while current:
    print(current.value, end=" ")
    current = current.prev
isabelle = Node("Isabelle")
kk_slider = Node("K.K. Slider")
saharah = Node("Saharah")
isabelle.next = kk_slider
kk_slider.next = saharah
saharah.prev = kk_slider
kk_slider.prev = isabelle

# Linked List: Isabelle <-> K.K. Slider <-> Saharah
# print_reverse(saharah)