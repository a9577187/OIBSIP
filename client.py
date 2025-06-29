import socket
import threading

# Server config
HOST = '127.0.0.1'
PORT = 5000

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print(message)
        except:
            client_socket.close()
            break

def send_messages(client_socket):
    while True:
        try:
            message = input()
            client_socket.send(message.encode())
        except:
            client_socket.close()
            break

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((HOST, PORT))
    except:
        return

    threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()
    send_messages(client_socket)

if __name__ == "__main__":
    main()
