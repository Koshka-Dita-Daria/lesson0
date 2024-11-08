# -*- coding: utf-8 -*-
import random
import threading
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
        time.sleep(randint(3, 10))


class Cafe:

    def __init__(self, *tables):
        self.tables, self.queue = tables, Queue()

    def guest_arrival(self, *guests):
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    table.guest = guest
                    break
            else:
                print(f'{guest.name} в очереди')
                self.queue.put(guest)

    def discuss_guests(self):
        while not self.queue.empty() and any([table.guest for table in self.tables]):
            table = random.choice(tables)
            for i in guests:
                if i == table.guest:
                    guest = i
                    break

            if guest.is_alive() and guest == table.guest:
                print(f'{guest.name} покушал(-а) и ушёл(ушла)')
                print(f'Стол номер {table.number} свободен')
                table.guest = None
            elif table.guest is None:
                table.guest = self.queue.get()
                print(f'{guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}"')
                guest.start()


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
