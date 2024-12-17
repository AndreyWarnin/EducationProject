from threading import Thread
from time import sleep

class Knight(Thread):

    def __init__(self, name, power):
        Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name} на нас напали!')
        foes = 100
        days = 0
        while foes > 0:
            foes -= self.power
            days += 1
            sleep(1)
            print(f'{self.name} сражается {days} дней(дня)..., осталось {foes} воинов.')
        print(f'{self.name} одержал победу спустя {days} дней(дня)!')

knight1 = Knight('Sir Lancelot', 10)
knight2 = Knight('Sir Galahad', 20)
knight1.start()
knight2.start()
knight1.join()
knight2.join()
print('Все битвы закончились!')
