from queue import Queue


class ServicioCliente:

    def __init__(self):
        self.__cola = Queue()

    def agregar_cliente(self, nombre_cliente):
        self.__cola.enqueue(nombre_cliente)
        print(f"Cliente '{nombre_cliente}' agregado a la cola.")

    def atender_cliente(self):
        if self.__cola.is_empty():
            print("No hay clientes en la cola.")
            return
        cliente = self.__cola.dequeue()
        print(f"Atendiendo al cliente '{cliente}'.")

    def clientes_es_espera(self):
        print(f"Clientes en espera: {self.__cola.size()}")


# Ejemplo de uso
cola_servicio = ServicioCliente()
cola_servicio.agregar_cliente("Brianita")
cola_servicio.agregar_cliente("Zyanya")
cola_servicio.clientes_es_espera()
cola_servicio.atender_cliente()
cola_servicio.clientes_es_espera()
cola_servicio.agregar_cliente("Mónica")
cola_servicio.clientes_es_espera()
cola_servicio.atender_cliente()
cola_servicio.clientes_es_espera()
cola_servicio.atender_cliente()
cola_servicio.atender_cliente()
