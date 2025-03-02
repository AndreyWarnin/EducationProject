import os.path
import threading
import time
from time import sleep

def write_words(word_count, file_name):
    file_mode = 'a' if os.path.exists(file_name) else 'w'
    with open(file_name, file_mode, encoding='UTF-8') as file:
        for num in range(1, word_count + 1):
            file.write(f'Какое-то слово № {num}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

time_start = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_end = time.time()
time_elapsed = time_end - time_start
print(f'Время затраченное на выполнение работы: {time_elapsed}')

time_start = time.time()
thread1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread1.join()
thread2.join()
thread3.join()
thread4.join()
time_end = time.time()
time_elapsed = time_end - time_start
print(f'Время затраченное на выполнение работы потоков: {time_elapsed}')



