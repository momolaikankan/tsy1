import os
import shutil
import time
from multiprocessing import Lock
from concurrent.futures import ProcessPoolExecutor
path = r'C:\Users\admin\Desktop\change'
# path = r"C:\Users\admin\Desktop\4"
# path = r"C:\Users\admin\Desktop\change\seq01"
# path = r"C:\Users\admin\Desktop\sync"


# def change_file(file_path):
#     try:
#         with open(file_path, 'r', buffering=40960) as file:
#             ma_file_content = file.read()
#             ma_file_content = ma_file_content.splitlines()
#
#         for index, line in enumerate(ma_file_content):
#             if line.find('requires maya "2018ff09"') != -1:
#                 ma_file_content[index] = line.replace('requires maya "2018ff09"', 'requires maya "2017ff05"')
#                 break
#         with open(file_path, 'w', buffering=40960) as f:
#             f.write(''.join(ma_file_content))
#     except Exception as e:
#         lock.acquire()
#         with open('d:/change_not.txt', 'a') as f:
#             f.write(file_path)
#             print(file_path)
#         lock.release()
def change_file(file_path):
    try:
        with open(file_path, 'r') as file:
            ma_file_content = file.read()
        if 'requires maya "2018ff09"' in ma_file_content:
            ma_file_content = ma_file_content.replace('requires maya "2018ff09"', 'requires maya "2017ff05"')
        with open(file_path, 'w') as f:
            f.write(ma_file_content)

    except Exception as e:
        lock.acquire()
        with open('d:/change_not.txt', 'a') as f:
            f.write(file_path)
            print(file_path)
        lock.release()

if __name__ == '__main__':
    start_time = time.time()
    executor= ProcessPoolExecutor(max_workers=6)
    futures = []
    lock = Lock()

    for root, dirs, files in os.walk(path):

            threads = []
            for file in files:
                    if file.endswith('.ma'):
                        file_path = os.path.join(root, file)
                        future = executor.submit(change_file, file_path)
                        futures.append(future)
    executor.shutdown(True)


    end_time = time.time()
    print(end_time-start_time)