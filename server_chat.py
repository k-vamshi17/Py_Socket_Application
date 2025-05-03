import socket
import threading


clients=[]

def handle_client(client_socket,addr):
    while True:
        msg=client_socket.recv(1024)
        msg=msg.decode()
        broadcast(msg,client_socket)

def broadcast(message,client_socket):
    for client in clients:
        client.send(message.encode())

def start_server(host="localhost",port=5555):
    server=socket.socket()
    server.bind((host,port))
    server.listen()
    print(f'Server is running on {host}:{port}')
    while True:
        client_socket,addr=server.accept()
        clients.append(client_socket)
        thread=threading.Thread(target=handle_client,args=(client_socket,addr))
        thread.start()
        
        
start_server()    
