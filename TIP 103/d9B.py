"Version 2"

"""
#1
UNDERSTAND:
> Input: adj matrix
> Output: boolean
> Edge cases:
MATCH:
PLAN:

nested for loop using i,j:
if celebrity[i][j] == 1:
   if celebrity[j][i] != 1:
    return False

return True 

REVIEW:
EVALUATE:
- size of matrix is always n x n  so when we do nested for loop, time is O(n^2) 
- O(1) space complexity
"""
def is_mutual(celebrities):

    for i in range(0, len(celebrities)):
        for j in range(1, len(celebrities)):
            if celebrities[i][j] == 1:
                if celebrities[j][i] != 1:
                    return False
    
    return True

celebrities1=[#celeb 0,1,2,3
                [0, 1, 1, 0],
                [1, 0, 1, 0],
                [1, 1, 0, 1],
                [0, 0, 1, 0]]

celebrities2 = [
              [0, 1, 1, 0],
              [1, 0, 0, 0],
              [1, 1, 0, 1],
              [0, 0, 0, 0]]

# print(is_mutual(celebrities1))
# print(is_mutual(celebrities2))

"""
#2
UNDERSTAND:
> Input: 2d list
> Output: map and adj_matrix
> Edge cases:
MATCH:
PLAN:
create client map:
- create a set for client
- iterate through elements in client and add to set
- convert set to list and use a dict to assign the client an id

create matrix: 
- know that size is n x n
- n = len(client_set)
- 


REVIEW:
EVALUATE: 
"""
def get_adj_matrix(clients):
  client_ids = {}

  # determine number of clients
  client_set = set()
  for lst_client in clients:
      for client in lst_client:
          client_set.add(client)

  client_set = list(client_set)
  for i in range(len(client_set)):
      client_ids[client_set[i]] = i

  # construct adj_matrix
  n = len(client_set) # 6
  matrix = [[0 for _ in range(n)] for _ in range(n)]

  # construct new edges using client ids - useful for matrix
  edges = []
  for client in clients:
      edges.append([client_ids[client[0]], client_ids[client[1]]])
  for edge in edges:
      matrix[edge[0]][edge[1]] = 1

  return client_ids, matrix

clients = [
  ["Yalitza Aparicio", "Julio Torres"], 
  ["Julio Torres", "Fred Armisen"], 
  ["Bowen Yang", "Julio Torres"],
  ["Bowen Yang", "Margaret Cho"],
  ["Margaret Cho", "Ali Wong"],
  ["Ali Wong", "Fred Armisen"], 
  ["Ali Wong", "Bowen Yang"]
]

id_map, adj_matrix = get_adj_matrix(clients)
print(id_map)
print(adj_matrix)

[[0, 0, 0, 0, 1, 0], 
 [1, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 1], 
 [1, 0, 1, 0, 0, 0], 
 [0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 1, 1, 0]]

# [
#   [0, 0, 0, 0, 1, 1],  # Fred Armisen
#   [0, 0, 0, 0, 0, 1],  # Yalitza Aparicio
#   [0, 0, 0, 1, 1, 0],  # Margaret Cho
#   [0, 0, 1, 0, 1, 1],  # Bowen Yang
#   [1, 0, 1, 1, 0, 0],  # Ali Wong
#   [1, 1, 0, 1, 0, 0]   # Julio Torres
# ]