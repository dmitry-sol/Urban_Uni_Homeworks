# module_9_3
# Генераторные сборки

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x) - len(y) for x, y in zip(first, second) if len(x) != len(y))
second_result = (len(first[i]) == len(second[i]) for i in range(min(len(first), len(second))))
second_result_2_way = map(lambda x,y: len(x) == len(y), first, second)

print(list(first_result))
print(list(second_result))
print(list(second_result_2_way))
