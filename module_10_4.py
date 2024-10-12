# module_10_4
# Очереди для обмена данными между потоками

from threading import Thread
from time import sleep
import queue
from random import randint


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 8))


class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = queue.Queue()

    def guest_arrival(self, *guests):
        global _guests
        _guests = guests
        tables_occupied = 0
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest.name
                    print(f'{guest.name} сел(-a) за стол номер {table.number}.')
                    tables_occupied += 1
                    guest.start()
                    break
                elif tables_occupied >= len(tables):
                    self.queue.put(guest)
                    print(f'{guest.name} в очереди.')
                    break

    def discuss_guests(self):
        tables_free = 0
        while tables_free <= len(tables):
            for guest in _guests:
                if guest.is_alive():
                    continue
                else:
                    for table in self.tables:
                        if table.guest != guest.name:
                            continue
                        else:
                            print(f'{guest.name} покушал(-а) и ушел(ушла)')
                            print(f'Стол номер {table.number} свободен.')
                            table.guest = None
                            try:
                                next_guest = self.queue.get(block=False)
                            except queue.Empty:
                                print(end='')
                            else:
                                table.guest = next_guest.name
                                print(f'Следующий гость {table.guest}')
                                next_guest.start()
                                print(f'{next_guest.name} Вышел из очереди и сел за стол номер {table.number}')

            for table in self.tables:
                if table.guest is None:
                    tables_free += 1
                else:
                    tables_free = 0


tables = [Table(number) for number in range(1, 6)]

guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()
