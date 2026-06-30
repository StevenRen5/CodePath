# 6/30/26

"""
Set1, #1
UNDERSTAND:
> Input:
> Output:
> Edge cases:
MATCH:
PLAN:

"""

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return 
        current = self.head
        # while loop brings us to the last element 
        while current.next:
            current = current.next
        current.next = new_node

linkedlist = LinkedList()
for value in [1,2,3,4,5]:
    linkedlist.add(value) 

"""
DEMO:
UNDERSTAND:
> Input: head of a singly linked list
> Output: middle node (if even, we return second middle)
> Edge cases: empty?, single item --> return that item, 2 items --> return second item
MATCH: slow and fast pointer technique 
PLAN: 
- start both slow and fast pointer at head
- move slow pointer by 1 step, fast by 2.
- when fast reaches end, slow is the middle node.
"""

def find_middle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow 

# print(find_middle(linkedlist.head).value)

class Villager:
    def __init__(self, name, species, personality, catchphrase):
        self.name = name
        self.species = species
        self.personality = personality 
        self.catchphrase = catchphrase
        self.furniture = []

    def greet_player(self, player_name):
        if player_name == "Tram":
            return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}?"
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"
    
    def set_catchphrase(self, new_catchphrase):
        if len(new_catchphrase) >= 20:
            print("Invalid catchphrase")
            return 
        for char in new_catchphrase:
            if not char.isalpha() and char != " ":
                print("Invalid catchphrase")
                return 
        self.catchphrase = new_catchphrase
        print("Catchphrase updated")

    def add_item(self, item_name):
        valid_items = [
            "acoustic guitar", 
            "ironwood kitchenette", 
            "rattan armchair", 
            "kotatsu", 
            "cacao tree"
            ]
        if item_name in valid_items:
            self.furniture.append(item_name)

    def print_inventory(self):
        if len(self.furniture) == 0:
            print("Inventory Empty")
            return 
        Inventory = {}

        for item in self.furniture:
            if item in Inventory:
                Inventory[item] += 1
            else:
                Inventory[item] = 1
        result = []
        for item, quantity in Inventory.items():
            result.append(f"{item}: {quantity}")
        
        print(", ".join(result))

            
        
# apollo = Villager("Apollo", "Eagle", "pah")
# bones = Villager("Bones", "Dog", "ruff it up")
# print(bones.greet_player("Samia"))

# alice = Villager("Alice", "Koala", "guvnor")

# alice.set_catchphrase("sweet dreams")
# print(alice.catchphrase)
# alice.set_catchphrase("#?!")
# print(alice.catchphrase)

# alice = Villager("Alice", "Koala", "guvnor")
# print(alice.furniture)

# alice.add_item("acoustic guitar")
# print(alice.furniture)

# alice.add_item("cacao tree")
# print(alice.furniture)

# alice.add_item("nintendo switch")
# print(alice.furniture)

# alice = Villager("Alice", "Koala", "guvnor")

# alice.print_inventory()

# alice.furniture = ["acoustic guitar", "ironwood kitchenette", "kotatsu", "kotatsu"]
# alice.print_inventory()

# Set 1, #7
def of_personality_type(townies, personality_type):
    res = []
    for townie in townies:
        if townie.personality == personality_type:
            res.append(townie.name)
    return res

isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

print(of_personality_type([isabelle, bob, stitches], "Lazy"))
print(of_personality_type([isabelle, bob, stitches], "Cranky"))