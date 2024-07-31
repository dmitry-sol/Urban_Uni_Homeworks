# module_3_3

# 1
def print_params(a=1, b='строка', c=True):
    print(a, b, c)
    return


print_params()
print_params(100)
print_params('one', 'two')
print_params('Black', 4, False)
print_params(b=25)
print_params(c=[1, 2, 3])

# 2
values_list = ['White', True, 550]
values_dict = {'a': False, 'b': 'Yellow', 'c': 1200}

print()
print_params(*values_list)
print_params(**values_dict)

# 3
print()
values_list_2 = ['String', 3.14]
print_params(*values_list_2, 42)
