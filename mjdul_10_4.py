from queue import Queue
from random import randint
from threading import Thread
from time import sleep


class Table:
    def __init__(self,number,guest=None):
        self.number=number
        self.guest=guest

class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        a=randint(3, 10)
        sleep(a)
class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = list(tables)

    def guest_arrival(self, *guests):
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start ()
                    print (f"{guest.name} сел(-а) за стол номер {table.number}")
                    break


            else:

                self.queue.put (guest)

                print (f"{guest.name} в очереди")

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest  is not None and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)\n Стол номер {table.number} свободен')
                    table.guest = None
                    if not self.queue.empty() and table.guest is None:
                        guest = self.queue.get()
                        table.guest = guest
                        guest.start ()
                        print(f'{guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')


tables = [Table(number) for number in range(1, 6)]
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()