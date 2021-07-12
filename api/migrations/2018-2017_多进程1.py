import os
import time
from multiprocessing import Process
from multiprocessing import Lock
path = r'C:\Users\admin\Desktop\change'
# path = r"C:\Users\admin\Desktop\4"
# path = r"C:\Users\admin\Desktop\change\seq01"
# path = r"C:\Users\admin\Desktop\sync"
def change_file(file_path):
    print(file_path)
    try:
        with open(file_path, 'r') as file:
            ma_file_content = file.readlines()
        for index, line in enumerate(ma_file_content):
            if line.find('requires maya "2018ff09"') != -1:
                ma_file_content[index] = line.replace('requires maya "2018ff09"', 'requires maya "2017ff05"')
                break
        with open(file_path, 'w') as f:
            f.writelines(ma_file_content)
    except Exception as e:
        lock.acquire()
        with open('d:/change_not.txt', 'a') as f:
            f.write(file_path)
            print(file_path)
        lock.release()


if __name__ == '__main__':

    process_list = []
    lock = Lock()
    start_time = time.time()
    for root, dirs, files in os.walk(path):
            for file in files:
                    if file.endswith('.ma'):
                        file_path = os.path.join(root, file)
                        p = Process(target=change_file, args=(file_path,))
                        p.start()
                        process_list.append(p)

    [p.join() for p in process_list]
    end_time = time.time()
    print(end_time-start_time)
