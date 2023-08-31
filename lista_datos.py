from nodo_datos import nodo_datos
class lista_datos:

    def __init__(self):
        self.primero = None
        self.contador_dato = 0

    def insertar_dato(self, dato):
        if self.primero is None:
            self.primero = nodo_datos(dato = dato)
            self.contador_dato += 1
            return
        
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo_datos(dato = dato)
        self.contador_dato += 1

    def recorrer_imprimirLista(self):
        print("******************************************************************")
        actual = self.primero
        while actual != None:
            print("Tiempo: ", actual.dato.tiempo, "Amplitud: ", 
                  actual.dato.amplitud, "Frecuencia: ", actual.dato.frecuencia)
            actual = actual.siguiente
        print("******************************************************************")