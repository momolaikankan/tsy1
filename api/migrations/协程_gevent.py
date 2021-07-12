from gevent import spawn, joinall, monkey;monkey.patch_all()
import os
import time
path = r'C:\Users\admin\Desktop\change'


def change_file(file_path):
    print(file_path)
    try:
        with open(file_path, 'r') as file:
            ma_file_content = file.read()
        if 'requires maya "2018ff09"' in ma_file_content:
            ma_file_content = ma_file_content.replace('requires maya "2018ff09"', 'requires maya "2017ff05"')
        with open(file_path, 'w') as f:
            f.write(ma_file_content)

    except Exception as e:
        with open('d:/change_not.txt', 'a') as f:
            f.write(file_path)
            print(file_path)




def asynchronous():
    coroutine = []
    for root, dirs, files in os.walk(path):
            for file in files:
                    if file.endswith('.ma'):
                        file_path = os.path.join(root, file)
                        coroutine.append(
                            spawn(change_file, file_path)
                        )

    joinall(coroutine)


# def asynchronous():  # 异步
#
#     g_l = [spawn(change_file, i) for i in range(10)]
#     joinall(g_l)
#     print('DONE')


if __name__ == '__main__':
    # print('Synchronous:')
    # synchronous()
    print('Asynchronous:')
    start_time = time.time()
    asynchronous()
    end_time = time.time()
    print(end_time - start_time)
