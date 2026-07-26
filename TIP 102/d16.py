# 7/23/26 Binary Trees I

from collections import deque 

# Tree Node class
class TreeNode:
  def __init__(self, value, key=None, left=None, right=None):
      self.key = key
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
Set1, #1 Monstera Madness
UNDERSTAND:
> Input: root of binary tree, each node is the number of splits in a leaf
> Output: integer that counts the number of leaves that have an odd number of splits (nodes with an odd value)
> Edge cases: null/empty root node
MATCH: inorder traversal
PLAN: inorder traversal 
# if current.val --> odd: 1 + recursive calls
REVIEW:
EVALUATE: 
"""

def count_odd_splits(root):
    if root is None:
        return 0
    if root.val % 2 == 1:
        return 1 + count_odd_splits(root.left) + count_odd_splits(root.right)
    else:
        return count_odd_splits(root.left) + count_odd_splits(root.right)
    
values = [2, 3, 5, 6, 7, None, 12]
monstera = build_tree(values)

# print(count_odd_splits(monstera))
# print(count_odd_splits(None))

"""
Set1, #2 Flower Finding
UNDERSTAND:
> Input: root of bst inventory, string target flower name
> Output: boolean value, true if name is a value for any node in inventory, false otherwise
> Edge cases: empty inventory --> return False
MATCH: binary search problem 
PLAN: 
REVIEW:
EVALUATE: 
"""
def find_flower(inventory, name):
    if inventory is None: 
        return False
    if inventory.val == name:
        return True
    if inventory.val < name:
        return find_flower(inventory.right, name)
    if inventory.val > name:
        return find_flower(inventory.left, name)

# time: O(log n), space: O(1)
"""
         Rose
        /    \
      Lilac   Tulip
     /  \       \
  Daisy  Lily  Violet
"""

# using build_tree() function at top of page
values = ["Rose", "Lilac", "Tulip", "Daisy", "Lily", None, "Violet"]

garden = build_tree(values)

# print(find_flower(garden, "Lilac"))  
# print(find_flower(garden, "Sunflower")) 

"""
Set1, #3 Flower Finding II
UNDERSTAND:
> Input: root of a binary tree (inventory), string (name)
> Output: boolean value
> Edge cases: empty inventory --> return False
MATCH:
inorder binary tree traversal
PLAN:
REVIEW:
EVALUATE: 

Question:
1. we don't check the left or right node while traversing based on current node.val. Instead, we check both left and right children.
2. O(n) time for non_bst b/c we're checking all the nodes. O(logn) for bst b/c we split in half each check.
3. The O(logn) time sol would become O(n) instead.
"""
def non_bst_find_flower(root, name):
    if root is None:
        return False
    
    if root.val == name:
        return True

    return non_bst_find_flower(root.left, name) or non_bst_find_flower(root.right, name)

"""
Set1, #4 Adding a New Plant to the Collection
UNDERSTAND: Want to insert a node where the value belongs alphebetically
> Input: Root of BST and a string 
> Output: Root of BST
> Edge cases: if a node with the inserted value already exists --> 
#    add new node in existing node's right subtree
MATCH: Binary Search Tree problem
PLAN:
REVIEW:
EVALUATE: 
"""

def add_plant(collection, name):
    if collection is None:
        return TreeNode(name)
    if collection.val == name:
        collection.right = TreeNode(name)
        return
    elif collection.val < name:
        collection.right = add_plant(collection.right, name)
    elif collection.val > name:
        collection.left = add_plant(collection.left, name)
    
    return collection
    
"""
            Money Tree
        /              \
None    Snake Plant
"""

# Using build_tree() function at the top of page
values = ["Money Tree", "Fiddle Leaf Fig", "Snake Plant"]
collection = build_tree(values)

# Using print_tree() function at the top of page
print_tree(add_plant(collection, "Aloe"))
  
"""
Set1, #5
UNDERSTAND: 
> Input: root collection
> Output: array of tuples (key, val)
> Edge cases: if none, return arr
MATCH:inorder traversal
PLAN: init arr
inorder traversal: compare key with each key in arr, add node to arr as a tuple
REVIEW:
EVALUATE: 
"""
def sort_plants(collection):
    if collection is None:
        return []
    left = sort_plants(collection.left)
    tup = (collection.val, collection.key)
    right = sort_plants(collection.right)
    return left + [tup] + right


"""
         (3, "Monstera")
        /               \
   (1, "Pothos")     (5, "Witchcraft Orchid")
        \                 /
  (2, "Spider Plant")   (4, "Hoya Motoskei")
"""

# Using build_tree() function at the top of page
values = [(3, "Monstera"), (1, "Pothos"), (5, "Witchcraft Orchid"), None, (2, "Spider Plant"), (4, "Hoya Motoskei")]
collection = build_tree(values)

print(sort_plants(collection))