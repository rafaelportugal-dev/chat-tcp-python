import socket

HOST = 'localhost'
PORT = 50000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

while True:
    msg = input("Você: ")
    client.send(msg.encode())
    resposta = client.recv(1024).decode()
    print("Servidor:", resposta)
