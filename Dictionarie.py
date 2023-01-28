# Dictionary: Dictionaries are used to store data values in key:value pairs. A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

# When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.

# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

# Dictionaries cannot have two items with the same key:

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)

# The keys() method will return a list of all the keys in the dictionary.
x = thisdict.keys()
print(x)

# The values() method will return a list of all the values in the dictionary.
x = thisdict.values()
print(x)

# The items() method will return each item in a dictionary, as tuples in a list.
x = thisdict.items()
print(x)

# Change Values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)

# Update Dictionary
thisdict.update({"year": 2020})
print(thisdict)

# Adding Items
thisdict["color"] = "red"
print(thisdict)

# Removing Items
thisdict.pop("color")
print(thisdict)

# The popitem() method removes the last inserted item
thisdict.popitem()
print(thisdict)

# The del keyword removes the item with the specified key name:
del thisdict["model"]
print(thisdict)

# The clear() method empties the dictionary:
thisdict.clear()
print(thisdict)

# Copy a Dictionary

# Make a copy of a dictionary with the copy() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

# Make a copy of a dictionary with the dict() function:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

# Nested Dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)

# Dictionary Methods
# clear()	    Removes all the elements from the dictionary
# copy()	    Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	        Returns the value of the specified key
# items()	    Returns a list containing a tuple for each key value pair
# keys()	    Returns a list containing the dictionary's keys
# pop()	        Removes the element with the specified key
# popitem()	    Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	    Updates the dictionary with the specified key-value pairs
# values()	    Returns a list of all the values in the dictionary

























