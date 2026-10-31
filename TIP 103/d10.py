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
  stack = [start_node]
  visited_nodes = []
  cost = 0
  while stack:
    node = stack.pop()
    # if current location is MIA, stop the while loop
    if node == dest_node:
      return cost
    if node not in visited_nodes:
      visited_nodes.append(node)
      for neighbor in graph[node]:
        if neighbor[0] not in visited_nodes:
          stack.append(neighbor[0])
      cost += graph[node][-1][1] # the last neighbor (edge) of the current in graph[node] is what we append to top of stack and what we traverse through.
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

# print(calculate_cost(flights, 'LAX', 'MIA'))


"""
Set1, #2
UNDERSTAND:
> Input: flights - adjacency dictionary 
> Output: integer -min number of edges (flights)
> Edge cases:
MATCH:
find the number of components and that'll be the number of edges to add
BFS
PLAN:
retrieve the total number of flights
run BFS on an arbitrary flight and check the number of flights we reached.
Run BFS on the flight not in the previous flights we've reached until we get all.
The number of iteration is the number of edges we add.
REVIEW:
EVALUATE: 
Run time is O(V+E)
Space is O(V)
"""

from d9 import BFS 

def min_flights_to_expand(flights):
  flights_list = list(flights.keys())
  num_flights = len(flights_list)
  need_edges = 0
  reachable_flights = set()

  start_flight = flights_list[0]
  res_start_flight = BFS(flights, start_flight)
  if len(res_start_flight) == num_flights:
    return 0 

  for reachable_flight in res_start_flight:
    reachable_flights.add(reachable_flight)

  for flight in flights_list:
    if flight not in reachable_flights:
      need_edges += 1
      component_res = BFS(flights, flight)
      for flight_res in component_res:
        reachable_flights.add(flight_res)
      if len(reachable_flights) == num_flights:
        return need_edges
    
flights = {
  'JFK': ['LAX', 'SFO'],
  'LAX': ['JFK', 'SFO'],
  'SFO': ['JFK', 'LAX'],
  'ORD': ['ATL'],
  'ATL': ['ORD']
}

"""
JFK ----- LAX
  \       /
   \     /
     SFO

ORD ----- ATL
"""

print(min_flights_to_expand(flights))

"""
Set1, #3
UNDERSTAND:
> Input: flights - adj dict 
> Output: flight path from source to destination
> Edge cases:
MATCH:
dictionary
BFS
PLAN:
Run BFS and at the same time create flight_map which maps an airpoint destination to another
REVIEW:
EVALUATE: 
"""
from collections import deque
def get_itinerary(graph, start_node, destination):
  visited_nodes = [start_node]
  flight_map = {}
  queue = deque([start_node])
  flag = False
  while queue and not flag:
    current = queue.popleft()
    for neighbor in graph[current]:
      if neighbor not in visited_nodes:
        # we're backtracking so instead of current -> neighbor, we do the opposite
        flight_map[neighbor] = current
        if neighbor == destination:
          flag = True
        queue.append(neighbor)
        visited_nodes.append(neighbor)

  res = []
  current = destination
  # backtrack from target node until we reach start node
  while current != start_node:
    res.append(current)
    current = flight_map[current]
  res.append(start_node)
  res.reverse()
  return res

flights = {
    'LAX': ['SFO'],
    'SFO': ['LAX', 'ORD', 'ERW'],
    'ERW': ['SFO', 'ORD'],
    'ORD': ['ERW', 'SFO', 'MIA'],
    'MIA': ['ORD']
}

print(get_itinerary(flights, 'LAX', 'MIA'))

