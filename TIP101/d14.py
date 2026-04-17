# Binary Trees

class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

class ListNode:
    def __init__(self, key):
        self.val = key
        self.next = None

# Creating a root node
# root = TreeNode(13)

# Creating children nodes
# root.left = TreeNode(6)
# root.right = TreeNode(21)

# V1 Q1
root = TreeNode(10)
root.left = TreeNode(4)
root.right = TreeNode(6)

# V1 Q2

def check_tree(root):
    sum1 = root.left.val + root.right.val
    if root.val == sum1:
        return True
    else:
        return False

check1 = check_tree(root)
#print(check1)

root2 = TreeNode(5)
root2.left = TreeNode(3)
root2.right = TreeNode(1)

check2 = check_tree(root2)
#print(check2)    

# V1 Q3
def check_tree(root):
    if root == None:
        return False
    sum_ = 0
    if root.left != None:
        sum_ += root.left.val
    if root.right != None:
        sum_ += root.right.val
    return root.val == sum_

root3 = TreeNode(10)
root3.left = TreeNode(10)

root4 = TreeNode(5)
root4.left = TreeNode(3)
root4.right = TreeNode(2)

root5 = TreeNode(5)
root5.right = TreeNode(2)

root6 = None

# print(check_tree(root3), check_tree(root4), check_tree(root5), check_tree(None))

# V1 Q4

# def left_most(root):
#     if root == None:
#         return None
#     while root.left != None:
#         root = root.left
#     return root.val

# V1 Q5

def left_most(root):
    if root == None:
        return None
    
    if root.left == None:
        return root.val
    
    return left_most(root.left)

root7 = TreeNode(1)
root7.left = TreeNode(2)
root7.right = TreeNode(5)
root7.left.left = TreeNode(4)
root7.left.right = TreeNode(3)

check_left_most1 = left_most(root7)
# print(check_left_most1)

root8 = TreeNode(1)
root8.right = TreeNode(2)
root8.right.left = TreeNode(3)

root9 = None

check_left_most2 = left_most(root8)
check_left_most3 = left_most(root9)

# print(check_left_most2)
# print(check_left_most3)

# V1 Q 6

def inorder_traversal(root):
    if root == None:
        return []

    curr = root
    ans = []

    while root.left != None:
        ans.append(root.val)

    inorder_traversal(root.left)

