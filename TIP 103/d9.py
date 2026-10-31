# 10/13/26 Intro to Graphs & Traversals (BFS/DFS) 

# Graphs

from collections import defaultdict
from collections import deque
""" BFS implementation:
- Initialize an empty list of visited nodes
- Initialize an empty queue 
- Add the node we would like to start our traversal from to the queue 
- Add the node we would like to start our traversal from to visited
- While the queue is not empty:
    - Remove an element from the queue and store it in a variable, `current`
    - Loop through each of the current node's neighbors:
        - If the neighbor has not yet been visited:
            - Add the neighbor to the queue
            - Add the neighbor to the list of visited nodes
- Return the list of visited nodes
"""
def BFS(graph, start_node):
  visited_nodes = [start_node] 
  queue = deque([start_node])

  while queue:
    current = queue.popleft()
    for neighbor in graph[current]:
      if neighbor not in visited_nodes:
        queue.append(neighbor)
        visited_nodes.append(neighbor)
  return visited_nodes


""" DFS implementation (stack)
- Initialize an empty stack
- Initialize an empty list to store visited nodes
- Add the node we would like to start our traversal from to the stack
- while the stack is not empty:
    - Pop the topmost node off the stack and store it in a variable, `current`
    - If the node is not already in the list of visited nodes:
        - Add `current` to the list of visited nodes
    - Loop through the current node's neighbors:
        - If the neighbor has not yet been visited
            - Push the neighbor onto the stack
- Return list of visited nodes
"""
def DFS(graph, start_node):
  stack = [start_node]
  visited_nodes = []
  while stack:
    current = stack.pop()
    if current not in visited_nodes:
      visited_nodes.append(current)
    for neighbor in graph[current]:
      if neighbor not in visited_nodes:
        stack.append(neighbor)
  return visited_nodes

""" DFS implementation (recursion)
- Main function
    def dfs(graph, start_node):
        - Create empty list to store nodes that have been visited
        - Pass list of visited nodes and `start_node` into `dfs_helper`
        - Return list of visited nodes

- Helper function
    def dfs_helper(graph, start_node, visited):
        - If `start_node` is not in list of visited nodes
            - Append `start_node` to list of visited nodes
            - Loop through `start_node`'s neighbors
                - Call dfs_helper passing in list of visited nodes and the neighbor
                  as the new start node
"""

def DFS_recursion(graph, start_node):
  visited_nodes = []

  def dfs_helper(graph, start_node):
    if start_node not in visited_nodes:
      visited_nodes.append(start_node)
      for neighbor in graph[start_node]:
        dfs_helper(graph, neighbor)

  dfs_helper(graph, start_node)

  return visited_nodes

graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "E"],
    "D": ["B"],
    "E": ["B", "C"]
}

print(DFS(graph, "A"))

"""
Instructo demo:

The Goal: Edge List → Adjacency List
Input: edges = [[0, 1], [1, 2], [2, 0]] (edge list)
Output: A searchable dictionary/hash map (adjacency list)
"""
# We are building a basic social network.
# We are given a list of friendships (undirected).
# We need to find if "User A" is friends with "User B."

friendships = [
    ("Alice", "Bob"),
    ("Bob", "Charlie"),
    ("Alice", "David"),
    ("David", "Eve"),
    ("Eve", "Alice")
]

def build_graph(edges):
    """
    Converts a list of edges into a searchable Adjacency List.
    Complexity: O(E) to build, but allows O(1) neighbor lookups.
    """
    # Use defaultdict to avoid manual "if key exists" checks
    # every key is mapped to an empty list
    graph = defaultdict(list)

    # u,v are nodes in an edge (a tuple)
    for u, v in edges:
        # Add connection from u to v
        graph[u].append(v)
        
        # KEY STEP: Because friendships are mutual (Undirected),
        # we must add the connection from v back to u.
        graph[v].append(u)
        
    return graph

# 1. Build the graph by passing in list of edges
# social_graph = build_graph(friendships)

