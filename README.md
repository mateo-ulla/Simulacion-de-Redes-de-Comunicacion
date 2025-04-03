# Simulación de Red en Python

Este proyecto es una simulación básica de una red de comunicación implementada en Python utilizando **Programación Orientada a Objetos (POO)**. Simula la comunicación entre un **servidor** y **tres clientes**, permitiendo enviar mensajes desde el servidor a todos los clientes conectados.

## Características
- Implementa la clase `Nodo`, que representa un dispositivo en la red.
- Permite conectar nodos entre sí.
- Simula el envío y recepción de mensajes.
- Uso de listas y métodos para gestionar conexiones.

## Explicación
1. **Clase `Nodo`**: Representa un nodo en la red con un nombre y una lista de conexiones.
2. **Métodos**:
   - `agregar_conexion(nodo)`: Conecta el nodo con otro.
   - `enviar_mensaje(mensaje)`: Envía un mensaje a todos los nodos conectados.
   - `recibir_mensaje(mensaje, emisor)`: Recibe un mensaje de otro nodo.
3. **Creación de nodos**: Se instancian un servidor y tres clientes.
4. **Conexión del servidor con los clientes**.
5. **Envío de un mensaje desde el servidor a todos los clientes**.

