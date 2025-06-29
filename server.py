import socket
import threading

# Server config
HOST = '127.0.0.1'
PORT = 5000

clients = []

# Broadcast message from server to all clients
def broadcast(message):
    for client in clients:
        try:
            client.send(message.encode())
        except:
            client.close()
            clients.remove(client)

# Handle messages from client (not broadcasting back)
def handle_client(client_socket, addr):
    print(f"[CONNECTED] {addr}")
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print(f"[{addr}] {message}")
        except:
            print(f"[DISCONNECTED] {addr}")
            if client_socket in clients:
                clients.remove(client_socket)
            client_socket.close()
            break

def send_from_server():
    while True:
        message = input()
        broadcast(f"[Server] {message}")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[STARTED] Server listening on {HOST}:{PORT}")

    threading.Thread(target=send_from_server, daemon=True).start()

    while True:
        client_socket, addr = server.accept()
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket, addr), daemon=True)
        thread.start()

if __name__ == "__main__":
    start_server()
