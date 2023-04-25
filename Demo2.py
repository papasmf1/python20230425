# List, Dict, Tuple, Set의 각각의 특징을 간단하게 비교하는 데모 코드입니다.

# List
my_list = ['apple', 'banana', 'cherry']
print("List:")
print(my_list)
print("Length of list:", len(my_list))
print("First item in list:", my_list[0])
print("Last item in list:", my_list[-1])
my_list.append('orange')
print("List after adding an item:", my_list)

# Dict
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
print("Dictionary:")
print(my_dict)
print("Length of dictionary:", len(my_dict))
print("Value of 'name' key:", my_dict['name'])
my_dict['job'] = 'programmer'
print("Dictionary after adding a key-value pair:", my_dict)

# Tuple
my_tuple = ('apple', 'banana', 'cherry')
print("Tuple:")
print(my_tuple)
print("Length of tuple:", len(my_tuple))
print("First item in tuple:", my_tuple[0])
print("Last item in tuple:", my_tuple[-1])

# Set
my_set = {'apple', 'banana', 'cherry'}
print("Set:")
print(my_set)
print("Length of set:", len(my_set))
my_set.add('orange')
print("Set after adding an item:", my_set)
