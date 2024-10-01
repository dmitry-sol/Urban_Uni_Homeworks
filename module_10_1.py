# module_10_1
# Создание потоков

from datetime import datetime
from time import sleep
from threading import Thread


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        time_start = datetime.now()
        for i in range(word_count):
            file.write('Какое-то слово № ' + str(i + 1) + '\n')
            sleep(0.1)
        time_stop = datetime.now()
        time_spent = time_stop - time_start
        print(f'Завершилась запись в файл: {file_name}, потраченное время: {time_spent}')


time_start = datetime.now()
test_1 = write_words(10, 'example1.txt')
test_2 = write_words(30, 'example2.txt')
test_3 = write_words(200, 'example3.txt')
test_4 = write_words(100, 'example4.txt')
time_stop = datetime.now()
time_spent = time_stop - time_start
print(f'Работа функции 4 раза одним потоком, времени потрачено: {time_spent}\n')

time_start = datetime.now()
test_5 = Thread(target=write_words, args=(10, 'example5.txt'))
test_6 = Thread(target=write_words, args=(30, 'example6.txt'))
test_7 = Thread(target=write_words, args=(200, 'example7.txt'))
test_8 = Thread(target=write_words, args=(100, 'example8.txt'))
test_5.start()
test_6.start()
test_7.start()
test_8.start()
test_5.join()
test_6.join()
test_7.join()
test_8.join()
time_stop = datetime.now()
time_spent = time_stop - time_start
print(f'Работа функции 1 раз в 4 потока, времени потрачено: {time_spent}')
