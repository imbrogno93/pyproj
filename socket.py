import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("127.0.0.1", 8080))

s.listen(1)

conn, addr = s.accept()

while True:
    data = conn.recv(1024)
    if data:
        print("Ricevuto messaggio:", data.decode())
    else:
        break

conn.close()