# Advance Binary Trees
# Preorder: root > left > right (pre as root comes first)
# inorder: left > root > right (root comes middle; this will result in sorted data if we were to output values to a list)
# postorder left > right > root (post as root comes last)
# in all 3 orders, left will come before right, but the root can be the first, second, or third
# code one one of the 3 orders, can code all three. We just move the root code to the correct order.

#inorder traversal

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    # Recursive Base against current node, 
    # Because of how we are concatenating ("adding") lists, we return an empty list instead of None
    if(root is None):
        print("Parent node was leaf node, returning []")
        return []
    
    # Keeps track of the order of our current subtree (including all children trees)
    res = []
    
    print(f"Recursing to left subtree from current root: {root.val}")

    #LEFT: Recurse to left subtree and append result.
    res += inorderTraversal(root.left)

    #ROOT: Append current root, nothing to recurse here
    print(f"Appending current root: {root.val}")
    res += [root.val]

    #RIGHT: Recurse to right subtree and append result.
    print(f"Recursing to right subtree from current root {root.val}")
    res += inorderTraversal(root.right)

    # This print statement can stay unindented so it fires for both None and real nodes
    print(f"Finished with subtree with Root {root.val}: current result list: {res}")
    return res


# Let's build a binary tree with 6 nodes:
#        4
#      /   \
#     2     6
#    / \   /
#   1   3 5

# In Order: 1 2 3 4 5 6
# Pre order: 4 2 1 3 6 5
# Post order: 1 3 2 5 6 4


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)

# Run the traversal
print("--- Starting Traversal ---")
result = inorderTraversal(root)
print("--- Traversal Complete ---")

# The expected inorder (Left, Root, Right) output is [1, 2, 3, 4, 5, 6]
print("\nFinal Output:", result)


# Simplified version

# def inorderTraversalv2(root):
#     if(root is None):
#         return []
    
#     res = []
    
#     res += inorderTraversalv2(root.left)
#     res.append(root.val)
#     res +=  inorderTraversalv2(root.right)

#     return res

# result = inorderTraversalv2(root)
# print("\nFinal Output:", result)

# In Order: 1 2 3 4 5 6
# Pre order: 4 2 1 3 6 5
# Post order: 1 3 2 5 6 4


# V1 Q1

#Given the root of a binary tree, return True if the tree’s left and right subtrees are mirrors of each other (i.e., tree is symmetric around its center). Return False otherwise.

#Evaluate the time complexity of your function.


# compare left.right and right.left
# compare left.left and right.right


# sol
def helper_is_symmetric(leftRoot, rightRoot):
    if leftRoot == None and rightRoot == None:
        return True
    
    if leftRoot == None and rightRoot:
        return False
    
    if leftRoot and rightRoot == None:
        return False
    
    if leftRoot.val != rightRoot.val:
        return False
    
    return helper_is_symmetric(leftRoot.left, rightRoot.right) and helper_is_symmetric(leftRoot.right, rightRoot.left)

#        1
#      /   \
#     /     \
#    2       5
#   / \     / \
#  3   4   4   3


# attempt 1
# def helper_is_symmetric(root):
#     if root.left == None and root.right == None:
#         return True
    
#     if root.left == None and root.right:
#         return False
    
#     if root.left and root.right == None:
#         return False

#     if root.left.val != root.right.val:
#         return False
    
#     if (root.left.left == None and root.right.right == None) and (root.left.right == None and root.right.left == None):
#         return True

#     if (root.left.left == None or root.right.right == None) or (root.left.right == None or root.right.left == None):
#         return False

#     if (root.left.left.val == root.right.right.val) and (root.left.right.val == root.right.left.val):
#         return helper_is_symmetric(root.left) and helper_is_symmetric(root.right)

def is_symmetric(root):    
    return helper_is_symmetric(root.left, root.right)
    # helper_is_symmetric(root)

    #root

    #check whether there are right and left branches. False otherwise
    #check whether nodes from subtree 1 and subtree 2 are equal
    #continue until you finish the tree

root = TreeNode(1)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
root.right.left = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
print(is_symmetric(root))


"""
Example Tree #1:
       1
     /   \
    /     \
   2       2
  / \     / \
 3   4   4   3


Input: root = 1
Expected Output: True
"""


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.right = TreeNode(3)
root.right.right = TreeNode(3)
print(is_symmetric(root))

"""
Example Tree #2:

        1
      /   \
     /     \
    2       2
     \       \
      3       3
         

Input: root = 1
Expected Output: False
"""