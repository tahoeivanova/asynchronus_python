
# декоратор
def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner

# класс исключения
class BlaBlaException(Exception):
    pass

# делигирующий генератор - это генератор, который вызывает другой генератор
# подгенератор - это вызываемый генератор
# когда нам нужно разбить один генератор на несколько
# @coroutine // при yield from инициализация встроена
def subgen(): # читающий генератор (что-то читает из сокета, из файла)
    while True:
        try:
            message = yield
        # except BlaBlaException:
        #     print('Ku-ku!!!')
        except StopIteration:
            break
        else:
            print('..................', message)

    return 'Returned from subgen()'

@coroutine
def delegator(g): # транслятор
    # while True:
    #     try:
    #         data = yield
    #         # g - объект генератора, который мы передаем в делегатор
    #         g.send(data) # передает data в субгенератор
    #     except BlaBlaException as e:
    #         g.throw(e)
    # PEP 380 - yield from содержит в себе инициализацию
    # yield from g
    result = yield from g
    print(result)
