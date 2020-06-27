import socket
import selectors

# Создаем дефолтный селектор
selector = selectors.DefaultSelector()

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    # register принимает 3 аргумента: файловый об, событие, к-ое нас интересует,любые связанные данные
    selector.register(fileobj=server_socket, events=selectors.EVENT_READ, data=accept_connection)

# принятие соединений
def accept_connection(server_socket):
    client_socket, addr = server_socket.accept()
    print('Connection from ', addr)
    # регистрируем для мониторинга клиентский сокет
    selector.register(fileobj=client_socket, events=selectors.EVENT_READ, data=send_message)



# Получение от пользователя сообщений и отправка ему сообщений
def send_message(client_socket):
    request = client_socket.recv(4096)

    if request:
        response = 'Hello world!\n'.encode()
        client_socket.send(response)
    else:
        # снимаем сокет с регистрации перед закрытием
        selector.unregister(client_socket)
        client_socket.close()

def event_loop():
    while True:
        # получаем выборку объектов, к-ые готовы для чтения или записи
        events = selector.select() # (key, events)

        # SelectorKey - связывает в сокет ожидаемое событие и данные (контейнер namedTuple)
        # fileobj
        # event
        # data

        for key, _ in events:
            callback = key.data
            callback(key.fileobj) # fileobj -  сам сокет

if __name__ == '__main__':
    server()
    event_loop()
