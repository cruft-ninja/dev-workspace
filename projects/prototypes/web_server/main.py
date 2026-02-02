import http.server
import socketserver

# Define the port number on which the server will listen
PORT = 8000

# SimpleHTTPRequestHandler serves files from the current directory
# and its subdirectories relative to where the script is run.
Handler = http.server.SimpleHTTPRequestHandler

# Create a TCP server instance
# Binding to an empty string ("" allows the server to accept connections on any network interface.
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving static files at http://localhost:{PORT}")
    print("Press Ctrl+C to stop the server.")
    
    # Start the server and keep it running until interrupted
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped by user.")