# 2. Test: Find Alice's friends instantly. O(1) lookup.
# print(f"Alice's friends: {social_graph['Alice']}")

# 3. Test: Does Bob have Alice in his list?
# can also check if Bob is in Alice's list since we're doing an undirected graph.
# print(f"Is Alice in Bob's friend list? {'Alice' in social_graph['Bob']}")

# 4. Critical Thinking Check:
# What happens if we add a new user who has NO friends yet?
# print(f"Zoe's friends: {social_graph['Zoe']}")  # Returns [] thanks to defaultdict!

"""
Set1, #1
UNDERSTAND:
> Input: flights - 0-index adjacency list 
> Output: boolean 
> Edge cases:
MATCH:
PLAN:
Iterate through each node i:
  iterate through each node's neighbor j:
    check if the node's neighbor (j) has i in j's list:
      if not return False
return True
REVIEW:
EVALUATE: 
run time: O(N + E x D)

"""

def bidirectional_flights(flights):
  for i in range(len(flights)): # node i, iterating through each node O(V)
     for neighbor in flights[i]: # node i's neighbor, iterating through each node's neighbor(edge) O(flights[i]). This for loop will run O(E) times total.
        # we know here that i -> neighbor, but how about neighbor -> i?
        if i not in flights[neighbor]:  # maximum degree D of a vertex. # we perform E iteration O(E) and this check here takes O(D) so O(E x D) here.
          return False
  return True

        #Node 0      1     2      3
flights1 = [[1, 2], [0], [0, 3], [2]]
"""
flights[0] = [1,2] node's 0 neighbors are 1,2
flights[1] = [0] node's 1 neighbors are 0
flights[2] = [0,3] node's 2 neighbors are 0,3
flights[3] = [0,3] node's 3 neighbors are 2
"""
flights2 = [[1, 2], [], [0], [2]]

# print(bidirectional_flights(flights1)) # True
# print(bidirectional_flights(flights2)) # False

"""
Set1, #2
UNDERSTAND:
> Input: terminals - 2D integer arr. terminals[i] = [u,v] means there's a path (edge) b/w u and v. Edge list representation of a graph.
> Output: integer - center of the airport
> Edge cases:
MATCH:
dictionary
PLAN:
We know that the center node will appear in every terminals[i]
We can use a dictionary where key is the node number and value is the occurences of the node number
Return the node val that matches the len of the terminals
REVIEW:
EVALUATE: 
"""

def find_center(terminals):
  d = defaultdict(int)
  for terminal in terminals:
    d[terminal[0]] += 1
    d[terminal[1]] += 1

  for key, val in d.items():
     if val == len(terminals):
      return key

terminals1 = [[1,2],[2,3],[4,2]]
terminals2 = [[1,2],[5,1],[1,3],[1,4]]

# print(find_center(terminals1))
# print(find_center(terminals2))

"""
Set1, #3
UNDERSTAND:
> Input: flights - adjacency dictionary ("adjacency list"), start (starting node)
  - key (index) - destinaton (node)
  - value (list) - neighbor of destination (node)
> Output: list - of all destinations reachable from the start in ascending order based on number of layovers required
> Edge cases:
MATCH:
BFS 
PLAN:
run a BFS algorithm. 

Note: The location should be provided in ascending order already because we BFS checks level by level.
REVIEW:
EVALUATE: 
N vertices, E edges
We visit each node once
We check each edge at most twice
O(N + E) run time
O(N) space complexity for storing visited cities, queue
"""

def get_all_destinations(flights, start):
  return BFS(flights, start)

flights = {
    "Tokyo": ["Sydney"],
    "Sydney": ["Tokyo", "Beijing"],
    "Beijing": ["Mexico City", "Helsinki"],
    "Helsinki": ["Cairo", "New York"],
    "Cairo": ["Helsinki", "Reykjavik"],
    "Reykjavik": ["Cairo", "New York"],
    "Mexico City": ["Sydney"],
    "New York": ["Helsinki", "Reykjavik"]   
}

