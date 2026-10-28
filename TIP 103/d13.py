# 10/27/26: Graphs III: Union Find

""""
class UnionFind:
  def __init__(self, n):
    self.parent = list(range(n)) # each node points to itself initally
    self.rank = [0] * n # track heights of different tree. Initially every node starts alone, every tree has height 0.

  # find root of the group containing x 
  # A node is a root when its index matches the value stored there
  def find(self,x):
    # if we are not at the root
    if self.parent[x] != x:
      self.parent[x] = self.find(self.parent[x]) # path compression. speeds up future searches. 3->2->1 becomes 3->1 and 2->1
    # if node points to itself, it's the root
    return self.parent[x] # or return x

  # combine two groups
  def union(self, a, b):
    ra, rb = self.find(a), self.find(b)
    # if the two groups are already in the same, group we're done
    if ra == rb:
      return False
    # check the rank. 
    # Two cases:
    # 1. Different ranks: Attach the lower-rank root under the higher-rank root. 
    # 2. Equal ranks: attach either root under the other, then increase the surviving root's rank by 1.
    if self.rank[ra] < self.rank[rb]:
      self.parent[ra] = rb
    if self.rank[ra] > self.rank[rb]:
      self.parent[rb] = ra
    else:
      # we attach root ra under root rb but we can do vice versa and update rank accordingly
      self.parent[ra] = rb
      self.rank[rb] += 1
    return True
"""

# Union Find
class UnionFind:
  def __init__(self, n):
    self.parent = list(range(n)) # each node points to itself initally
    self.rank = [0] * n # track heights of different tree. Initially every node starts alone, every tree has height 0.

  # find root of the group containing x 
  # A node is a root when its index matches the value stored there
  def find(self,x):
    # if we are not at the root
    if self.parent[x] != x:
      self.parent[x] = self.find(self.parent[x]) # path compression. speeds up future searches. 3->2->1 becomes 3->1 and 2->1
    # if node points to itself, it's the root
    return self.parent[x] # or return x

  # combine two groups
  def union(self, a, b):
    ra, rb = self.find(a), self.find(b)
    # if the two groups are already in the same, group we're done
    if ra == rb:
      return False
    # check the rank. 
    # Two cases:
    # 1. Different ranks: Attach the lower-rank root under the higher-rank root. 
    # 2. Equal ranks: attach either root under the other, then increase the surviving root's rank by 1.
    if self.rank[ra] < self.rank[rb]:
      self.parent[ra] = rb
    if self.rank[ra] > self.rank[rb]:
      self.parent[rb] = ra
    else:
      # we attach root ra under root rb but we can do vice versa and update rank accordingly
      self.parent[ra] = rb
      self.rank[rb] += 1
    return True

"""
Set1, #1

A city network is described by an n x n matrix is_connected, where is_connected[i][j] == 1 means 
city i and city j are directly connected. A province is a group of cities that are directly or 
indirectly connected. Return the total number of provinces.

UNDERSTAND:
> Input: graph represented by a matrix
> Output: integer - representing total number of provinces
> Edge cases: len(is_connected) is 0, return 0
MATCH:
Union Find() to get the total number of roots which will represent a distinct province
PLAN:
- start with len(is_connected) provinces
- create a DSU for len(is_connected) provinces: DSU(len(is_connected))


REVIEW:
EVALUATE: 
"""
def find_circle_num(is_connected):
  dsu = UnionFind(len(is_connected)) # 3 cities
  # dsu.parent = [0,1,2]
  # how to initalize the parent list based on graph
  for i in range(len(is_connected)):
    # i is the city we're looking at
    for j in range(i+1, len(is_connected[i])):
      # j is the city we're seeing if i is connected to it
      if is_connected[i][j] == 1:
        # index of parent is the node, parent[i] is the parent
        # dsu.parent[i] = j
        # union
        dsu.union(i, j)

  #
  
  # union
  # dsu.union(dsu.parent[0], dsu.parent[1])
  # city 0, city 1
  # city 1, city 0

  # len of array
  # decrement array when a province is made / combined

# [1, 1, 2]
# parent index 0, is 1 and parent of 1 is 1 parent of 2 is 2

find_circle_num([[1, 1, 0], [1, 1, 0], [0, 0, 1]]) # 2
# find_circle_num([[1, 1, 0],   # itself & prov1
#                  [1, 1, 0],   # itself & prov0
#                  [0, 0, 1]])  # itself
# 3 cities (nodes). [city0->city1, city1->city0] province, [city2->city2] province

# find_circle_num([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) # 3
# none of the cities connect, each city is its own province


