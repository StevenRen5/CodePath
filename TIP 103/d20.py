# 11/19/26 - Binary Trees

from collections import deque 

# Tree Node class
class TreeNode:
    def __init__(self, value, left=None, right=None):
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
> Input: design - root of a binary tree
> Output: list of list, where the element list is the nodes on a level
> Edge cases:
MATCH:
PLAN:
create an empty list res


create an interior array for the node found in that level

start at 0
condition checking the length of the res arr
create subarray when finished with the level

REVIEW:
EVALUATE: 
O
"""

class Puff():
     def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def listify_design(design):
    res = []
    # BFS recursion
    
    def bfs(node, level):
        # level = 0, at root, and res = []
        if level == len(res): # on a new level
          res.append([])

        res[level].append(node.val)

        if node.left:
            bfs(node.left, level + 1)
        if node.right:
            bfs(node.right, level + 1)


    bfs(design, 0)
    # ['Vanilla', 'Chocolate', 'Vanilla', 'Matcha', 'Strawberry']

    # BFS iteratively:
    # q = deque([design])
    # while q:
    #   level_list = []
    #   for i in range(len(q)):
    #     curr = q.popleft()
    #     level_list.append(curr.val)
    #     if curr.left:
    #       q.append(curr.left)
    #     if curr.right:
    #       q.append(curr.right)
    #   res.append(level_list)

    return res


"""
            Vanilla
           /       \
      Chocolate   Strawberry
      /     \
  Vanilla   Matcha  
"""
# croquembouche = Puff("Vanilla", 
#                     Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
#                     Puff("Strawberry"))
# print(listify_design(croquembouche)) # [['Vanilla'], ['Chocolate', 'Strawberry'], ['Vanilla', 'Matcha']]


"""
Set1, #2
UNDERSTAND:
> Input: cupcakes - root of a binary tree
> Output: list of list (elements in each row)
> Edge cases:
MATCH: BFS - for loop for level nodes, flag for zigzagness
PLAN:

level = 0 (update thru recursion. if lvl is even, start left. if odd, start right)
if left is true
|_start bfs with recurse(left)
else
|_ start bfs with recurse(right)

REVIEW:
EVALUATE: 
"""

def zigzag_icing_order(cupcakes):
    res = []
    def bfs(node, level):
        if node is None:
            return 
        
        # res.append(node.val)
        
        # if level % 2 == 0:
        #     bfs(node.right, level + 1)
        #     bfs(node.left, level + 1)
        # else:
        #     bfs(node.left, level + 1)
        #     bfs(node.right, level + 1) 
    
    bfs(cupcakes, 0)        
  
    return res


"""
            Chocolate
           /         \
        Vanilla       Lemon
       /              /    \
    Strawberry   Hazelnut   Red Velvet   
"""
# Using build_tree() function included at top of page
flavors = ["Chocolate", "Vanilla", "Lemon", "Strawberry", None, "Hazelnut", "Red Velvet"]
cupcakes = build_tree(flavors)
print(zigzag_icing_order(cupcakes))  # ['Chocolate', 'Lemon', 'Vanilla', 'Strawberry', 'Hazelnut', 'Red Velvet']
