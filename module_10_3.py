# module_10_3
# Блокировки и обработка ошибок

import random
import threading
from time import sleep


class Bank:

    def __init__(self, transactions, sleep_duration, balance=0, lock=threading.Lock()):
        self.transactions = transactions
        self.sleep_duration = sleep_duration
        self.balance = balance
        self.lock = lock

    def deposit(self):
        for transaction in range(self.transactions):
            any_transaction = random.randint(50, 500)
            self.balance += any_transaction
            print(f'{transaction + 1}. Пополнение: {any_transaction}. Баланс: {self.balance}')
            if self.balance >= 500:
                if self.lock.locked():
                    self.lock.release()
            sleep(self.sleep_duration)

    def take(self):
        for transaction in range(self.transactions):
            any_transaction = random.randint(50, 500)
            print(f'Запрос на {any_transaction}')
            if any_transaction <= self.balance:
                self.balance -= any_transaction
                print(f'{transaction + 1}. Снятие: {any_transaction}. Баланс: {self.balance}.')
            else:
                print(f'{transaction + 1}. Запрос отклонён, недостаточно средств')
                try:
                    self.lock.acquire()
                finally:
                    self.lock.release()
            sleep(self.sleep_duration)


transactions = 100
sleep_duration = 0.001
bk = Bank(transactions, sleep_duration)

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
