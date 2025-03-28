import socket
from colorama import init, Fore

init(autoreset=True)

def iniciar_cliente():
    try:
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.connect(('localhost', 5000))
        print(Fore.GREEN + "Conexión establecida con el servidor.")
    except Exception as e:
        print(Fore.RED + f"Error al conectar con el servidor: {e}")
        return

    try:
        while True:
            mensaje = input(Fore.YELLOW + "Cliente envía: ").strip()

            if not mensaje:
                print(Fore.RED + "ERROR: Por favor ingrese un mensaje para enviar")
                continue

            cliente.send(mensaje.encode('utf-8'))

            if mensaje.upper() == "DESCONEXION":
                print(Fore.RED + "Cliente ha solicitado la desconexión.")
                break

            respuesta = cliente.recv(1024).decode('utf-8')
            print(Fore.CYAN + f"Servidor responde: {respuesta}")
    except Exception as e:
        print(Fore.RED + f"Error en la comunicación: {e}")
    finally:
        cliente.close()
        print(Fore.RED + "Conexión con el servidor cerrada.")

if __name__ == "__main__":
    iniciar_cliente()
