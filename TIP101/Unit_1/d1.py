# 2/24

## Problem Set Version 1

# Q1
def hello_world():
    print("Hello world!")
print("Q1:\n") 
hello_world()


# Q2
def todays_mood():
    mood = "😎"
    print("Today's mood: " + mood)
print("Q2:\n") 
todays_mood()

# Q3
def print_menu(menu):
    print("Lunch today is: " + menu)

print("Q3:\n") 
print_menu("🥇")

# Q4
def sum(a, b):
    return a + b

answer = sum(13,27)
answer2 = sum(answer,answer)
print("Q4:", answer2)

# Q5
def product(a,b):
    return a * b

print("Q5:", product(22,7))


# Q6
def classify_age(age):
    if age >= 18:
        return "adult"
    else:
        return "child"
print(classify_age(18))

# Q7
def what_time_is_it(hour):
    if hour == 2:
        return "taco time"
    elif hour == 12:
        return "peanut butter jelly time"
    else:
        return "nap time"
print(what_time_is_it(2))

# Q8
def blackjack(score):
    if score == 21:
        print("Blackjack!")
    elif score > 21:
        print("Bust!")
    elif score >= 17 and score < 21:
        print("Nice hand!")
    else:
        print("Hit me!")
blackjack(21)

# Q9
def get_first(lst):
    if len(lst) == 0:
        pass
    return lst[0]
print("Q10: ", get_first([1]))

# Q10
def get_last(lst):
    if len (lst) == 0:
        pass
    return lst[-1]
print("Q10: ", get_last([1,2]))

# Q11
def counter(stop):
    for i in range(1, stop+1):
        print(i)


# Q12
def sum_ten():
    ans = 0
    for i in range(0,11):
        ans += i
    return ans

# Q13
def sum_positive_range(stop):
    ans = 0
    for i in range(0, stop+1):
        ans += i
    return ans

# Q14
def sum_range(start, stop):
    ans = 0
    for i in range(start, stop+1):
        ans += i
    return ans

# Q15
def print_negatives(lst):
    for i in range(len(lst)):
        if lst[i] < 0:
            print(i)