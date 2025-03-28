import socket
from colorama import init, Fore

init(autoreset=True)  

def manejar_cliente(conn, addr):
    """Maneja la comunicación con un cliente específico."""
    print(Fore.GREEN + f"Conexión establecida con {addr}")
    with conn: 
        while True:
            try:
                datos = conn.recv(1024).decode('utf-8')
                if not datos:
                    print(Fore.RED + f"Cliente {addr} desconectado.")
                    break

                print(Fore.BLUE + f"Mensaje recibido de {addr}: {datos}")

                if datos.upper() == "DESCONEXION":
                    print(Fore.RED + f"Cliente {addr} ha solicitado la desconexión.")
                    break

                respuesta = datos.lower().replace("servidor", "cliente").upper()
                conn.send(respuesta.encode('utf-8'))
            except Exception as e:
                print(Fore.RED + f"Error con el cliente {addr}: {e}")
                break

def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(('localhost', 5000))
    servidor.listen()
    print(Fore.CYAN + "Servidor escuchando en el puerto 5000...")

    try:
        while True:
            conn, addr = servidor.accept()
            manejar_cliente(conn, addr)
    except KeyboardInterrupt:
        print(Fore.RED + "\nServidor detenido manualmente.")
    finally:
        servidor.close()
        print(Fore.RED + "Servidor cerrado.")

if __name__ == "__main__":
    iniciar_servidor()
