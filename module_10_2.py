# -*- coding: utf-8 -*-
from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name_, power):
        self.name_, self.power = str(name_), int(power)
        super().__init__()
    def run(self):
        print(f'{self.name_}, на нас напали!')
        k = 100
        l = 0
        while k > 0:
            sleep(1)
            k = k - self.power
            l += 1
            if k < 0:
                k = 0
            print(f'{self.name_} сражается {l} день(дня)..., осталось {k} воинов.')
        print(f'{self.name_} одержал победу спустя {l} день(дня)!')

threads=[]

first_knight = Knight('Sir Lancelot', 10)
first_knight.start()
second_knight = Knight("Sir Galahad", 20)
second_knight.start()

threads.append(first_knight)
threads.append(second_knight)
for i in threads:
    i.join()
print(f'\nВсе битвы закончились!')
