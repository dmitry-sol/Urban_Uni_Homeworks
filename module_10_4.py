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
        self.guest_name = name
        super().__init__()

    def run(self):
        sleep(randint(3, 8))


class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = queue.Queue()

    def guest_arrival(self, *guests):
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    print(f'{guest.guest_name} сел(-a) за стол номер {table.number}')
                    break
            if not guest.is_alive():
                self.queue.put(guest)
                print(f'{guest.guest_name} в очереди')

    def discuss_guests(self):
        while Cafe.any_table_occupied(self):
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f'{table.guest.guest_name} покушал(-а) и ушел(ушла).')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                    if not self.queue.empty():
                        next_guest = self.queue.get()
                        table.guest = next_guest
                        print(f'Следующий гость {table.guest.guest_name}')
                        next_guest.start()
                        print(f'{next_guest.guest_name} Вышел(вышла) из очереди и сел(-а) за стол номер {table.number}')

    def any_table_occupied(self):
        table_occupied = False
        for table in self.tables:
            if table.guest is not None:
                table_occupied = True
                break
        return table_occupied


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
