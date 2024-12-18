import random
import threading
from time import sleep

class Bank:
    lock = threading.Lock()

    def __init__(self):
        self.balance = 500

    def deposit(self):
        for i in range(100):
            income = random.randint(50, 500)
            self.balance += income
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {income}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(100):
            outcome = random.randint(50, 500)
            print(f'Запрос на {outcome}')
            if outcome <= self.balance:
                self.balance -= outcome
                print(f'Снятие: {outcome}. Баланс: {self.balance}')
            else:
                self.lock.acquire()
                print('Запрос отклонён, недостаточно средств')
            sleep(0.001)

bk = Bank()
thread1 = threading.Thread(target=Bank.deposit, args=(bk,))
thread2 = threading.Thread(target=Bank.take, args=(bk,))
thread1.start()
thread2.start()
thread1.join()
thread2.join()

print(f'Итоговый баланс: {bk.balance}')
