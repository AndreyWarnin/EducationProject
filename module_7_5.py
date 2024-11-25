import os
import time

# os.path.join
# os.path.getmtime
# os.path.getsize
# os.path.dirname

directory = '.'

# dir_ = os.getcwd()
# dir_ = os.path.abspath('module_7_5.py')
# print(dir_)
# print(os.path.dirname(dir_))

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