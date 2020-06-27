import socket
from select import select

# нужно определить, какие сокеты уже готовы для чтения и записи и вызвать у них соответсв. методы
# accept, receive, send

# нужен механизм, который мог бы переключать управление между функциями server и client

# David Beazley
# 2015 Pycon
# Concurrency from the Ground up Live
# Конкурентность в Питоне с нуля вживую

# очередь - список, к-ый наполняется генераторами
tasks = []

to_read = {}
to_write = {}

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    while True:
        yield ('read', server_socket)
        client_socket, addr = server_socket.accept() # read
        print('Connection from ', addr)
        tasks.append(client(client_socket))

def client(client_socket):
    # отфильтровать два состояния клиент.сокета - read/write, чтобы передать в ф-цию select
    while True:

        yield ('read', client_socket)
        request = client_socket.recv(4096) # read

        if not request:
            break
        else:
            response = 'Hello world!\n'.encode()

            yield ('write', client_socket)
            client_socket.send(response) # write

    client_socket.close()


# событийный цикл
def event_loop():
    while any([tasks, to_read, to_write]):

        while not tasks:
            ready_to_read, ready_to_write, _ = select(to_read, to_write, [])

            for sock in ready_to_read:
                tasks.append(to_read.pop(sock))

            for sock in ready_to_write:
                tasks.append(to_write.pop(sock))

        try:
            task = tasks.pop(0)
            reason, sock = next(task)

            if reason == 'read':
                to_read[sock] = task
            if reason == 'write':
                to_write[sock] = task

        except StopIteration:
            print('Done!')

tasks.append(server())
event_loop()
