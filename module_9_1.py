# module_9_1
# Введение в функциональное программирование

# 1st way

def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        results[func.__name__] = func(int_list)
    return results

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))



#2nd way

def apply_all_func(int_list, *functions):
    results = {key.__name__: key(int_list) for key in functions}
    return results

print()
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
