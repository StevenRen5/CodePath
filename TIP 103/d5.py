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
# a1 -> a2 -> a3  
# b1 -> b2 -> b3  
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

def merge_orders(a,b):
    if not a and not b:
        return None
    elif not a:
       return b
    elif not b:
       return a
    # both a,b not none
    head = a
    """
    situations:
    a1 -> a2 -> None
    b1 -> b2 -> None

    a1 -> a2 -> None
    b1 -> None

    a1 -> None
    b1 -> b2 -> None
    """
    curr_a = a
    curr_b = b
    while curr_a:
        # save the next ptrs of a,b
        next_a = curr_a.next 
        next_b = curr_b.next

        # first iteration: link a1 -> b1 -> a2
        curr_a.next = curr_b
        curr_b.next = next_a

        # covers the case when b's length > a's length
        if next_a == None:
           curr_b.next = next_b
           break
        # cover's the case when a's length > b's length
        if next_b == None:
           # we are modify a so we don't need to do any other operations
           break
           
        # update curr_a and curr_b
        curr_a = next_a
        curr_b = next_b
    return head


sandwich_a = Node('Bacon', Node('Lettuce', Node('Tomato')))
sandwich_b = Node('Turkey', Node('Cheese', Node('Mayo')))
sandwich_c = Node('Bread')

# print_linked_list(merge_orders(sandwich_a, sandwich_b))
# print_linked_list(merge_orders(sandwich_a, sandwich_c))
# print_linked_list(merge_orders(sandwich_c, sandwich_b))

def merge_orders_rec(sandwich_a, sandwich_b):
    if not sandwich_a and not sandwich_b:
        return None
    elif not sandwich_a:
        return sandwich_b
    elif not sandwich_b:
        return sandwich_a

    # save original head
    head = sandwich_a

    # save where each list continues
    next_a = sandwich_a.next
    next_b = sandwich_b.next

    sandwich_a.next = sandwich_b
    sandwich_b.next = merge_orders_rec(next_a, next_b)

    return head

sandwich_a = Node('Bacon', Node('Lettuce', Node('Tomato')))
sandwich_b = Node('Turkey', Node('Cheese', Node('Mayo')))
sandwich_c = Node('Bread')

print_linked_list(merge_orders(sandwich_a, sandwich_b))
# print_linked_list(merge_orders(sandwich_a, sandwich_c))


  




    

