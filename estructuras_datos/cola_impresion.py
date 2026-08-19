from queue import Queue


class ColaImpresion:

    def __init__(self):
        self.__cola = Queue()

    def agregar_trabajo(self, nombre_trabajo):
        self.__cola.enqueue(nombre_trabajo)
        print(f"Cliente '{nombre_trabajo}' agregado a la cola.")

    def procesar_trabajo(self):
        if self.__cola.is_empty():
            print("No hay trabajos en la cola.")
            return
        trabajo = self.__cola.dequeue()
        print(f"Procesando trabajo'{trabajo}'.")

    def numero_de_trabajos(self):
        if not self.__cola:
            print("La cola de impresión está vacía.")
        print(f"Trabajos en la cola: {self.__cola.size()}")


# Ejemplo de uso
cola_impresion = ColaImpresion()
cola_impresion.agregar_trabajo("Documento1.pdf")
cola_impresion.agregar_trabajo("Foto2.jpg")
cola_impresion.numero_de_trabajos()
cola_impresion.procesar_trabajo()
cola_impresion.procesar_trabajo()
cola_impresion.procesar_trabajo()
