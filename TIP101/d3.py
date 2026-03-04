# 3/3/26 Unit 2

# Demo
# Understand:
# Plan:
'''
1. takes in a list of words
2. create an empty dictionary
3. iterate through list
4. check if current word is an anagram of something else
4b. figure how to assess anagrams
5. keep track / update dictionary with new decisions
6. return a list of grouped words

return a list

'''
words = ["eat", "tea", "tan", "ate", "nat", "bat"] 
# output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

# Implement
def group_anagrams(words):
    anagram_dictionary = {} # aet -> [tea, eat, ate]; this line makes clear after line 26

    for word in words:
        sorted_word = str(sorted(word)) # eat -> aet, tea -> aet, ate -> aet
        # sorted word will be used as an anagram key
        # note: sorted() returns a list so use str() for string sorting

        if  sorted_word not in anagram_dictionary: #if item in dictionary
            anagram_dictionary[sorted_word] = [word]
        else:
            anagram_dictionary[sorted_word].append(word)
    
    return list(anagram_dictionary.values())
        
# print(group_anagrams(words))
    
# Q1

def is_monotonic(nums)):
    isMonotonic = False

    for i in range(len(nums)):

    # check decreasing and increasing (two for loops)

    return 


# Q2
def student_directory(student_names):
    student_dictionary = {}
    for i in range(len(student_names)):
        student_dictionary[student_names[i]] = i+1

    return student_dictionary

student_names = ["Ada Lovelace", "Tu Youyou", "Mae Jemison", "Rajeshwari Chatterjee", "Alan Turing"]
# print(student_directory(student_names))


# Q#

print("Q#", )


