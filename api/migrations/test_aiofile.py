import asyncio
from aiofile import async_open


async def main():
    async with async_open("hello.txt", 'w+') as afp:
        await afp.write("Hello ")
        await afp.write("world")
        afp.seek(0)
        content =await afp.read()
        print(content)


        await afp.write("Hello from\nasync world")
        print(await afp.readline())
        print(await afp.readline())

loop = asyncio.get_event_loop()
loop.run_until_complete(main())