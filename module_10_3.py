# module_10_3
# Блокировки и обработка ошибок

import random
import threading
from time import sleep


class Bank:

    def __init__(self, transactions, balance=0, lock=threading.Lock()):
        self.transactions = transactions
        self.balance = balance
        self.lock = lock

    def deposit(self):
        for transaction in range(self.transactions):
            any_transaction = random.randint(50, 500)
            self.balance = self.balance + any_transaction
            print(f'{transaction + 1}. Пополнение: {any_transaction}. Баланс: {self.balance}')
            if self.balance >= 500:
                if self.lock.locked():
                    self.lock.release()
            sleep(0.001)

    def take(self):
        for transaction in range(self.transactions):
            any_transaction = random.randint(50, 500)
            print(f'Запрос на {any_transaction}')
            if any_transaction <= self.balance:
                self.balance = self.balance - any_transaction
                print(f'{transaction + 1}. Снятие: {any_transaction}. Баланс: {self.balance}.')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            sleep(0.001)


transactions = 100
bk = Bank(transactions)

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
