import os
import time
import shutil
path = r'C:\Users\admin\Desktop\change'
# path = r"C:\Users\admin\Desktop\4"
# path = r"C:\Users\admin\Desktop\change\seq01"
# path = r"C:\Users\admin\Desktop\sync"
start = time.time()
import cProfile

def job():

    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.ma'):
                try:
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r') as file:
                            ma_file_content = file.readlines()
                            # print(ma_file_content)
                            # res = input('***')
                    for index, line in enumerate(ma_file_content):
                            if line.find('requires maya "2018ff09"') != -1:
                                    ma_file_content[index] = line.replace('requires maya "2018ff09"', 'requires maya "2017ff05"')
                                    break
                    with open(file_path, 'w') as f:
                            f.writelines(ma_file_content)
                except Exception as e:
                    with open('d:/change_not.txt', 'a') as f:
                        f.write(file_path)
                        print(file_path)

# end = time.time()
# print(end - start)




if __name__ == '__main__':
    job()
    # pr = cProfile.Profile()
    # pr.runcall(job)
    # # pr.sort_stats('cumtime')
    # pr.print_stats(sort='cumtime')