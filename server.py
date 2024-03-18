import socket

# Créer un serveur socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 12345))
server_socket.listen(1)

print("Attente de la connexion du client...")
conn, addr = server_socket.accept()
print("Client connecté:", addr)

# Recevoir des données du client
while True:
    data = conn.recv(1024)
    if not data:
        break
    print("Données reçues du client:", data.decode())

conn.close()
