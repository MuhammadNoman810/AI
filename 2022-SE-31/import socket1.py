import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ("127.0.0.1", 9000)
client_socket.connect(server_address)

print("Connected!")

try:
    message = input("Enter something to send: ")
    client_socket.sendall(message.encode())
    data = client_socket.recv(1024)
    print(f"Received from server: {data.decode()}")
except Exception as e:
    print(f"An error occurred!\n{e}")
finally:
    client_socket.close()