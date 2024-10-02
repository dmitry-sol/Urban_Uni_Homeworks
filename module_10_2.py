# module_10_2
# Потоки на классах

from time import sleep
from threading import Thread


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = str(name)
        self.power = int(power)

    def run(self):
        print(f'{self.name}, на нас напали!')
        enemy = 100
        day_power = self.power
        days = 1
        for warrior in range(enemy):
            day_power -= 1
            enemy -= 1
            if enemy == 0:
                print(f'{self.name} одержал победу спустя {days} дней(дня)!')
            elif day_power == 0:
                print(f'{self.name} сражается {days} день(дня)..., осталось {enemy} воинов.')
                days += 1
                day_power = self.power
                sleep(1)


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
