import socket
import threading

# Configuración de red
host = '192.168.204.192'  # Dirección IPv4 del servidor
port = 12345  # Puerto arbitrario

def handle_client(conn, addr):
    """Maneja la comunicación con un cliente específico."""
    print(f"Conexión establecida desde: {addr}")
    while True:
        try:
            # Recibir datos del cliente
            data = conn.recv(1024)
            if not data:
                break
            print(f"Mensaje recibido del cliente {addr}: {data.decode('utf-8')}")

            # Enviar respuesta al cliente
            response = input(f"Ingrese la respuesta para el cliente {addr}: ")
            conn.sendall(response.encode('utf-8'))
        except ConnectionResetError:
            print(f"El cliente {addr} ha cerrado la conexión.")
            break

    # Cerrar la conexión
    conn.close()
    print(f"Conexión cerrada con: {addr}")

def main():
    # Crear un socket TCP/IP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Enlace del socket a la dirección y puerto
    sock.bind((host, port))

    # Escuchar conexiones entrantes
    sock.listen(5)  # Aumentar el número de conexiones en cola a 5

    print(f"Servidor escuchando en {host}:{port}")

    while True:
        # Esperar una conexión
        conn, addr = sock.accept()

        # Crear un nuevo hilo para manejar la conexión
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()

if __name__ == "__main__":
    main()
