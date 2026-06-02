
# 6/2/26


# Version 1, #1
"""
Understand:
Write a function using the provided skeleton code

Plan:
Use the print()

"""
def welcome():
	print("Welcome to The Hundred Acre Wood!")

welcome()

# Version 1, #2

# Understand:
# Write a function using the provided skeleton code and accepting 2 parameters.

# plan: write the function and use the print build-in function

def greeting(name,):
	print(f"Welcome to The Hundred Acre Wood{name}! My name is Christopher Robin.")

greeting("Michael")
greeting("Winnie the Pooh")


# Version 1, #3

def print_catchphrase(character):
    if character == "Pooh":
        print("Oh Brother")
    elif character == "Tigger":
        print("TTFN: Ta-ta for now!")
    elif character == "Euyore":
        print("Thanks for noticing me")
    elif character == "Christopher Robin":
        print("Silly Old Bear")
    else:
        print(f"Sorry! I don't know {character}'s catchphrase!")

print_catchphrase("Pooh")
print_catchphrase("Tigger")
print_catchphrase("Euyore")
print_catchphrase("Christopher Robin")


# Version 1, #4

'''
Implement a function get_item() that accepts a 0-indexed list items and a non-negative integer x and returns the element at index x in items. If x is not a valid index of items, return None.
'''

def get_item(items, x):
    if x < len(items):
        return items[x]
    return None

items = ["piglet", "pooh", "roo", "rabbit"]
x = 2
print(get_item(items, x))

items = ["piglet", "pooh", "roo", "rabbit"]
x = 5
print(get_item(items, x))



''' Create a function that takes list of integers and returns the sum of all values '''

def sum_honey(hunny_jars):
     total = 0
     for jar in hunny_jars:
          total += jar
     return total

hunny_jars = [2, 3, 4, 5]
print(sum_honey(hunny_jars))

hunny_jars = []
print(sum_honey(hunny_jars))

# Version 1, #6
"""
Understand:
input: list of integers
output: modified list

Plan:
loop through each element and multiply 2
"""

def doubled(hunny_jars):
  for i in range(len(hunny_jars)):
    hunny_jars[i] = hunny_jars[i] * 2
  return hunny_jars
    
hunny_jars = [1, 2, 3]
print(doubled(hunny_jars))

