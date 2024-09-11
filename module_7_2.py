# module_7_2
# "Позиционирование в файле"

def custom_write(file_name, strings):
    keys_ = []
    values_ = []

    file = open(file_name, 'w', encoding='utf-8')
    len_ = len(strings)
    i = 0
    while i < len_:
        key_ = []
        tell_ = file.tell()
        key_.append(i + 1)
        key_.append(tell_)
        key_ = tuple(key_)
        keys_.append(key_)
        value_ = strings[i]
        values_.append(value_)
        file.write(value_ + '\n')
        i += 1
    strings_positions = dict(zip(keys_, values_))
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)

