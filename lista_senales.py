from nodo_senal import nodo_senal

class lista_senales:

    def __init__(self):
        self.primero = None
        self.contador_senales = 0

    def insertar_senal(self, senal):
        if self.primero is None:
            self.primero = nodo_senal(senal = senal)
            self.contador_senales += 1
            return
        
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo_senal (senal = senal)
        self.contador_senales +=1
    
    def recorre_imprimirLista_senal(self):
        print("*****************************************")
        print("Total senales: ", self.contador_senales)
        print("")
        print("")

        actual = self.primero
        while actual != None:
            print("Nombre: ", actual.senal.nombre, "Tiempo: ", actual.senal.tiempo,
                   "Amplitud: ", actual.senal.amplitud)
            actual.senal.lista_datos.recorrer_imprimirLista()
            actual.senal.lista_patrones.recorrer_imprimirLista()
            actual = actual.siguiente
            print("")
            print("")
        print("*****************************************")
        print("")
        print("")


    def graficar_list_original(self):

        actual = self.primero
        while actual != None:
            
            actual.senal.lista_datos.graficar_datos(actual.senal.nombre, str(actual.senal.tiempo),str(actual.senal.amplitud))
            
            actual = actual.siguiente

    def graficar_list_patrones(self):

        actual = self.primero
        while actual != None:
            
            actual.senal.lista_patrones.graficar_datos(actual.senal.nombre, str(actual.senal.tiempo),str(actual.senal.amplitud))
            
            actual = actual.siguiente