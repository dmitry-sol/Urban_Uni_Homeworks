# module_10_3
# Блокировки и обработка ошибок

import random
import threading
from time import sleep


class Bank:

    def __init__(self, balance=0, lock = threading.Lock()):
        self.balance = balance
        self.lock = lock

    def deposit(self):
        transactions = 100
        for transaction in range(transactions):
            one_deposit = random.randint(50, 500)
            self.balance = self.balance + one_deposit
            print(f'{transaction + 1}. Пополнение: {one_deposit}. Баланс: {self.balance}')
            if self.balance >= 500:
                if self.lock.locked():
                    self.lock.release()
            sleep(0.001)

    def take(self):
        transactions = 100
        for transaction in range(transactions):
            one_withdrawal = random.randint(50, 500)
            print(f'Запрос на {one_withdrawal}')
            if 0 < self.balance - one_withdrawal < self.balance:
                self.balance = self.balance - one_withdrawal
                print(f'{transaction + 1}. Снятие: {one_withdrawal}. Баланс: {self.balance}.')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            sleep(0.001)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')