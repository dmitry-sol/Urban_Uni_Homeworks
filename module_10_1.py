# module_10_1
# Создание потоков

from datetime import datetime
from time import sleep
from threading import Thread


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        _start = datetime.now()
        for i in range(word_count):
            file.write('Какое-то слово № ' + str(i + 1) + '\n')
            sleep(0.1)
        _stop = datetime.now()
        print(f'Завершилась запись в файл: {file_name}, потраченное время: {_stop-_start}')


words_value = [10, 30, 200, 100]

# Один поток
file_names = [f'example{number}.txt' for number in range(1, 5)]

start = datetime.now()
list(map(write_words, words_value, file_names))
stop = datetime.now()
print(f'Работа функции 4 раза одним потоком, времени потрачено: {stop - start}\n')

# Много потоков
file_names = [f'example{number}.txt' for number in range(5, 9)]
thread_args = list(zip(words_value, file_names))

start = datetime.now()
threads = [Thread(target=write_words, args=(x, y)) for x, y in thread_args]  # потоки
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
stop = datetime.now()
print(f'Работа функции 1 раз в 4 потока, времени потрачено: {stop - start}\n')
