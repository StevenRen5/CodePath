# 6/9/26: Dictionaries & Sets

# Set 1, #1
def lineup(artists, set_times):
  d = {}
  for i in range(len(artists)):
    d[artists] = set_times[i]
  return d

# Set1, #2
'''
Understand:
Input: artist (string), festival_schedule(dictionary)
Output: dictionary with the day, time, stage
Edge case: artist doesn't exist -> {'message': 'Artist not found'}

Plan:
if artist is in festival_schedule
Else return {'message': 'Artist not found'}
'''

def get_artist_info(artist, festival_schedule):
  if artist in festival_schedule:
    return festival_schedule[artist]
  return {'message': 'Artist not found'}

festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}

print(get_artist_info("Blood Orange", festival_schedule)) 
print(get_artist_info("Taylor Swift", festival_schedule))

# Set1, #3
'''
Understand:
Input: two dictionaries: artist -> time of performance
Output: dictionary: similarities from both dictionaries
Edge case: {} for both inputs -> {}

Plan:
Go through a dicionary 
check if key in another dictionary and time is same
Create a new key-value pair for the returned {}
'''

def identify_conflicts(venue1_schedule, venue2_schedule):
  ret = {}
  for artist in venue1_schedule: # n iterations
    if artist in venue2_schedule and venue1_schedule[artist] == venue2_schedule[artist]: #o(1)
      ret[artist] = venue1_schedule[artist] 
  return ret

venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

# Set1, #4
'''
Understand:
Input: two dictionaries: artist -> time of performance
Output: dictionary: similarities from both dictionaries
Edge case: {} for both inputs -> {}

Plan:
Go through a dicionary 
check if key in another dictionary and time is same
Create a new key-value pair for the returned {}
'''

def identify_conflicts(venue1_schedule, venue2_schedule):
  ret = {}
  for artist in venue1_schedule: # n iterations
    if artist in venue2_schedule and venue1_schedule[artist] == venue2_schedule[artist]: #o(1)
      ret[artist] = venue1_schedule[artist] 
  return ret

venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

print(identify_conflicts(venue1_schedule, venue2_schedule))

