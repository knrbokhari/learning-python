# list
py_list = ['apple', "banana", "cherry"]
print(py_list)

# list() Constructor
thislist = list(("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")) # note the double round-brackets
print(thislist)

# Access Items
print(thislist[1])

# Negative Indexing
print(thislist[-1])

# Range of Indexes
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])

# Range of Negative Indexes
print(thislist[-4:-1])
print(thislist[:-1])
print(thislist[-4:])

# Insert Items
thislist.insert(2, "watermelon")
print(thislist)

# Append Items
thislist.append("orange")
print(thislist)

# Extend List
list1 = ["apple", "banana", "cherry"]
list2 = ["mango", "pineapple", "papaya"]
list1.extend(list2)
print(list1)

# Remove Specified Item
thislist.remove("banana")
print(thislist)

# Remove Specified Index
thislist.pop(1)
print(thislist)

# Remove the last item:
thislist.pop()
print(thislist)

# The del keyword also removes the specified index:
del thislist[0]
print(thislist)

# Delete the entire list:
# del thislist

# Clear the List
# thislist.clear()
# print(thislist)

# Sort List Alphanumerically
thislist.sort()
print(thislist)

# Sort Descending
thislist.sort(reverse = True)
print(thislist)

# Reverse Order
thislist.reverse()
print(thislist)

# Perform a case-insensitive sort of the list:
thislist.sort(key = str.lower)
print(thislist)

# Customize Sort Function
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

# Copy a List
mylist = thislist.copy()
print(mylist)

# Join Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# List Methods
#   append()    	Adds an element at the end of the list
#   clear() 	    Removes all the elements from the list
#   copy()  	    Returns a copy of the list
#   count() 	    Returns the number of elements with the specified value
#   extend()    	Add the elements of a list (or any iterable), to the end of the current list
#   index() 	    Returns the index of the first element with the specified value
#   insert()    	Adds an element at the specified position
#   pop()   	    Removes the element at the specified position
#   remove()	    Removes the item with the specified value
#   reverse()       Reverses the order of the list
#   sort()  	    Sorts the list