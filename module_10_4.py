# -*- coding: utf-8 -*-
import time
from time import sleep
from random import randint
import threading
import queue
from queue import Queue
from threading import Thread


class Table:
    def __init__(self, number):
        self.number, self.guest = number, None


class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:

    def __init__(self, queue, *tables):
        self.queue, self.tables = Queue(), tables

    def guest_arrival(self, *guest):
        self.guests = guests
        for i in range(len(self.tables)):
            if self.tables[i].guest is None:
                self.queue.put(self.guests[i])
                print(f'{self.guests[i]} сел(-а) за стол номер {self.tables[i]}')
        for i in range(len(self.guests)):
            if self.tables is None:
                print(f"{self.guests[i]} в очереди")
    def discuss_guests(self):
        while (not self.queue.empty()) or (self.tables.guest is None):
            for i in range(len(self.tables)):
                if self.tables.guest.is_alive() and self.queue.get(self.guests) is not None:
                    print(f'{self.tables[i](guests)} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {self.tables} свободен')
                    self.tables.guest = None
                if self.queue.empty() and self.tables.guest is None:
                    self.queue.get(self.tables.guests)
                    print(f"{self.guests}вышел(-ла) из очереди и сел(-а) за стол номер{self.tables}")
        self.guests.start()


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman','Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
