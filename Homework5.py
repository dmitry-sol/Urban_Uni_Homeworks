# Homework5

import math
immutable_var = (1, 12, 'Solid', 'Book', True, 358, [2, 4, 6, 8, 10], math.pi)
print('Immutable tuple:', immutable_var)

# Если попытаться изменить элемент кортежа:

# immutable_var[1] = 13
# immutable_var.append(123/3)
# immutable_var.extend('coke')
# print(immutable_var)

# Мы увидем прерывание процесса с ошибками

# Однако, если внутри кортежа есть список, мы можем изменить елементы внутри этого списка:

immutable_var[6][4] = 12
print('Immutable tuple:', immutable_var, "\n")


mutable_list = [1, 12, 'Solid', 'Book', True, 358, [2, 4, 6, 8, 10], math.pi]
print('Mutable List:', mutable_list)

# В списке можно изменять любой элемент:

mutable_list[1] = 24
mutable_list[2] = 'Soft'
mutable_list[4] = False
mutable_list[6][0] = 0
mutable_list.append(123/3)
mutable_list.extend(['coke', 'pepsi'])
mutable_list.remove(math.pi)

print('Mutable List:', mutable_list)
