import multiprocessing
import time
import threading
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, "r", encoding="utf-8") as file:
        if file.readline() is not None:
            all_data.append(file.readline())
    k = all_data


filenames = [f'./file{number}.txt' for number in range(1, 5)]


time_start = datetime.now()

thr1 = threading.Thread(target=read_info(filenames[0]))
thr1.start()

thr2 = threading.Thread(target=read_info(filenames[1]))
thr2.start()

thr3 = threading.Thread(target=read_info(filenames[2]))
thr3.start()

thr4 = threading.Thread(target=read_info(filenames[3]))
thr4.start()

thr1.join()
thr2.join()
thr3.join()
thr4.join()

time_end = datetime.now()
time_res1 = time_end - time_start
print(time_res1)

# if __name__ == '__main__':
#     start = datetime.now()
#     with multiprocessing.Pool(processes=4) as pool:
#         pool.map(read_info, filenames)
#     finish = datetime.now()
#     print(finish - start)






