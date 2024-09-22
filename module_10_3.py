# -*- coding: utf-8 -*-
import random
import time
from time import sleep
from random import randint
import threading
from threading import Thread, Lock

class Bank:
    def __init__(self):
        self.balance, self.lock = randint(50, 500), Lock()
    def deposit(self):
        for i in range(100):
             k = randint(50, 500)
             if self.balance >= 500 and self.lock.locked() == True:
                self.lock.release()
             self.balance += k
             print(f'Пополнение: {k}. Баланс: {self.balance}')
             time.sleep(0.001)
    def take(self):
        for i in range(100):
            k = randint(50, 500)
            print(f'Запрос на {k}')
            if self.balance >= k:
                self.balance -= k
                print(f'Снятие: {k}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')

