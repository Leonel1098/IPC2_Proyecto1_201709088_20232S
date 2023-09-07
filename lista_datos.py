import sys
import os
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
        print("***************************************************")
        actual = self.primero
        while actual != None:
            print("Tiempo: ", actual.dato.tiempo, "Amplitud: ", 
                  actual.dato.amplitud, "Frecuencia: ", actual.dato.frecuencia)
            actual = actual.siguiente
        #print("****************************************************")

    def graficar_datos(self, nombre_senal, tiempo, amplitud ):
        f = open("bb.dot", "w")

        text ="""
            digraph G {"t="""+tiempo+"""","A="""+amplitud+""""->" """+nombre_senal+ """" bgcolor="#5b5b5b" style="filled"
            subgraph cluster1 {fillcolor="blue:skyblue" style="filled"
            node [shape=circle fillcolor="black:white" style="radial" gradientangle=180]
            a0 [ label=<
            <TABLE border="10" cellspacing="10" cellpadding="10" style="rounded" bgcolor="blue:green" gradientangle="315">\n"""
        actual = self.primero
        sentinela_filas = actual.dato.tiempo 
        fila_iniciada=False
        while actual != None:
            
            if  sentinela_filas!=  actual.dato.tiempo:
                
                sentinela_filas = actual.dato.tiempo
                fila_iniciada=False
                
                text+="""</TR>\n"""  
            if fila_iniciada==False:
                fila_iniciada=True
               
                text+="""<TR>"""  
                text+="""<TD border="3"  bgcolor="orange" gradientangle="315">"""+str(actual.dato.frecuencia)+"""</TD>\n"""
            else:
                text+="""<TD border="3"  bgcolor="orange" gradientangle="315">"""+str(actual.dato.frecuencia)+"""</TD>\n"""
            actual = actual.siguiente
        text+=""" </TR></TABLE>>];
                }
                }\n"""
        f.write(text)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system('dot -Tpng bb.dot -o Gráfica.png')
        print("Gráfica Terminada")