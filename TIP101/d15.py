# Binary Trees continued

# class mock interview problem 1
# dictionary
# key is the char and value is occurence of char in str
# go through string and check for the first counter = 1 . Return it 
def first_uniq_char(s: str) -> int:
	d = {}
	for char in s:
		if char not in d:
			d[char] = 1 # we can return the index at char here if it's the first we'v
		else:
			d[char] += 1 
	
	for i in range(len(s)):
		if d[s[i]] == 1:
			return i
	return -1


# print(f'Test 1 ("leetcode"): {first_uniq_char("leetcode")}') # Expected: 0
# print(f'Test 2 ("loveleetcode"): {first_uniq_char("loveleetcode")}') # Expected: 2
# print(f'Test 3 ("aabb"): {first_uniq_char("aabb")}') # Expected: -1

# class mock interview problem 2

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


"""
If either head is empty, return the head of the unempty head
Compare the head value of both linked list and use the smaller value as the new head of the combined linked list. Set .next to the other node in the linked list.
Continue buildng linked list adding the smaller node and the bigger node after 
"""

def merge_two_lists(list1, list2):
	h1 = list1
	h2 = list2

	if h1 == None and h2 == None:
		return None
	if h1 == None:
		return h2
	if h2 == None:
		return h1
	
	h_new = None
	if h1.val < h2.val:
		h_new = h1
	else:
		h_new = h2
	
	# ....
	
# --- Helper functions for testing only, you can ignore this until the end ---
def create_linked_list(nums):
	if not nums: return None
	head = ListNode(nums[0])
	current = head
	for val in nums[1:]:
		current.next = ListNode(val)
		current = current.next
	return head

def print_linked_list(head):
	vals = []
	current = head
	while current:
		vals.append(str(current.val))
		current = current.next
	print(" -> ".join(vals) if vals else "Empty List")

# --- Test Cases ---
l1 = create_linked_list([1, 2, 4])
l2 = create_linked_list([1, 3, 4])

# print("Test 1:")
merged1 = merge_two_lists(l1, l2)
# print_linked_list(merged1) # Expected: 1 -> 1 -> 2 -> 3 -> 4 -> 4

# V1 Q1

class TreeNode():
	def __init__(self, value, left=None, right=None):
		self.val = value
		self.left = left
		self.right = right
"""
1      1 -> OG. LEFT SUBTREE = TRUE AND RIGHT SUBTREE T AND F
     / \
    /   \
2   1    2
  / \   / \
3 1   1  1   1   
  / \  
4 N  N  T


"""
def helper(root, original_node_val):
	if root == None:
		return True
	if root.val != original_node_val:
		return False
		# True AND helper(root.right)

	return helper(root.left, original_node_val) and helper(root.right, original_node_val)

def is_univalued(root):
	if root == None:
		return True
	val = root.val
	return helper(root, val)
	
# root = TreeNode(1)
# root.left = TreeNode(1)
# root.right = TreeNode(1)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(1)
# root.right.right = TreeNode(1)

# root = TreeNode(1)
# root.left = TreeNode(1)
# root.right = TreeNode(1)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(2)
# root.right.right = TreeNode(1)
# print(is_univalued(root))

# V1 Q2
"""
Leaves in the bottom level are as far left as possible
"""

def height(root):
	if root == None:
		return 0
	return 1 + max(height(root.left), height(root.right))

# root = TreeNode(1)
# root.left = TreeNode(1)
# root.right = TreeNode(1)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(2)
# root.right.right = TreeNode(1)
# print(height(root))

# V1 !3
class TreeNode():
     def __init__(self, key, value=0, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

# from cheat sheet:
def search_bst(node, key):
    # Base case: node is None or we find the key
    if node is None or node.key == key:
        return node

    # If the key to be found is less than the current node's key, search in the left subtree
    if key < node.key:
        return search_bst(node.left, key)

    # If the key to be found is greater than the current node's key, search in the right subtree
    return search_bst(node.right, key)

"""
Helper function.
Helper function will take the key and value to identify where to place the new node.
"""


def insert(root, key, value):
	if root is None:
		return TreeNode(key, value)
	
	if root.key == key:
		root.value = value
		return root

	if root.key < key:
		# we don't return the helper function, but assign the root.left or right to the called function so that when we return the node in the base case, the tree is connected.
		root.right = insert(root.right, key, value)
	
	if root.key > key:
		root.left = insert(root.left, key, value)

	return root


root = TreeNode(4)
root.left = TreeNode(3)
root.right = TreeNode(5)
insert(root, 6, "hi")
# print(root.right.right.value)



	