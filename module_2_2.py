# module_2_2
# 1st way

first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))

if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)


# 2nd way

list_numbers = []
for i in range(3):
    list_numbers.append(int(input(f'Введите {i+1}-е число: ')))
if list_numbers[0] == list_numbers[1] == list_numbers[2]:
    print('Совпадающих чисел: 3')
elif (list_numbers[0] == list_numbers[1]
      or list_numbers[0] == list_numbers[2]
      or list_numbers[1] == list_numbers[2]):
    print('Совпадающих чисел: 2')
else:
    print('Совпадающих чисел: 0')
