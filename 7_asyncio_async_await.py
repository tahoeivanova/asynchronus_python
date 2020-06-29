import asyncio

# @asyncio.coroutine # обертка, делающая из функции генератор, можно проверить: inspect.isgeneratorfunction(a) - True
async def print_nums():
    num = 1
    while True:
        print(num)
        num += 1
        # yield from asyncio.sleep(1)
        await asyncio.sleep(0.5)


async def print_time():
    count = 0
    while True:
        if count % 3 == 0:
            print(f'{count} seconds have passed')
        count += 1
        # yield from asyncio.sleep(1)
        await asyncio.sleep(1)



# @asyncio.coroutine
async def main():
    '''
    task1 = asyncio.ensure_future(print_nums())
    task2 = asyncio.ensure_future(print_time())
    '''
    task1 = asyncio.create_task(print_nums())
    task2 = asyncio.create_task(print_time())
    # yield from asyncio.gather(task1, task2)
    await asyncio.gather(task1, task2)

if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    # loop.close()
    asyncio.run(main())