# Servidor y Cliente con Sockets en Python

Este proyecto implementa un servidor y un cliente en Python que se comunican mediante sockets. El servidor escucha conexiones entrantes y responde a los mensajes del cliente con una versión modificada del mensaje recibido.

## Archivos del Proyecto

- `servidor.py`: Contiene el código del servidor.
- `cliente.py`: Contiene el código del cliente.

## Funcionamiento

### Servidor
El servidor escucha en el puerto 5000 de `localhost`. Cuando un cliente se conecta, el servidor:
1. Recibe el mensaje enviado por el cliente.
2. Si el mensaje es "DESCONEXION", cierra la conexión.
3. Modifica el mensaje recibido reemplazando la palabra "SERVIDOR" con "CLIENTE", lo convierte en mayúsculas y lo envía de vuelta.
4. Continúa escuchando nuevos mensajes hasta que el cliente se desconecte.

### Cliente
El cliente se conecta al servidor en `localhost` y el puerto 5000. Su funcionamiento es el siguiente:
1. Solicita al usuario ingresar un mensaje.
2. Envía el mensaje al servidor.
3. Si el mensaje es "DESCONEXION", cierra la conexión.
4. Recibe la respuesta del servidor y la muestra en pantalla.
5. Permite el envío de múltiples mensajes hasta que el usuario decida desconectarse.

## Ejecución

### Ejecutar el Servidor
Ejecuta el siguiente comando en la terminal para iniciar el servidor:
```sh
python servidor.py
```

### Ejecutar el Cliente
En otra terminal, ejecuta el siguiente comando para iniciar el cliente:
```sh
python cliente.py
```

Luego, puedes escribir mensajes en el cliente para enviarlos al servidor y recibir respuestas.

## Notas
- Asegúrate de ejecutar el servidor antes que el cliente.
- El cliente se desconectará correctamente si se envía el mensaje "DESCONEXION".
- Puedes modificar el código para mejorar la funcionalidad o agregar nuevas características.
- Para Interrumpir el servidor de manera manual se tiene que utilizar la combinación CTRL + C

