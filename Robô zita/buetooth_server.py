import bluetooth

# Cria um socket Bluetooth
server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

# Define o endereço e a porta para o bind
port = 1
server_socket.bind(("", port))

# Coloca o socket em modo de escuta
server_socket.listen(1)

print("Aguardando conexão...")

# Aceita a conexão de um cliente
client_socket, address = server_socket.accept()
print("Conectado a", address)

try:
    while True:
        # Recebe os dados do cliente (até 1024 bytes)
        data = client_socket.recv(1024)
        if not data:  # Verifica se a conexão foi fechada pelo cliente
            break
        print("Recebido:", data.decode())  # Decodifica e imprime os dados recebidos
except KeyboardInterrupt:
    print("Interrompido pelo usuário")
finally:
    # Fecha as conexões
    client_socket.close()
    server_socket.close()
    print("Conexões fechadas")