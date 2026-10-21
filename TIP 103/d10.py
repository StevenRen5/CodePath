# 10/15/26

"""
Set1, #1
UNDERSTAND:
> Input: flights - adjacency dictionary (weighted graph), start location, final destination
> Output: int - cost from fyling to start to final
> Edge cases:
MATCH:
DFS
PLAN:
REVIEW:
EVALUATE: 
"""

def DFS(graph, start_node, dest_node):
  stack = [start_node[0]]
  visited_nodes = []
  cost = 0
  while stack:
    current = stack.pop()[0]
    # if current location is MIA, stop the while loop
    if current == dest_node:
      return cost
    if current not in visited_nodes:
      visited_nodes.append(current)
    for neighbor in graph[current]:
      if neighbor[0] not in visited_nodes:
        stack.append(neighbor[0])
    cost += graph[current][-1][0] # the last neighbor (edge) of the current in graph[current] is what we append to top of stack and what we traverse through.
  return -1

def calculate_cost(flights, start, dest):
  return DFS(flights, start, dest)


flights = {
    'LAX': [('SFO', 50)],
    'SFO': [('LAX', 50), ('ORD', 100), ('ERW', 210)],
    'ERW': [('SFO', 210), ('ORD', 300)],
    'ORD': [('ERW', 300), ('SFO', 100), ('MIA', 400)],
    'MIA': [('ORD', 400)]
}

print(calculate_cost(flights, 'LAX', 'MIA'))