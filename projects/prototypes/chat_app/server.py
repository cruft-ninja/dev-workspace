import socket
import threading

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(message)
            broadcast(message, client_socket)
        except:
            break
    client_socket.close()

def broadcast(message, connection):
    for client in clients:
        if client != connection:
            try:
                client.send(message.encode('utf-8'))
            except:
                client.close()
                if client in clients:
                    clients.remove(client)

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5555))
    server.listen()

    print("Server started on port 5555")

    while True:
        client, addr = server.accept()
        print(f"Accepted connection from {addr[0]}:{addr[1]}")
        clients.append(client)
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

clients = []

if __name__ == "__main__":
    main()
