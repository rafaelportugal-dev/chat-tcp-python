import socket

HOST = 'localhost'
PORT = 50000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Servidor aguardando conexão...")

conn, addr = server.accept()
print("Conectado com:", addr)

while True:
    msg = conn.recv(1024).decode()
    if not msg:
        break
    print("Cliente:", msg)
    resposta = input("Você: ")
    conn.send(resposta.encode())

conn.close()
