# 10/20/26: Graphs II: topological sort & dijkstra 

""" Instructor Demo

The 100% Speedrun: Build a system that generates a valid quest completion order for an RPG.
Input: 

numQuests – total number of quests (0 to n - 1)
prerequisites – a list of pairs where [a, b] means quest b must be finished before quest a


Example:
3 quests
Dependencies: [[1,0], [2,1]]

Plan:
Represent the graph with an adjacency list
Track the in-degree for each quest using a hash table
Use a queue to:
Process quests with in-degree = 0
Update in-degree for other quests
Repeat until we (hopefully) finish

"""

from collections import defaultdict, deque

def get_quest_order(numQuests, prerequisites):
  # make adjacency list
  # adj_list = defaultdict(list)
  adj_list = {i: [] for i in range(numQuests)}
  # number of edges pointing to a node.
  in_degree = [0] * numQuests

  # [a,b] b must be completed before a
  for quest, prereq in prerequisites:
    # records which quest depends on that prereq 
    # prereq node -> quest node
    adj_list[prereq].append(quest)
    # increment in_degree of quest node by one since it depends on that prereq node
    in_degree[quest] += 1

  # process quests that have no prereqs
  queue = deque([i for i in range(numQuests) if in_degree == 0])
  order = []

  while queue:
    current = queue.popleft()
    order.append(current)

    # prune edges
    # decrement the in_degree of current's neighbor by 1 since we finished procesing this node so this node's edge connecting to its neighbors should be removed.
    for neighbor in adj_list[current]:
      in_degree[neighbor] -= 1

      if in_degree[neighbor] == 0:
        queue.append(neighbor)

  # length of ordering must be equal to numQuests. Otherwise, return [] for failing to do topologicla sort.
  return order if len(order) == numQuests else []

"""
Set1, #1

In the aftermath of the zombie apocalypse, your survival depends on crafting essential gear from limited 
resources. You are given a list of strings, gear that you can craft and a 2D list components where components[i] 
contains the materials you need to craft gear[i].

Some components are basic supplies that you already have, while others need to be crafted from other gear. 
Additionally, you are given a string array supplies containing all the components you initially have in your stash 
(infinite supply).

Return a list of all the gear you can craft. You can return the list in any order.

UNDERSTAND:
> Input: 
gear - list of strings,
components (materials needed to make gear at index components[i])
 supplies (infinite supply)
 (all lists)

 assumption: each list will be at least of length 1
 - no duplicates of components

> Output: list of strings representing gear which can be crafted
> Edge cases: if supplies is an empty list, return an empty list (nothing can be crafted)


MATCH:
hashmap where key is gear type and value is components needed
PLAN:

if all gear components in supplies, add gear in supplies

once a gear is made we can add it to the supplies

1. make graph based on list given
adj_dictionary = {components[i]: gear[i]}

if gear in components, replace/simplify to base components?
2. topological sort

REVIEW:
EVALUATE: 
"""
#                  item,   recipe,   curr ingredients
def craftable_gear(gear, components, supplies):
  adj_dict = {g: [] for g in gear} 
  in_degree = [0] * len(gear) # ho wmany components are needed to make a piece of gear
  for i in range(len(gear)):
    for component in components[i]:
      # go thru each component of each gear
      if component not in supplies:
        adj_dict[component].append(gear[i]) # can potentially make multiple so we append
        in_degree[i] += 1
    #if components for gear already exist in supplies, don't add to adj_dict (continue)
    # else
    # incrememnt degree of gear
    # add gear into components
  
  # topological sort:
  # 1. Calculate the in-degree of each node (how many edges are coming into the node).
  
  for supply in supplies:
    if supply in adj_dict. # partial matching

  # 2. Start with nodes that have an in-degree of 0. These nodes have no dependencies and can be processed first.
  queue = deque([i for i in range() if in_degree == 0])
  
  # 3. Remove the processed node from the graph
  # 4. For each of the processed node's neighbors, reduce their in-degree by 1. Since one of their dependencies has 
  #    been processed, you are effectively "removing" an incoming edge.
  # 5. Add new nodes with in-degree 0 to the queue and repeat until all nodes are processed.
  
  


gear_1 = ["weapon"]
components_1 = [["metal", "wood"]]
supplies_1 = ["metal", "wood", "rope"]

gear_2 = ["weapon", "trap"]
components_2 = [["metal", "wood"], ["weapon", "wire"]]
supplies_2 = ["metal", "wood", "wire"]

gear_3 = ["weapon", "trap", "shelter"]
components_3 = [["metal", "wood"], ["weapon", "wire"], ["trap", "wood", "metal"]]
supplies_3 = ["metal", "wood", "wire"]

print(craftable_gear(gear_1, components_1, supplies_1))
print(craftable_gear(gear_2, components_2, supplies_2))
print(craftable_gear(gear_3, components_3, supplies_3))



