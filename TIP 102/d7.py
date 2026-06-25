# 6/23/26 OOP & Linked List

# Class 

# Parent Class (Base Class)
class Student:
    # constructor (special method)
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major
    # method
    def introduce(self):
        return f"Hi, I am {self.name}, {self.age} year old {self.major} computer science major."
# instance (object) of this class Student
s1 = Student("Alice", 20, "CS")
# print(s1.introduce())

# Child Class (Derived Class) inherits from Student
class TeachingFellow(Student):
    def __init__(self, name, age, major, cohort):
        # 1. Pass parent arguments to the parent constructor
        # note: super() lets a subclass call methods or constructors defined in its parent class. Primarily used when a child class overrides a parent method, but still need to execute the parent's origin logic.
        super().__init__(name,age,major)
        # 2. Initialize new-child specific attributes
        self.cohort = cohort
    
    def introduce(self):
        return f"{super().introduce()}. I am also TF-ing {self.cohort}."

techfellow = TeachingFellow("Michael", 22, "Physics", "Summer 2026")
# print(techfellow.introduce())

# Linked List

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

a = Node(2)
# print(x.value)

# iterating through a node
current = a
while current:
	print (current.value)
	current = current.next

"""
Set1, #1
UNDERSTAND:
> Input: list of dictionaries
> Output: list of NFT names
> Edge cases: [] -> []
MATCH: for loop 
PLAN:
Go through each item in list:
    append the name key's value to list
return list

"""
def extract_nft_names(nft_collection):
    lst = []
    for nft in nft_collection:
        lst.append(nft["name"])
    return lst

"""
Set1, #3
UNDERSTAND:
> Input:
> Output:
> Edge cases:
MATCH:
PLAN:

"""
def identify_popular_creators(nft_collection):
    d = {}
    for nft in nft_collection:
        if nft["creator"] not in d:
            d[nft["creator"]] = 1
        else:
            d[nft["creator"]] += 1
    
    ret = []
    for creator in d:
        if d[creator] >= 2:
            ret.append(creator)
    return ret

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7},
    {"name": "Future Galaxy", "creator": "SpaceArt", "value": 8.3}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

# print(identify_popular_creators(nft_collection))
# print(identify_popular_creators(nft_collection_2))
# print(identify_popular_creators(nft_collection_3))

"""
Set1, #5
UNDERSTAND:
> Input: a list of nft_collections, each element is a list 
> Output: a list of names 
> Edge cases: [] -> []
MATCH:
iterating nft_collections
PLAN:
create empty list
go through each nft_collection
    go through each nft 
        check if tag is in nft["tags"]
return list
"""

def search_nft_by_tag(nft_collections, tag):
    ret = []
    for nft_collection in nft_collections:
        for nft in nft_collection:
            if tag in nft["tags"]:
                ret.append(nft["name"])
    return ret

nft_collections = [
    [
        {"name": "Abstract Horizon", "tags": ["abstract", "modern"]},
        {"name": "Pixel Dreams", "tags": ["pixel", "retro"]}
    ],
    [
        {"name": "Urban Jungle", "tags": ["urban", "landscape"]},
        {"name": "City Lights", "tags": ["modern", "landscape"]}
    ]
]

nft_collections_2 = [
    [
        {"name": "Golden Hour", "tags": ["sunset", "landscape"]},
        {"name": "Sunset Serenade", "tags": ["sunset", "serene"]}
    ],
    [
        {"name": "Pixel Odyssey", "tags": ["pixel", "adventure"]}
    ]
]

nft_collections_3 = [
    [
        {"name": "The Last Piece", "tags": ["finale", "abstract"]}
    ],
    [
        {"name": "Ocean Waves", "tags": ["seascape", "calm"]},
        {"name": "Mountain Peak", "tags": ["landscape", "adventure"]}
    ]
]
# print(search_nft_by_tag(nft_collections, "landscape"))
# print(search_nft_by_tag(nft_collections_2, "sunset"))
# print(search_nft_by_tag(nft_collections_3, "modern"))

from collections import deque

def process_nft_queue(nft_queue):
    lst = []
    nft_queue = deque(nft_queue)
    while nft_queue:
        lst.append(nft_queue.popleft()["name"])
    return lst
    
nft_queue = [
    {"name": "Abstract Horizon", "processing_time": 2},
    {"name": "Pixel Dreams", "processing_time": 3},
    {"name": "Urban Jungle", "processing_time": 1}
]
# print(process_nft_queue(nft_queue))

nft_queue_2 = [
    {"name": "Golden Hour", "processing_time": 4},
    {"name": "Sunset Serenade", "processing_time": 2},
    {"name": "Ocean Waves", "processing_time": 3}
]
# print(process_nft_queue(nft_queue_2))

nft_queue_3 = [
    {"name": "Crypto Kitty", "processing_time": 5},
    {"name": "Galactic Voyage", "processing_time": 6}
]
# print(process_nft_queue(nft_queue_3))


"""
Set1, #8
UNDERSTAND:
> Input: list of sorted integers
> Output: tuple of min and high number 
> Edge cases: [] -> 
MATCH: iterate
PLAN:


"""
def find_closest_nft_values(nft_values, budget):
    for i in range(len(nft_values)):
        if nft_values[i] < budget:
            if nft_values[]
            

