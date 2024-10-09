# Module_5
# Многопроцессорное программирование

import multiprocessing
from datetime import datetime


def read_info(file_name):
    all_data = []
    with open(file_name, 'r') as file:
        for line in file:
            line = file.readline()
            all_data.append(line)


if __name__ == '__main__':
    file_names = [f'./files/file {number}.txt' for number in range(1, 5)]

    # Линейный вызов
    start = datetime.now()
    list_ = list(map(read_info, file_names))
    stop = datetime.now()
    print(stop-start)

    # Многопроцессорный
    start = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, file_names)
    stop = datetime.now()
    print(stop - start)
