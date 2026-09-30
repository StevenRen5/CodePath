# 9/29/26: Recursion, Stacks, Queues & OOP


#1
def count_layers(sandwich):
    length = len(sandwich)
    
    if length <= 1:
        return 1
    
    return 1 + count_layers(sandwich[1])

sandwich1 = ["bread", ["lettuce", ["tomato", ["bread"]]]]
sandwich2 = ["bread", ["cheese", ["ham", ["mustard", ["bread"]]]]]

# print(count_layers(sandwich1))
# print(count_layers(sandwich2))

#2
def reverse_orders(orders):
    """Return the orders in reverse order using recursion."""
    def helper(index):
        if index < 0:
            return []
        return [order_list[index]] + helper(index - 1)
    order_list = orders.split()
    return " ".join(helper(len(order_list) - 1))

# Example Usage:
# print(reverse_orders("Bagel Sandwich Coffee"))


#4
# a1 -> b1 -> a2 -> b2 -> a3 -> b3 -> ...
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

def merge_orders(sandwich_a, sandwich_b):
  if not sandwich_a and not sandwich_b:
      return None
  elif not sandwich_a:
      return sandwich_b
  elif not sandwich_b:
      return sandwich_a
  # both nodes are not None

  # save original head
  head = sandwich_a

  # save next nodes before changing pointers to current a's and b's nodes
  a_next = sandwich_a.next
  b_next = sandwich_b.next

  # Connecting A1 -> B1 -> A2 
  sandwich_a.next = sandwich_b
  sandwich_b.next = a_next

  merge_orders(a_next, b_next)

  return head

sandwich_a = Node('Bacon', Node('Lettuce', Node('Tomato')))
sandwich_b = Node('Turkey', Node('Cheese', Node('Mayo')))
sandwich_c = Node('Bread')

# print_linked_list(merge_orders(sandwich_a, sandwich_b))
print_linked_list(merge_orders(sandwich_a, sandwich_c))


  




    

