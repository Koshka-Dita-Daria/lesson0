# -*- coding: utf-8 -*-
import time
from time import sleep
from random import randint
import threading
import queue
from queue import Queue
from threading import Thread

class Table:
    def __init__(self, number, guest=None):
        self.number, self.guest = number, guest
class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name
    def run(self):
        sleep(randint(3, 10))
class Cafe:
    def __init__(self, queue, *tables):
        super().__init__()
        self.queue, self.tables = Queue(), tables
    def  guest_arrival(self, *guests):
        self.guests = Guest
        if self.guests is None:
            self.queue.put(guests)
            print(f'{self.guests} сел(-а) за стол номер {self.tables}')
    def discuss_guests(self):
        if self.queue.empty() or self.tables(self.guests) is not None:
            if self.queue.get() is not [] and self.guests.is_alive():
                print(f"{self.tables(self.tables.index())} покушал(-а) и ушёл(ушла)")
                print(f"Стол номер {self.tables} свободен")
