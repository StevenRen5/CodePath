# 9/24/26 Hash Table & Big O

"""
Set#, ##
UNDERSTAND:
> Input:
> Output:
> Edge cases:
MATCH:
PLAN:
REVIEW:
EVALUATE: 
"""

"""
Set1, #1
UNDERSTAND:
> Input: list of integer
> Output: integer
> Edge cases: [] -> 0, [1] -> 0 
MATCH:
- Not sliding window b/c we can skip elements
- dictionary
PLAN:
Use a counter to store max elements
Use a dictionary to count number of appearances of each integer
REVIEW:
EVALUATE: 
"""


def find_balanced_subsequence(art_pieces): #
    d_counter = {}
    max_c = 0

    for num in art_pieces:
        if num not in d_counter:
            d_counter[num] = 1
        else:
            d_counter[num] += 1

    for num in art_pieces:
        if num - 1 in d_counter:
            max_c = max(max_c, d_counter[num] + d_counter[num-1])
        elif num + 1 in d_counter:
            max_c = max(max_c, d_counter[num] + d_counter[num+1])

    return max_c

art_pieces1 = [1,3,2,2,5,2,3,7]
art_pieces2 = [1,2,3,4]
art_pieces3 = [1,1,1,1]

print(find_balanced_subsequence(art_pieces1))
print(find_balanced_subsequence(art_pieces2))
print(find_balanced_subsequence(art_pieces3))

