from math import sqrt
import asyncio
from concurrent.futures import ProcessPoolExecutor
from timeit import default_timer as timer
import logging
import time

logging.basicConfig(filename='async.log', filemode='a', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s' )
# async def is_prime(x):
def is_prime(x):
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
        print('%i is a prime number.' %x)

async def main():
    task1 = loop.run_in_executor(executor, is_prime, 9637529763296797)
    task2 = loop.run_in_executor(executor, is_prime, 427920331)
    task3 = loop.run_in_executor(executor, is_prime, 157)

    await asyncio.gather(*[task1,task2,task3])


if __name__ == '__main__':
    start = timer()
    try:
        executor = ProcessPoolExecutor(max_workers=3)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())

    except Exception as e:
        print('There was a problem: ')
        print(str(e))
    finally:
        loop.close()


    finish = timer()
    time_ = finish-start
    print(f'Process time: {finish-start}')
    logging.debug('module %s executed, took %s seconds', __name__,time_)
