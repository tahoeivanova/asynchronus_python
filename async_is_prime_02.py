from math import sqrt
import time
import asyncio

async def is_prime(x):
    print('Processing %i...' %x)

    if x < 2:
        print('%i is not a prime number.' %x)
    elif x ==2:
        print('%i is a prime number.' %x)
    else:
        limit = int(sqrt(x)) + 1
        for i in range(3, limit, 2):
            if x%i==0:
                print('%i is not a prime number.' %x)
                return
            elif i%100000 == 1:
                await asyncio.sleep(0)
        print('%i is a prime number.' %x)

async def main():
    task1 = asyncio.create_task(is_prime(9637529763296797))
    task2 = asyncio.create_task(is_prime(427920331))
    task3 = asyncio.create_task(is_prime(157))
    await asyncio.gather(task1,task2,task3)
if __name__ == '__main__':
    start = time.perf_counter()
    try:
        asyncio.run(main())
    except Exception as e:
        print('There was a problem: ')
        print(str(e))



    finish = time.perf_counter()
    print(f'Process time: {finish-start}')
