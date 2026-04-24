# V1 Q1

from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def level_order(root):
    if root == None:
        return []
    
    queue = deque([]) # first in first out
    explored_nodes = []

    queue.append(root)

    while queue: # while isn't an empty list
        popped_node = queue.popleft()
        explored_nodes.append(popped_node.val)

        if popped_node.left != None:
            queue.append(popped_node.left)

        if popped_node.right != None:
            queue.append(popped_node.right)
        

    return explored_nodes


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
print(level_order(root))

"""
Example Input Tree:

      4
     / \
    2   6
   / \  
  1   3

Example Input: root = 4
Expected Output: [4, 2, 6, 1, 3]
Explanation: 
Level 1: Node 4
Level 2 (left to right): Node 2, Node 6
Level 3 (left to right): Node 1, Node 3
"""



# V1 Q2
def min_depth(root):
    if root is None:
        return 0

    queue = deque([]) # create queue
    queue.append(root) # initialize root

    while queue:
        popped = queue.popleft()
        


    """
    BFS from cheat sheet
    If the tree is empty:
    return an empty list

Create an empty queue
Create an empty list to store visited nodes

Add the root into the queue

While the queue is not empty:
    Pop the next node off the queue 
    Add the popped node to the list of visited nodes

    Add the popped node's left child to the queue
    Add the popped node's right child to the queue
    """

"""
Example Input Tree #1:

   3
  / \
 9  20
    / \  
   15  7

Example Input: root = 3
Expected Output: 2
Shortest path from root node to a leaf node is 3 -> 9. Number of nodes in path is 2.

Example Input Tree #2:

   2
    \
     3
      \
       4
        \
         5
          \
           6        

Example Input: root = 2
Expected Output: 5
Shortest path from root node to a leaf node is 2 -> 3 -> 4 -> 5 -> 6.
Number of nodes in path is 5.
"""
