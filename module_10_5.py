import multiprocessing
import time
import threading
from datetime import datetime

time_start = datetime.now()


def read_info(name):
    all_data = []
    with open(name, "r") as file:
        if file.readline() is not None:
            all_data.append(file.readline())


filenames = [f'./file {number}.txt' for number in range(1, 5)]


thr1 = threading.Thread(target=read_info(filenames[0]))
thr2 = threading.Thread(target=read_info(filenames[1]))
thr3 = threading.Thread(target=read_info(filenames[2]))
thr4 = threading.Thread(target=read_info(filenames[3]))


thr1.start()
thr2.start()
thr3.start()
thr4.start()

thr1.join()
thr2.join()
thr3.join()
thr4.join()
time_end = datetime.now()
time_res1 = time_end - time_start
print(time_res1)
#if __name__ == '__main__':
    #start = time.perf_counter()


