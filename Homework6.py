# Homework6

# Работа со словарями:
my_dict = {'Anna': 1990, 'Petr': 1994, 'Sofy': 2006, 'Ivan': 2023}
print('Dictionary:', my_dict)
print('Existing value:', my_dict['Anna'])
print('Not existing value:', my_dict.get('Fyodor'))
my_dict.update({'Ira': 2010, 'Gena': 2007})
print('Deleted value:', my_dict.pop('Sofy'))
print('Modified dictionary:', my_dict, '\n')

# Работа с множествами:
my_set = {1, 9, 4, 7, 5, 3, 8, 9, 0, 2, 6, 5, 4, 3, 1, True, 'Autum', 3.14, (22, 34, 56)}
print('Set:', my_set)
my_set.add(99)
my_set.add('Summer')
my_set.remove(1)
print('Modified set:', my_set)
