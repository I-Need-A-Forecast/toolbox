'''
Python's libraries allows us to convert nested dictionaries and lists into a
json ready to send accross the interenet. Unfortunately, many python server process
framworks, specifically ones that query the database (looking at you Django!)
return objects that look and act exactly like dictionaries and arrays, but don't work
in cases where hard code dictionaries and list do.
The purpose of this program is to deep copy an arbetrary dictionary in preparation of
making it a json.
'''

def prejson(dictionary_tocopy):
    return {}