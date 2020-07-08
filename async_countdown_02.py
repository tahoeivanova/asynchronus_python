import time
import asyncio

# превращаем функцию в сопрограмму
# определить точку внутри данной функции, которая будет неким событием переключения задач
async def count_down(name, delay):
    indents = (ord(name) - ord('A')) * '\t'

    n = 3
    while n:
        # time.sleep(delay)
        await asyncio.sleep(delay)

        duration = time.perf_counter() - start
        print('-' * 40)
        print('%.4f \t%s%s = %i' % (duration, indents, name, n))

        n-= 1

async def main():

    task1 = asyncio.create_task(count_down('A', 1))
    task2 = asyncio.create_task(count_down('B', 0.8))
    task3 = asyncio.create_task(count_down('C', 0.5))

    await asyncio.gather(task1, task2, task3)

# в основной программе мы проинициализируем некий цикл событий и будем управлять им

if __name__ == '__main__':
    start = time.perf_counter()
    asyncio.run(main())


    print('-' * 40)
    print('Done.')

