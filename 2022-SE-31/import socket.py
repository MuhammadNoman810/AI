import socket
def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a TCP client socket
    server_address = ('127.0.0.1', 65432) # Define server IP and port (replace with actual server IP for remote testing)
    try:
        client_socket.connect(server_address) # Connect to the server
        print(f"Connected to server at {server_address[0]}:{server_address[1]}")
        while True:
            message = input("You (Client): ") # Get input from the user
            if message.lower() == "exit":
                print("Closing connection...")
                break
        client_socket.sendall(message.encode()) # Send the message to the server
        data = client_socket.recv(1024) # Receive response from the server
        print(f"Server: {data.decode()}") # Print server&#39;s response
    except ConnectionRefusedError:
        print("Failed to connect to the server. Is the server running?")
    finally:
        client_socket.close() # Close the socket when done
if _name_ == '_main_':
    start_client() # Start the client