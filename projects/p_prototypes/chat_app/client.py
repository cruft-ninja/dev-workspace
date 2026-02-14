import socket
import threading

# Function to handle receiving messages from the server in a separate thread
def receive_messages(client_socket):
    """
    Continuously listens for incoming messages from the server.
    """
    while True:
        try:
            # Receive up to 1024 bytes and decode using UTF-8
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                # If message is empty, the connection might be closed
                break
            print(message)
        except Exception as e:
            # Handle potential connection errors
            print(f"An error occurred: {e}")
            client_socket.close()
            break

def main():
    """
    Sets up the client socket, connects to the server, and handles user input.
    """
    # Create a TCP/IP socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the server on the local machine and specified port
    try:
        client.connect(('127.0.0.1', 5555))
    except ConnectionRefusedError:
        print("Could not connect to server. Make sure the server is running.")
        return

    # Start a background thread to receive messages from the server without blocking input
    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.daemon = True # Ensure thread closes when main program exits
    receive_thread.start()

    print("Connected to the server. Type your messages below (type 'quit' to exit):")
    
    # Main loop to send user messages to the server
    while True:
        try:
            message = input()
            if message.lower() == 'quit':
                break
            # Send the encoded message to the server
            client.send(message.encode('utf-8'))
        except EOFError:
            break

    # Clean up the connection
    client.close()

if __name__ == "__main__":
    main()