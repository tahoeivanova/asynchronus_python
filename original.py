import socket

# domain:5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5000))
server_socket.listen()

while True:
    print('Before .accept()')
    # Любая функция является блокирующей.
    # Она блокирует программу до тех пор, пока не закончится ее выполнение.

    client_socket, addr = server_socket.accept()
    # запрос nc localhost 5000
    print('Connection from ', addr)

    while True:
        # print('Before .recv()')
        request = client_socket.recv(4096)
        # если подключится второй клиент, сервер не отреагирует, так как занят первым

        if not request:
            break
        else:
            response = 'Hello world!\n'.encode()
            client_socket.send(response)

    # Чтобы принять другое подключение, нужно выйти из внутреннего цикла while
    # нужно передавать контроль выполнения программы (приостанавливать, опять запускать функции при опр. событиях)
    print('Outside inner while loop')
    client_socket.close()
