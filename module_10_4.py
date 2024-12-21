import threading
from itertools import count
from random import randint
from time import sleep
from gevent.queue import Queue


class Guest(threading.Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time_waiting = randint(3, 10)
        sleep(time_waiting)


class Table:
    number = None
    guest = None

    def __init__(self, num):
        self.number = num

class Cafe:
    tables = []
    queue = Queue()

    def __init__(self, *args):
        self.tables.extend(args)

    def guest_arrival(self, *guests):
        table_number = 0
        for guest in guests:
            if table_number < len(self.tables):
                print(f'{guest.name} сел(-а) за стол номер {self.tables[table_number].number}')
                self.tables[table_number].guest = guest
                guest.start()
                table_number += 1
            else:
                print(f'{guest.name} в очереди')
                self.queue.put(guest)

    def discuss_guests(self):
        occupied_tables = sum(1 for t in tables if t.guest is not None)
        while occupied_tables > 0:
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                    occupied_tables -= 1
                if table.guest is None and not self.queue.empty():
                    table.guest = self.queue.get()
                    table.guest.start()
                    occupied_tables += 1
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')

# 1. check empty tables
# 2. check queue
# 3. fill tables

tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']

# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()