# print(get_all_destinations(flights, "Beijing"))
# print(get_all_destinations(flights, "Helsinki"))

"""
Set1, #4
UNDERSTAND:
> Input: flights - adjacency dictionary, start - location name
> Output: list - all destinations that can be reached from start
> Edge cases:
MATCH:
DFS
PLAN:
run DFS algorithm
REVIEW:
EVALUATE: 
Run time: O(V+E)
Each vertex is processed once, and each edge is checked at most twice
Space: O(V) for ret_list and worst case recursion stack
"""
def get_all_destinations_(flights, start):
  return DFS(flights,start)

# print(get_all_destinations_(flights, "Beijing"))
# print(get_all_destinations(flights, "Helsinki"))

"""
Set1, #5
UNDERSTAND:
> Input: list of edges 
> Output: arr
> Edge cases:
MATCH:
dictionary
PLAN:
create a dictionary
go through each element and add the departure and arrival to the dictionary
add the departure and arrival airports totheir respective sets
find the start_airport which is in the departure and not arrival airport
iterate through the dictionary map using the starting airport and return res
REVIEW:
EVALUATE: 
O(E) for space, run time
"""

def find_itinerary(boarding_passes):
  flights_map = {}
  departure_airport = set()
  arrival_airport = set()

  for boarding_pass in boarding_passes:
    flights_map[boarding_pass[0]] = boarding_pass[1]
    departure_airport.add(boarding_pass[0])
    arrival_airport.add(boarding_pass[1])

  start_airport = ""
  for dep in departure_airport:
    if dep not in arrival_airport:
      start_airport = dep
      break
  res = [start_airport]
  while start_airport in flights_map:
    arrival = flights_map[start_airport]
    res.append(arrival)
    start_airport = arrival
  return res

boarding_passes_1 = [
                    ("JFK", "ATL"),
                    ("SFO", "JFK"),
                    ("ATL", "ORD"),
                    ("LAX", "SFO")]

boarding_passes_2 = [
                    ("LAX", "DXB"),
                    ("DFW", "JFK"),
                    ("LHR", "DFW"),
                    ("JFK", "LAX")]

# print(find_itinerary(boarding_passes_1))
# print(find_itinerary(boarding_passes_2))

"""
Set1, #7
UNDERSTAND:
> Input: adjacency matrix
> Output: integer - minimim flights from i to j
> Edge cases:
MATCH:
BFS - finds the minimum number of edges
PLAN:
BFS On adjacency matrix algorithm
REVIEW:
EVALUATE: 
"""
def counting_flights(matrix, i, j):
  n = len(matrix)

  visited = [False] * n
  visited_edges = {i: 0}
  queue = deque([i])
  result = [i]

  visited[i] = True
  while queue:
      node = queue.popleft()
      # Check every possible neighbor
      for neighbor in range(n):
          # Is there an edge AND is it unvisited?
          if matrix[node][neighbor] == 1 and not visited[neighbor]:
            visited[neighbor] = True
            visited_edges[neighbor] = visited_edges[node] + 1
            if neighbor == j:
              return visited_edges[neighbor]
            queue.append(neighbor)
            result.append(neighbor)
  return -1

# Example usage
flights = [
    [0, 1, 1, 0, 0], # Airport 0
    [0, 0, 1, 0, 0], # Airport 1
    [0, 0, 0, 1, 0], # Airport 2
    [0, 0, 0, 0, 1], # Airport 3
    [0, 0, 0, 0, 0]  # Airport 4
]

print(counting_flights(flights, 0, 2))  
print(counting_flights(flights, 0, 4))
print(counting_flights(flights, 4, 0))
"""
1 
Example 1 Explanation: Flight path: 0 -> 2
3
Example 2 Explanation: Flight path 0 -> 2 -> 3 -> 4
-1
Explanation: Cannot fly from Airport 4 to Airport 0
"""
   




