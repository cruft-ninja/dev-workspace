import http.server
import socketserver

# Define the port number on which the server will listen.
# 8000 is a common alternative port for HTTP development.
PORT = 8000

# SimpleHTTPRequestHandler is a built-in handler that serves files 
# from the current directory and its subdirectories. It handles 
# standard GET and HEAD requests automatically.
Handler = http.server.SimpleHTTPRequestHandler

# socketserver.TCPServer handles the network-level details of 
# listening for and accepting TCP connections.
# Binding to an empty string ("") allows the server to accept 
# connections on any available network interface (local or public).
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving static files at http://localhost:{PORT}")
    print("Press Ctrl+C to stop the server.")
    
    # serve_forever() enters a loop that continues to process requests 
    # until the process is terminated (e.g., via KeyboardInterrupt).
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        # Graceful shutdown when the user presses Ctrl+C.
        print("\nServer stopped by user.")
