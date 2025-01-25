import socket

#Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Define the host and port connect to 
host = '127.0.0.1' #localhost
port = 12345

#Bind to the server to the address
server_socket.bind((host, port))

#Start listening for incoming connections
server_socket.listen(5)

print(f'Server listening on {host}:{port}...')

#Accept a connection and get the client socket
client_socket, client_address = server_socket.accept()
print(f'Connection established with {client_address}')

#Recive data from the client
data = client_socket.recv(1024).decode('utf-8')
print(f'Recived: {data}')

#Echo the received data back to the client
client_socket.send(data.encode('utf-8'))

#close the sockets
client_socket.close()
server_socket.close()