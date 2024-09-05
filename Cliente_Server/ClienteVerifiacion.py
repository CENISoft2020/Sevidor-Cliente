import socket

def check_port(host, port):
    """Verifica si el puerto está ocupado en el host especificado."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)  # Tiempo de espera para la conexión
        result = sock.connect_ex((host, port))
        return result == 0  # Retorna True si el puerto está en uso

# Configuración de red
host = '192.168.204.71'  # Dirección IPv4 del servidor
port = 12345  # Puerto arbitrario

# Verificar si el puerto está ocupado
if check_port(host, port):
    print(f"El puerto {port} en el host {host} está ocupado.")
else:
    print(f"El puerto {port} en el host {host} está disponible.")

    # Crear un socket TCP/IP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conectar el socket al servidor remoto
    try:
        sock.connect((host, port))
    except Exception as e:
        print(f"No se pudo conectar al servidor: {e}")
        sock.close()
        exit(1)

    while True:
        # Enviar datos al servidor
        message = input("Ingrese un mensaje para el servidor: ")
        sock.sendall(message.encode('utf-8'))

        # Recibir respuesta del servidor
        data = sock.recv(1024)
        print(f"Respuesta del servidor: {data.decode('utf-8')}")

        # Preguntar al usuario si desea enviar otro mensaje
        continuar = input("¿Desea enviar otro mensaje? (s/n): ")
        if continuar.lower() != 's':
            break

    # Cerrar la conexión
    sock.close()
