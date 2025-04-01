class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.conexiones = []  

    def agregar_conexion(self, nodo):
        self.conexiones.append(nodo)

    def enviar_mensaje(self, mensaje):
        print(f"{self.nombre} envía: {mensaje}")
        for nodo in self.conexiones:
            nodo.recibir_mensaje(mensaje, self.nombre)

    def recibir_mensaje(self, mensaje, emisor):
        print(f"{self.nombre} recibio mensaje de {emisor}: {mensaje}")

servidor = Nodo("servidor")
cliente1 = Nodo("cliente 1")
cliente2 = Nodo("cliente 2")
cliente3 = Nodo("cliente 3")

servidor.agregar_conexion(cliente1)
servidor.agregar_conexion(cliente2)
servidor.agregar_conexion(cliente3)

servidor.enviar_mensaje("hola clientes")
