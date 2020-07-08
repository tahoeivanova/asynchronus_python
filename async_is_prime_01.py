from math import sqrt
import time

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


if __name__ == '__main__':
    start = time.perf_counter()
    try:
        is_prime(9637529763296797)
        is_prime(427920331)
        is_prime(157)
    except Exception as e:
        print('There was a problem: ')
        print(str(e))



    finish = time.perf_counter()
    print(f'Process time: {finish-start}')
