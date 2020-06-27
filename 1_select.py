import socket
from select import select

# select - системная ф-ция, которая нужна для мониторинга изменений состояния файловых объектов и сокетов
# в Unix файлом является все (каждый запущенный процесс, часы и т.д.)
# select работает с файловыми объектами, т.е. с любыми обектами, у к-ых есть метод .fileno()
# .fileno() возвращает файловый дескриптор (целое сисло, которое ассоциируется с опр. файлом)

# список для мониторинга select
to_monitor = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5000))
server_socket.listen()

# принятие соединений
def accept_connection(server_socket):
    client_socket, addr = server_socket.accept()
    print('Connection from ', addr)

    to_monitor.append(client_socket)


# Получение от пользователя сообщений и отправка ему сообщений
def send_message(client_socket):
    request = client_socket.recv(4096)

    if request:
        response = 'Hello world!\n'.encode()
        client_socket.send(response)
    else:
        client_socket.close()

def event_loop():
    while True:
        # select  - мониторит файлы, доступные для 1) чтения 2) записи 3) ошибки
        ready_to_read, _, _ = select(to_monitor, [], []) # read, write, errors

        for sock in ready_to_read:
            if sock is server_socket:
                accept_connection(sock)
            else:
                send_message(sock)

if __name__ == '__main__':
    to_monitor.append(server_socket)
    event_loop()
