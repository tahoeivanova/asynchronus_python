# корутины, или сопрограммы - генераторы, которые в процессе работы
# могут принимать извне какие-то данные

def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner


def subgen():
    x = 'Ready to accept message'
    message = yield x
    print('Subgen received: ', message)
# from inspect import getgeneratorstate
# getgeneratorstate(g) // GEN_CREATED
# g.send(None)
# getgeneratorstate(g) // GEN_SUSPENDED'

# g.throw(StopIteration)

class BlaBlaException(Exception):
    pass

@coroutine
def average():
    count = 0
    summ = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print('Done')
        except BlaBlaException:
            print('..........................')
        else:
            count += 1
            summ += x
            average = round(summ/count,2)

@coroutine
def average1():
    count = 0
    summ = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print('Done')
            break
        except BlaBlaException:
            print('..........................')
            break
        else:
            count += 1
            summ += x
            average = round(summ/count,2)

    return average

'''
>>> g = average1()
>>> g.send(5)
5.0
>>> g.send(6)
5.5
>>> g.send(1)
4.0
>>> try:
...     g.throw(StopIteration)
... except StopIteration as e:
...     print('Average', e.value)
... 
Done
Average 4.0

'''