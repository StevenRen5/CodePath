# 7/30/26 Binary Trees II

from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from d17 import print_tree, build_tree

"""
Slideshow problem
UNDERSTAND:
> Input: root of a binary tree
> Output: array of arrays, which contain elements in level order
> Edge cases: [] -> []
MATCH: BFS algorithm
PLAN:
First construct the BFS algorithm
Use a counter to track whether we traverse left or right
Create an array globally to store the result and use a local queue inside the BFS to store the level result

REVIEW: 
EVALUATE: O(n) time, O(n) space
"""

def zigzag(root):
    if root is None:
        return []
    res = []
    counter = 0
    q = deque([root])

    while q:
        local_q = deque()
        for _ in range(len(q)):
            curr = q.popleft()
            if counter % 2 == 0:
                local_q.append(curr.val)
            else:
                local_q.appendleft(curr.val)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        counter += 1
        res.append(list(local_q))
    return res

root = build_tree([3, 9, 20, None, None, 15, 7]) # Output: [[3], [20, 9], [15, 7]]
print(zigzag(root))

    
            
