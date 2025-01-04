import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='UTF-8') as file:
        line = file.readline()
        while len(line) > 0:
            all_data.append(line)
            line = file.readline()

# time_start = time.time()
# for fn in ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']:
#     read_info(fn)
# time_elapsed = time.time() - time_start
# print(time_elapsed)

if __name__ == '__main__':
    time_start = time.time()
    with Pool() as p:
        p.map(read_info, [f'file {n}.txt' for n in range(1, 5)])
    time_elapsed = time.time() - time_start
    print(time_elapsed)