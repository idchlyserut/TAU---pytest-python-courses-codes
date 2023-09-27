"""
Dictionaries

contents: key/value pairings
mutable: can be changed
order: maintain order of entry as python 3.7
syntax: curly braces contain keys and values keys and values separated by a colon

example: 

years = {"Layla": 1974, "Ackeem": 1997}
"""


#dictionary method
#get method

stuff = {"food":15, "energy":100, "enemies":3}

"""
print(stuff.get("food"))

#items method accepts all dictionary acts upon an argument
print(stuff.items())

#keys method same as items method, but only prints the keys

print(stuff.keys())

"""

#popitem method allows us to remove the last item in the dictionary
#print(stuff.popitem())
#print(stuff)
#set default method

'''
print(stuff.setdefault("food"))
print(stuff)
print(stuff.setdefault("friends", 123))
print(stuff)

'''

#update method

new_items = {"rocks":4, "arrows": 18}
stuff.update(new_items)
print(stuff)

new_items = {"rocks":2, "arrows":5}
stuff.update(new_items)
print(stuff)

stuff.update(food = 450, cookies =6)
print(stuff)