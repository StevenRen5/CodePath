# 7/28/26 Binary Trees II

"""
Full binary tree
.. copy from Ram notes
"""

from collections import deque 

# Tree Node class
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root

"""
Set1, #1
UNDERSTAND:
> Input: two binary trees
> Output: return root of combined single binary tree with overlappign nodes b being usmmed
> Edge cases: empty tree, if they share nodes in the sam eplace add, None is used as a placeholder for an empty node
MATCH: binary tree
PLAN: 
    - create a new root of a new tree
    - start at root, access the left of each tree, if one of the nodes is none
    we can use the non non evalue for the new node in our tree
    - if both are not none, then we sum the values and make that the new node
REVIEW:
EVALUATE: time complexity o(m + n), space: o(m + n)
"""


"""
     1             2         
    /  \         /   \       
   3    2       1     3   
 /               \      \   
5                 4      7   
"""
def merge_orders(order1, order2):
    if order1 is None and order2 is None:
        return None

    new_root = TreeNode()

    if order1 is None and order2 is not None:
        new_root.val = order2.val
        new_root.left = merge_orders(None, order2.left)
        new_root.right = merge_orders(None, order2.right)
    elif order1 is not None and order2 is None:
        new_root.val = order1.val
        new_root.left = merge_orders(order1.left, None)
        new_root.right = merge_orders(order1.right, None)
    elif order1 and order2:
        new_root.val = order1.val + order2.val
        new_root.left = merge_orders(order1.left, order2.left)
        new_root.right = merge_orders(order1.right, order2.right)

    return new_root



# Using build_tree() function included at top of page
cookies1 = [1, 3, 2, 5]
cookies2 = [2, 1, 3, None, 4, None, 7]
order1 = build_tree(cookies1)
order2 = build_tree(cookies2)

# Using print_tree() function included at top of page
print_tree(merge_orders(order1, order2))

"""
Set1, #2
UNDERSTAND:
> Input: a binary tree with puff that represents flavor of cream
> Output: the list of the flavors in a level order
> Edge cases: 
1. empty tree
MATCH:
PLAN:
1. initialize deque (-> queue)
2. using while loop, traverse next level nodes
3. append val to result list
REVIEW:
EVALUATE: 
"""

class Puff():
     def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def print_design(design):
    res = []
    q = deque([design])
    
    while q:
        curr = q.popleft()
        res.append(curr.val)
        
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)
            
    print(res)

"""
            Vanilla
           /       \
      Chocolate   Strawberry
      /     \
  Vanilla   Matcha  
"""
croquembouche = Puff("Vanilla", 
                    Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
                    Puff("Strawberry"))
# print_design(croquembouche)

"""
Set1, #4
UNDERSTAND: 
> Input: root of a binary tree - called cake
> Output: integer - representing the maximum height of the binary tree
> Edge cases: root = None -> return 0
MATCH:
binary tree
PLAN:
- create a recursive helper function that's going to take in the root's left or right subtree
- base case: if root == None -> return 0
- recursive step: return 1 + max(recursive_function(root.left), recursive_function(root.right)
REVIEW: 
EVALUATE: o(n) time, o(logn) space
Using DFS, implemented recursively, we have go from the root to the very left. The maximum # of recursive function we add to stack is logn (height of tree).
"""
def max_tiers(cake):
  if cake is None:
    return 0
  return 1 + max(max_tiers(cake.left), max_tiers(cake.right))

"""
        Chocolate
        /        \
    Vanilla    Strawberry
                /     \
         Chocolate    Coffee
"""
# Using build_tree() function included at top of page
cake_sections = ["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Coffee"]
cake = build_tree(cake_sections)

# print(max_tiers(cake))

"""
Set1, #4
UNDERSTAND: 
> Input: root of a binary tree - called cake
> Output: integer - representing the maximum height of the binary tree
> Edge cases: root = None -> return 0
MATCH:
binary tree (BFS)
PLAN:
1. initialize q (deque)
2. initialize max_level
3. using while loop, traverse nodes in a level order
4. after traversing the nodes in current level, increase max_lever by 1

REVIEW: 
EVALUATE: o(n) time, o(n) space
Using BFS, for a balanced binary tree, there will be n/2 nodes in the queue after appending the last node in the second to last level. O(n) spac.
"""
def max_tiers(cake):
    q = deque([cake])
    max_level = 0
    
    while q:        
        for _ in range(len(q)):
            curr = q.popleft()
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
                
        max_level += 1
        
    return max_level

"""
        Chocolate
        /        \
    Vanilla    Strawberry
                /     \
         Chocolate    Coffee
"""
# Using build_tree() function included at top of page
cake_sections = ["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Coffee"]
cake = build_tree(cake_sections)

print(max_tiers(cake))