import socket
import threading

# List to keep track of all connected client sockets
clients = []

def handle_client(client_socket):
    """
    Handles communication with a single client.
    Listens for messages and broadcasts them to others.
    """
    while True:
        try:
            # Receive data from the client
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                # Connection closed by client
                break
            print(f"Received: {message}")
            # Send the message to all other connected clients
            broadcast(message, client_socket)
        except Exception:
            # Handle unexpected disconnections
            break
    
    # Remove client from list and close the socket
    if client_socket in clients:
        clients.remove(client_socket)
    client_socket.close()

def broadcast(message, connection):
    """
    Sends a message to all connected clients except the sender.
    """
    for client in clients:
        if client != connection:
            try:
                # Forward the message to other clients
                client.send(message.encode('utf-8'))
            except Exception:
                # If sending fails, close and remove the broken connection
                client.close()
                if client in clients:
                    clients.remove(client)

def main():
    """
    Initializes the server, binds to an address, and listens for incoming connections.
    """
    # Create a TCP/IP socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to all available interfaces on port 5555
    server.bind(('0.0.0.0', 5555))
    
    # Enable the server to accept connections
    server.listen()
    print("Server started on port 5555. Waiting for connections...")

    while True:
        # Accept a new connection
        client, addr = server.accept()
        print(f"Accepted connection from {addr[0]}:{addr[1]}")
        
        # Add the new client to our list
        clients.append(client)
        
        # Start a new thread to handle this specific client's communication
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == "__main__":
    main()