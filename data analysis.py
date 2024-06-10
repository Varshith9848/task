
print("---- List Operations ----")
# Creating a list
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)

# Adding elements to a list
my_list.append(6)
print("List after appending 6:", my_list)

# Removing elements from a list
my_list.remove(3)
print("List after removing 3:", my_list)

# Modifying elements in a list
my_list[2] = 10
print("List after modifying index 2 to 10:", my_list)

# Dictionaries
print("\n---- Dictionary Operations ----")
# Creating a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("Original dictionary:", my_dict)

# Adding elements to a dictionary
my_dict['d'] = 4
print("Dictionary after adding {'d': 4}:", my_dict)

# Removing elements from a dictionary
del my_dict['b']
print("Dictionary after deleting key 'b':", my_dict)

# Modifying elements in a dictionary
my_dict['a'] = 10
print("Dictionary after modifying key 'a' to 10:", my_dict)

# Sets
print("\n---- Set Operations ----")
# Creating a set
my_set = {1, 2, 3, 4, 5}
print("Original set:", my_set)

# Adding elements to a set
my_set.add(6)
print("Set after adding 6:", my_set)

# Removing elements from a set
my_set.remove(3)
print("Set after removing 3:", my_set)

# Sets are unordered, and you can't directly modify an element. 
# However, you can remove an element and add a new one.
my_set.discard(4)
my_set.add(10)
print("Set after removing 4 and adding 10:", my_set)
