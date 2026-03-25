# 3/24/26 Linked List & OOP (classes, instances, methods, and attributes)

class Node:
    def __init__(self, value): # initiallizer function to create an instance of an object
        self.value = value
        self.next = None
    
x = "hi" # instantiation in str
a = Node(2) # initialize our Node object
b = Node(3)
a.next = b # a.next points to b's Node even though b is set to None
b = None # now only a.next points to b's Node, b points to nothing
# print(a.value, b.value)

# Iterating through a Linked List
x_1 = Node(1)
x_2 = Node(2)
x_3 = Node(3)
x_4 = Node(4)
x_1.next = x_2
x_2.next = x_3
x_3.next = x_4

current = x_1 # start at root node (current is a pointer)
while current != None:
	# print(current.value)
	current = current.next




# V1
class Pokemon:
    def __init__(self, name, types, evolution = None):
        self.name = name
        self.types = types
        self.is_caught = False
        self.evolution = evolution
 
    
    def print_pokemon(self):
        print({
            "name": self.name,   
            "types": self.types, 
            "is_caught": self.is_caught 
        })
    
    # Q3
    def catch(self):
        self.is_caught = True
    
    #Q5
    def choose(self):
        if(self.is_caught):
            print(f"{self.name}  I choose you!")
        else:
            print(f"{self.name} is wild! Catch them if you can!")
    

    #Q6
    def add_type(self, new_type):
        self.types.append(new_type)

# my_pokemon = [jigglypuff, diglett, meowth, pidgeot, blastoise]
# normal_pokemon = get_by_type(my_pokemon, "Normal")
# print(normal_pokemon)
       
# V1 Q1
# Question: Add a line of code (outside of the class) to instantiate an instance of the class Pokemon and store it in a variable named my_pokemon. The Pokemon instance created should have name "Pikachu" and its types should be ["Electric"].
my_pokemon = Pokemon("Pikachu", ["Electric"])

# V1 Q2
squirtle = Pokemon("Squirtle", ["Water"])
# squirtle.print_pokemon()

# V1 Q3
squirtle.is_caught = True
# squirtle.print_pokemon()

# V1 Q4
my_pokemon = Pokemon("rattata", ["Normal"])
# my_pokemon.print_pokemon()
my_pokemon.catch()
# my_pokemon.print_pokemon()

# V1 Q5
my_pokemon = Pokemon("rattata", ["Normal"])
# my_pokemon.print_pokemon()
# my_pokemon.choose()
my_pokemon.catch()
# my_pokemon.choose()

# V1 Q6
jigglypuff = Pokemon("Jigglypuff", ["Normal"])
# jigglypuff.print_pokemon()

jigglypuff.add_type("Fairy")
# jigglypuff.print_pokemon()

# V1 Q7
# for pokemon in my_pokemon
    # for type in pokemon:
        #   if type == pokemontype
        #   list.append(pokemon.name)

def get_by_type(my_pokemon, pokemon_type):
    lst = []

    # way 1 (shorter)
    # Ex. of My Pokeong: Jigglypuff, Diglett, Pidgeot
    for pokemon in my_pokemon:
        # want to check if poekong type == pokemon_type
        # if pokemon_type == Fairy
        #. -> Jigglypuff.types -. [Noarmal and Fairy]
        if pokemon_type in pokemon.types:
            lst.append(pokemon.name)
    
    # way 2
    for pokemon in my_pokemon:
        for type in pokemon.types:
            if type == pokemon_type:
                lst.append(pokemon.name)

    return lst

# Ex
jigglypuff = Pokemon("Jigglypuff", ["Normal", "Fairy"])
diglett = Pokemon("Diglett", ["Ground"])
meowth = Pokemon("Meowth", ["Normal"])
pidgeot = Pokemon("Pidgeot", ["Normal", "Flying"])
blastoise = Pokemon("Blastoise", ["Water"])


# v1 Q8

def get_evolutionary_line(starter_pokemon):
    lst = [starter_pokemon.name]
    cuurent_pokemon = starter_pokemon.evolution

    # check if starter_pokeom.evolution != null
    # append into list

    while cuurent_pokemon is not None:
        lst.append(cuurent_pokemon.name)
        cuurent_pokemon = cuurent_pokemon.evolution
    
    return lst 


charizard = Pokemon("Charizard", ["fire", "flying"])
charmeleon = Pokemon("Charmeleon", ["fire"], charizard)
charmander = Pokemon("Charmander", ["fire"], charmeleon)

charmander_list = get_evolutionary_line(charmander)
# print(charmander_list)

charmeleon_list = get_evolutionary_line(charmeleon)
# print(charmeleon_list)

charizard_list = get_evolutionary_line(charizard)
# print(charizard_list)

# V1 Q9
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
          
node_one = Node("a")
node_two = Node("b")      

# print(node_one.value) 
# print(node_one.next) 
# print(node_two.value)
# print(node_two.next) 

# V1 Q10
node_one.next = node_two

print(node_one.value)
print(node_one.next.value)
print(node_two.value)

# V1 Q11
node_4 = Node("Toad")
node_3 = Node("Wario", node_4)
node_2 = Node("Luigi", node_3)
node_1 = Node("Mario", node_2)
#copied and great working with you all as well!
# feel free to copy the code great working with you all! see you!

# "Mario", "Luigi", "Wario", "Toad"]
# Mario -> Luigi
# Luigi -> Wario
# Wario -> Toad
# Toad -> None
# print(node_1.value, "->", node_1.next.value)
# print(node_2.value, "->", node_2.next.value)
# print(node_3.value, "->", node_3.next.value)
# print(node_4.value, "->", node_4.next)

# V1 Q12
def print_linked_list(head):
    current = head
    while current != None:
        print(current.value, "->", end=" ")
        current = current.next

print_linked_list(node_1)
          
