from time import time

# генераторы - это функции
# next возвращает элемент и контроль управления над потоком в то место, откуда мы вызвали ф-цию next
# если элементы кончились - выбрасывает исключение StopIteration
# ключевая особенность - можно поставить выполнение ф-ции на паузу,
# а потом продолжить ее выполнение с того самого места, на котором она остановилась





def gen_filename():
    while True:
        pattern = 'file-{}.jpeg'
        t = int(time()*1000) # кол-во милисекунд

        yield pattern.format(str(t))

        # выполнение программы сдвигается до след. yield
        # yield рубит итерацию на две половину (next и след. next)
        sum = 243+234
        print(sum)

# g = gen_filename()


# ключевые особенности
# генераторы - функции, это не просто список,
# контроль управления
# инструкции yield м б несколько, то, что после yield - выполняется в след итерации

def gen1(s):
    for i in s:
        yield i


def gen2(n):
    for i in range(n):
        yield i

g1 = gen1('Nalalia')
g2= gen2(4)

tasks = [g1, g2]

while tasks:
    task = tasks.pop(0)

    try:
        i = next(task)
        print(i)
        tasks.append(task)
    except StopIteration:
        pass

