# 6/25/26: Linked list

"""
Set1, #1
UNDERSTAND:
> Input: list of integers
> Output: boolean value 
> Edge cases: [] -> false
MATCH: 2ptrs
PLAN: 
Go through time in task_times
  Go through time in task_times 
    if i != j:
      adds to available_time
"""
def find_task_pair(task_times, available_time):
  for i in range(len(task_times)):
    for j in range(len(task_times)):
      if i != j and task_times[i] + task_times[j] == available_time:
        return True
    
  return False

task_times = [30, 45, 60, 90, 120]
available_time = 105
# print(find_task_pair(task_times, available_time))

task_times_2 = [15, 25, 35, 45, 55]
available_time = 100
# print(find_task_pair(task_times_2, available_time))

task_times_3 = [20, 30, 50, 70]
available_time = 60
# print(find_task_pair(task_times_3, available_time))

def time_helper(time):
  """ alternative:
  Extra division gets the hours, modulo gets the last two digits (minutes)
  hours = time_int // 100
  minutes = time_int % 100
  
  return (hours * 60) + minutes
  """
  mins = 0
  if len(time) == 3:
    mins_temp = (int(time[0]) * 60) + int(time[1:3])
    mins += mins_temp
  elif len(time) == 4:
    mins_temp = (int(time[0:2]) * 60) + int(time[2:4])
    mins += mins_temp
  return mins

def find_smallest_gap(work_sessions):
  min = float('inf')
  for i in range(len(work_sessions)-1):
    diff = time_helper(str(work_sessions[i+1][0])) - time_helper(str(work_sessions[i][1]))
    if diff < min:
      min = diff
  return min

work_sessions = [(900, 1100), (1300, 1500), (1600, 1800)]
print(find_smallest_gap(work_sessions))

work_sessions_2 = [(1000, 1130), (1200, 1300), (1400, 1500)]
print(find_smallest_gap(work_sessions_2))

work_sessions_3 = [(900, 1100), (1115, 1300), (1315, 1500)]
print(find_smallest_gap(work_sessions_3))

# Set 1, #3
def calculate_expenses(expenses):
  totals = {}
  for expense in expenses:
    if expense[0] not in totals:
      totals[expense[0]] = expense[1]
    else:
      totals[expense[0]] += expense[1]
  max_price = 0
  max_exp = ''
  for exp, price in totals.items():
    if price > max_price:
      max_price = price
      max_exp = exp
  return (totals, max_exp)

expenses = [("Food", 12.5), ("Transport", 15.0), ("Accommodation", 50.0),
            ("Food", 7.5), ("Transport", 10.0), ("Food", 10.0)]
# print(calculate_expenses(expenses))

expenses_2 = [("Entertainment", 20.0), ("Food", 15.0), ("Transport", 10.0),
              ("Entertainment", 5.0), ("Food", 25.0), ("Accommodation", 40.0)]
# print(calculate_expenses(expenses_2))

expenses_3 = [("Utilities", 100.0), ("Food", 50.0), ("Transport", 75.0),
              ("Utilities", 50.0), ("Food", 25.0)]
# print(calculate_expenses(expenses_3))

"""
Set1, #5
UNDERSTAND:
> Input: string of html tags
> Output: boolean value
> Edge cases: "" -> true
MATCH:
stack
PLAN:
create a stack
Split the str at ">"
Go through the lst of html tags:
  Append tag if it doesn't have "/"
  Pop otherwise 
return len(stack) == 0
"""

def validate_html_tags(html):
  stack = []
  htmlTags = html.split(">")
  htmlTags.remove('')
  d = {"</div": "<div", "</a": "<a", "</p": "<p"}
  for tag in htmlTags:
    if "/" not in tag:
      stack.append(tag)
    elif stack and stack[-1] != d[tag]:
      return False
    else:
      stack.pop()
  return len(stack) == 0

html = "<div><p></p></div>"
# print(validate_html_tags(html))

# html_2 = "<div><p></div></p>"
# print(validate_html_tags(html_2))

# html_3 = "<div><p><a></a></p></div>"
# print(validate_html_tags(html_3))

# html_4 = "<div><p></a></p></div>"
# print(validate_html_tags(html_4))
