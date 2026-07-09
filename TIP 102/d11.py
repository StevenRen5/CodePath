# 7/7/26: Recursion & Linked Lists III

"""
Set1, #5
UNDERSTAND:
> Input: head of linked list
> Output: integer - length of linked list
> Edge cases: head = None -> 0
MATCH: fast-slow method
PLAN:
Use the fast-slow implementation
Create a var for cycle length

"""
class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()

def loop_length(playlist_head):
    counter = 0
    if not playlist_head:
      return counter
    
    fast = playlist_head
    slow = playlist_head
    
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next

      if fast == None:
          return counter
      if fast == slow:
          temp_ptr = slow.next
          while temp_ptr != fast:
            counter += 1
            temp_ptr = temp_ptr.next
          return counter + 1 # account for the loop that brings the temp_ptr back to the fast
              
song1 = SongNode("Wein", "AL SHAMI")
song2 = SongNode("Si Ai", "Tayna")
song3 = SongNode("Qalbi", "Yasser Abd Alwahab")
song4 = SongNode("La", "DYSTINCT")
song1.next = song2
song2.next = song3
song3.next = song4
song4.next = song2

print(loop_length(song1))
           
"""
Set1, #2
UNDERSTAND:
> Input: head of singly linked list
> Output: integer
> Edge cases: head = none -> 0
MATCH: iterate throuhg node 
PLAN:
Iterate through node saving the prev node and compare
"""
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def count_critical_points(song_audio):
  if not song_audio:
      return 0
  count = 0
  head = song_audio
  current = head
  prev = None
  while current:
    # handling first node
    if not prev:
      current = current.next
      if current:
        prev = song_audio
        continue
      else:
        return 0
    elif current.next and prev.value < current.value and current.value > current.next.value:
       count += 1
    elif current.next and prev.value > current.value and current.value < current.next.value:
       count += 1
    prev = current
    current = current.next
  return count

song_audio = Node(5, Node(3, Node(1, Node(2, Node(5, Node(1, Node(2)))))))
print(count_critical_points(song_audio))
       
        
      
     
     
    






