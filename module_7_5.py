import os
import time

directory = '.'

for root, dirs, files in os.walk(directory):
    for file in files:
        if os.path.exists(file):
            filepath = os.path.join(os.getcwd(), file)
            filetime = os.path.getmtime(file)
            formatted_time = time.strftime("%d.%m.%Y%H:%M", time.localtime(filetime))
            filesize = os.path.getsize(file)
            parent_dir = os.path.dirname(file)
            print(f'Обнаружен файл: {file}, Путь: {filepath}, '
                  f'Размер: {filesize} байт, Время изменения: '
                  f'{formatted_time}, Родительская директория: {parent_dir}')