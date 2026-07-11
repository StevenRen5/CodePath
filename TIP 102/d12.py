# 7/9/26 (Linked List III)

"""
Set1, #1
UNDERSTAND: 
> Input: head of linked list
> Output: boolean
> Edge cases: head = None -> False, head.next = None -> False
MATCH:
PLAN:

"""
class Node:
  def __init__(self, value, next=None):
      self.value = value
      self.next = next

def is_circular(clues):
  if not clues:
    return False
  if not clues.next:
    return False
  current = clues.next
  while current:
    if current.next == clues:
      return True
    current = current.next
  return False
     
clue1 = Node("The stolen goods are at an abandoned warehouse")
clue2 = Node("The mayor is accepting bribes")
clue3 = Node("They dumped their disguise in the lake")
clue1.next = clue2
clue2.next = clue3
clue3.next = clue1

# print(is_circular(clue1))  


"""
Set1, #2
UNDERSTAND:
> Input: head of a linked list
> Output: array of values that are part of any cycle in evidence
> Edge cases: head = none -> []
MATCH:
Slow fast technique
PLAN:
Slow fast techinque setup
Encounter a cycle. go through the cycle again and append all the elements to the array.
"""
def collect_false_evidence(evidence):
  arr = []
  slow = evidence
  fast = evidence
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

    if slow == fast:
      temp_slow = slow.next
      while temp_slow != fast:
        arr.append(temp_slow.value)
        temp_slow = temp_slow.next
      arr.append(fast.value)
      return arr
  return []

clue1 = Node("Unmarked sedan seen near the crime scene")
clue2 = Node("The stolen goods are at an abandoned warehouse")
clue3 = Node("The mayor is accepting bribes")
clue4 = Node("They dumped their disguise in the lake")
clue1.next = clue2
clue2.next = clue3
clue3.next = clue4
clue4.next = clue2

clue5 = Node("A masked figure was seen fleeing the scene")
clue6 = Node("Footprints lead to the nearby woods")
clue7 = Node("A broken window was found at the back")
clue5.next = clue6
clue6.next = clue7

print(collect_false_evidence(clue1))
print(collect_false_evidence(clue5))







