# Homework4

my_string = input('Введите произвольную строку такста: ')
length = len(my_string)
print('Длина строки:', length, 'символ(-а/ов).')
print('Строка в ВЕРХНЕМ регистре:', my_string.upper())
print('Строка в нижнем регистре:', my_string.lower())
print('Строка без пробелов:', my_string.replace(' ', ''))
print('Первый символ строки:', my_string[0])
print('Последний символ строки:', my_string[length-1])
