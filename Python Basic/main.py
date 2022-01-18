print('Hello', 'World', sep='#', end=' ')
print('Hello {}'.format('world!!'))

a = 10
a = 'Ini String'
print(a)

# List, Tuple, Set, Dictionary 
lists = [1, 2, 3]

# Nambah list
lists.append(4)
lists.insert(0, 10)

# Update
list[0] = 9

# # Delete
# lists.remove(9)

# # Delete sesuai index
# list.pop(0)
print(lists)

# Tuple
tuples = (1, 2, 3)
b = 3, 4, 5
print(tuples + b)

# Sets
sets = {1, 2, 3, 3, 2, 1}
sets.add(10)
sets.add('Sepuluh')
sets.pop()
sets.discard(10)
sets.remove(10)
print(sets)

# Dictionary
dicts = {
    'name' : 'Ziggy',
    'age'  : '22'
}

print(dicts['name'])