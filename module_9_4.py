# module_9_4
# Создание функций на лету


# Lambda-функция:

first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x, y: x == y, first, second))
print(result)


# Замыкание:

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file: # Файл будет создан, если не найден.
            for data_ in data_set:
                file.write(str(data_) + '\n')

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# Метод __call__:

import random

class MysticBall:
    def __init__(self, *word):
        self.word = word

    def __call__(self):
        return random.choice(self.word)


first_ball = MysticBall('Да', 'Нет', 'Наверное', 'Может быть', 'Вряд ли', 'Кто знает')
print(first_ball())
print(first_ball())
print(first_ball())
