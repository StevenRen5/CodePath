# 7/21/26 Binary trees

class Node:
  def __init__(self, value, next=None):
      self.value = value
      self.next = next

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left # smaller value
    self.right = right # greater value

def insert(root, val):
  if root is None:
    return TreeNode(val)
   # if value is less than root, go left
  if val < root.val:
    root.left = insert(root.left, val)
  # if value is greater than root, go right
  else:
    root.right = insert(root.right, val)
  return root


def inorder(root):
  if root is None:
    return []
  return inorder(root.left) + [root.val] + inorder(root.right)
  # preorder: val in beginning
  # postoder: val at the end

root = None
l1 = [5,3,1,4,6,9]
for val in l1:
  root = insert(root, val)

# print(inorder(root))

"""
UNDERSTAND:
> Input: root of a BST, node to del
> Output: root of BST after deletion
> Edge cases:
- key not found 
- root is none
- deleting the root
MATCH:
- BST property
PLAN:
- if key < root.val -> delete from left subtree
- if key > root.val -> delete from right subtree
REVIEW:
EVALUATE: 
"""
def get_min(node):
  while node.left:
    node = node.left
  return node


def del_node(root, key):
  if root is None:
    return None
  
  if key < root.val:
    root.left = del_node(root.left, key)
  elif key > root.val:
    root.right = del_node(root.right, key)
  else:
    # case 2 (also secretly case 1)
    if root.left is None:
      return root.right
    if root.right is None:
      return root.left
    
    # case 3: node has two children
    successor = get_min(root.right)
    root.val = successor.val
    root.right = del_node(root.right, successor.val)

  return root

newroot = del_node(root, 4)
# print(inorder(newroot))

"""
Set1, #1
UNDERSTAND:
> Input: treenode class, root of the tree
> Output: a created tree
> Edge cases: empty tree
MATCH: binary tree
PLAN:
  - we created nodes and then assigned the appropriate left and rights
REVIEW:
EVALUATE: 
"""
from collections import deque  

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



root = TreeNode("Trunk")
root.left = TreeNode("Mcintosh")
root.left.left = TreeNode("Fuji")
root.left.right = TreeNode("Opal")
root.right = TreeNode("Granny Smith")
root.right.left = TreeNode("Crab")
root.right.right = TreeNode("Gala")

# Using print_tree() included at the top of this page
# print_tree(root)

"""
Set1, #2
UNDERSTAND:
> Input: root of a tree
> Output: calculated value
> Edge cases: 
MATCH:
binary tree
PLAN:
- grab the root's left and right childrens
- apply the operation using the root node
REVIEW: prints 12, works.
EVALUATE: O(1) time, space complexity
"""

def calculate_yield(root):
  if root.val == "+":
    return root.left.val + root.right.val
  elif root.val == "-":
    return root.left.val - root.right.val
  elif root.val == "*":
    return root.left.val * root.right.val
  elif root.val == "/" and root.right.val != 0:
    return root.left.val / root.right.val
  else:
    return None

apple_tree = TreeNode("+", TreeNode(7), TreeNode(5))
# print(calculate_yield(apple_tree))




"""
Set1, #3
UNDERSTAND:
> Input: TreeNode / root of binary tree
> Output: list of path from root to righmost node in tree
> Edge cases: root is None, return None
MATCH:
- binary tree
PLAN:
- start from root 
- move to right and print until we get right child as None
REVIEW: 
EVALUATE: O(H) time,space complexity
"""

# def right_vine(root):
#   if root is None:
#     return None
#   if root.right is None:
#     return [root.val]

#   path = []
#   # path.add(root.val)

#   while root.right:
#     path.append(root.val)
#     root = root.right
  
#   path.append(root.val)

#   return path


ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

# print(right_vine(ivy1))
# print(right_vine(ivy2))

"""
Set1, #4
UNDERSTAND:
> Input: root of the tree
> Output: list of the roots taken to get to the right most
> Edge cases: root is None
MATCH: binary tree
PLAN:
- edge cases for if the root is none, return none
- is root.right doesn't exist, we return the root
- create our list, list would eb an added parameter
- base:
- root.right is None, we return list with the added root of where we are
- add the root we are currently at the our list
- return right_vine(root.right)
REVIEW: works
EVALUATE: O(H), time and space complexity
"""
path = []

def right_vine(root):
  if root is None:
    return []
  return [root.val] + right_vine(root.right)

ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))
path = []
# print(right_vine(ivy1))
path = []
ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))
# print(right_vine(ivy2))

"""
Set1, #5
UNDERSTAND:
> Input: root of a binary tree
> Output: integer - representing how many leaf nodes we have
> Edge cases: root is None -> 0
MATCH:
binary tree
PLAN:
- go through the left and right child repeatedly and check if left and right child exist. If both doesn't we return a node.
REVIEW:
EVALUATE: 
"""

def count_leaves(root):
  if root is None:
    return 0
  if root.left == None and root.right == None:
    return 1
  return count_leaves(root.left) + count_leaves(root.right)


"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""

oak1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

"""
      Root
      /  
    Node1
    /
  Leaf1  
"""
oak2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

print(count_leaves(oak1))
print(count_leaves(oak2))

