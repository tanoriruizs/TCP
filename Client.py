import socket

def iniciar_cliente():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(('localhost', 5000))
    print("Conexión establecida con el servidor.")
    
    while True:
        mensaje = input("Cliente envía: ")
        
        if mensaje.strip() == "":
            print("ERROR: Por favor ingrese un mensaje para enviar")
            continue
        
        cliente.send(mensaje.encode('utf-8'))
        
        if mensaje.upper() == "DESCONEXION":
            print("Servidor cierra la conexión con el cliente.")
            cliente.close()
            break
        
        respuesta = cliente.recv(1024).decode('utf-8')
        print(f"Servidor responde: {respuesta}")

if __name__ == "__main__":
    iniciar_cliente()
