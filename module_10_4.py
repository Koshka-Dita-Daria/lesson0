# -*- coding: utf-8 -*-
import time
from time import sleep
from random import randint
from queue import Queue
from threading import Thread


class Table:
    def __init__(self, number):
        self.number, self.guest = number, None


class Guest(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:

    def __init__(self, *tables):
        self.tables, self.queue = tables, Queue()

    def guest_arrival(self, *guests):
        self.guests = guests
        if len(self.guests) > len(self.tables):
            for i in range(len(self.tables)):
                if self.tables[i].guest is None:
                    self.tables[i].guest = self.guests[i]
                    self.tables[i].guest.start()
                    print(f'{self.guests[i].name} сел(-а) за стол номер {self.tables[i].number}')
            for g in range(len(self.tables), len(self.guests)):
                self.queue.put(self.guests[g])
                print(f"{self.guests[g].name} в очереди")
        elif len(self.guests) < len(self.tables):
            for i in range(len(self.guests)):
                if self.tables[i].guest is None:
                    self.tables[i].guest = self.guests[i]
                    self.tables[i].guest.start()
                    print(f'{self.guests[i].name} сел(-а) за стол номер {self.tables[i].number}')
        else:
            for i in range(len(self.tables)):
                if self.tables[i].guest is None:
                    self.tables[i].guest = self.guests[i]
                    self.tables[i].guest.start()
                    print(f'{self.guests[i].name} сел(-а) за стол номер {self.tables[i].number}')

    def discuss_guests(self):
        while (self.queue.empty()) or (?):
            for i in range(len(self.tables)):
                if (not self.tables[i].guest is None) and (self.tables[i].guest.is_alive()):
                    print(f'{self.tables[i].guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {self.tables[i].number} свободен')
                    self.tables[i].guest = None
                elif self.queue.empty() and self.tables[i].guest is None:
                    self.tables[i].guest = self.queue.get()
                    print(f"{self.queue.get().name}вышел(-ла) из очереди и сел(-а) за стол номер{self.tables[i].number}")
                    self.tables[i].guest.start()


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman', 'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
