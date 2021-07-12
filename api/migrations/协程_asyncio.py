import asyncio
import os
path = r'C:\Users\admin\Desktop\change'
import time
from aiofile import async_open
lock = asyncio.Lock()


async def change_file(file_path):
    print(file_path)
    try:
        async with async_open(file_path, 'r') as file:
            ma_file_content =await file.read()
        if 'requires maya "2018ff09"' in ma_file_content:
            ma_file_content = ma_file_content.replace('requires maya "2018ff09"', 'requires maya "2017ff05"')
        async with async_open(file_path, 'w') as f:
            await f.write(ma_file_content)

    except Exception as e:
        async with lock:
            with open('d:/change_not.txt', 'a') as f:
                f.write(file_path)
                print(file_path)


loop = asyncio.get_event_loop()
def asynchronous():
    tasks = []
    for root, dirs, files in os.walk(path):
            for file in files:
                    if file.endswith('.ma'):
                        file_path = os.path.join(root, file)
                        tasks.append(
                            loop.create_task(change_file(file_path))

                        )
    loop.run_until_complete(asyncio.wait(tasks))

if __name__ == '__main__':
    start = time.time()
    asynchronous()
    end  = time.time()
    print(end - start)