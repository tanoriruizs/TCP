import socket

def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(('localhost', 5000))
    servidor.listen()
    print("Servidor escuchando en el puerto 5000...")
    
    while True:
        conn, addr = servidor.accept()
        print(f"Conexión establecida con {addr}")
        
        while True:
            datos = conn.recv(1024).decode('utf-8')
            if not datos:
                break
            print(f"Mensaje recibido: {datos}")
            
            if datos.upper() == "DESCONEXION":
                print("Cliente desconectado.")
                conn.close()
                break
            

            respuesta = datos.lower().replace("servidor", "cliente").upper()
            conn.send(respuesta.encode('utf-8'))

if __name__ == "__main__":
    iniciar_servidor()