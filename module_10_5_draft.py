# Module_5
# Многопроцессорное программирование

import multiprocessing
from datetime import datetime


all_data = []

def read_info(file_name):
    with open(file_name, 'r') as file:
        for _ in file:
            line = file.readline()
            all_data.append(line)


if __name__ == '__main__':
    file_names = [f'./files/file {number}.txt' for number in range(1, 5)]

    # Линейный вызов
    start = datetime.now()
    list(map(read_info, file_names))
    stop = datetime.now()
    print(stop-start)

    # Многопроцессорный
    start = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, file_names)
    stop = datetime.now()
    print(stop - start, '\n')

    print(all_data[0:10], all_data[-10:-1])