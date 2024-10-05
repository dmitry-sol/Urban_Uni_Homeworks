# module_10_3
# Блокировки и обработка ошибок

import random
import threading
from time import sleep


class Bank:

    def __init__(self, transactions, sleep_duration, balance: int = 0, lock=threading.Lock()):
        self.transactions = transactions
        self.sleep_duration = sleep_duration
        self.balance = balance
        self.lock = lock
        self.lock_counter = 0
        self.end_of_thread_1 = False

    def deposit(self):
        for transaction in range(self.transactions):
            any_transaction = random.randint(50, 500)
            self.balance += any_transaction
            print(f'{transaction + 1}+. Пополнение: {any_transaction}. Баланс: {self.balance}')
            if transaction == 99:
                self.end_of_thread_1 = True
            if self.balance >= 500:
                if self.lock.locked():
                    self.lock.release()
                    print(f'     = Замок открылся {self.lock_counter}-й раз')
            else:
                continue
            sleep(self.sleep_duration)

    def take(self):
        for transaction in range(self.transactions):
            any_transaction = random.randint(50, 500)
            print(f'     = Запрос на {any_transaction}')
            if any_transaction <= self.balance:
                self.balance -= any_transaction
                print(f'{transaction + 1}-. Снятие: {any_transaction}. Баланс: {self.balance}.')
            else:
                print(f'{transaction + 1}-. Запрос отклонён, недостаточно средств')
                if self.end_of_thread_1:
                    continue
                else:
                    self.lock.acquire()
                    self.lock_counter += 1
                    print(f'     = Замок закрылся {self.lock_counter}-й раз')
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

print(f'\nИтоговый баланс: {bk.balance}.')
print(f'Замок блокировки закрывался и открывался: {bk.lock_counter} раз.')
