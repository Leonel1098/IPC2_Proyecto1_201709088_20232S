import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import Tk
from tkinter import filedialog
from senales import senales
from datos import datos
from lista_senales import lista_senales
from lista_datos import lista_datos


def Leer_Xml():
    root = Tk()
    root.withdraw()
    root.attributes("-topmost", True)

    archivo = filedialog.askopenfilename()
    print("Archivo seleccionado:", archivo)
    print("")
    archivo_texto = open(archivo, "r+", encoding = "utf8")
    archivo_texto.close()
    tree = ET.parse(archivo)
    raiz = tree.getroot()

    lista_senalestemp = lista_senales()
    for senales_temporal in raiz.findall("senal"):
        nombre_senal = senales_temporal.get("nombre")
        tiempo_senal = senales_temporal.get("t")
        amplitud_senal = senales_temporal.get("A")
        print("")
        print(nombre_senal, tiempo_senal, amplitud_senal)

        lista_datostemp = lista_datos()
        lista_datosPatrones_temp = lista_datos()
        for dato_senal in senales_temporal.findall("dato"):
            tiempo_dato = dato_senal.get("t")
            amplitud_dato = dato_senal.get("A")
            frecuencia_dato = dato_senal.text

            nuevo_dato = datos(int(tiempo_dato),int(amplitud_dato),frecuencia_dato)
            lista_datostemp.insertar_dato(nuevo_dato)

            if frecuencia_dato != "0":
                nuevo_dato = datos(int(tiempo_dato),int(amplitud_dato),1)
                lista_datosPatrones_temp.insertar_dato(nuevo_dato)
            else:
                nuevo_dato = datos(int(tiempo_dato),int(amplitud_dato),0)
                lista_datosPatrones_temp.insertar_dato(nuevo_dato)
        
        lista_senalestemp.insertar_senal(senales(nombre_senal,tiempo_senal,amplitud_senal,lista_datostemp,lista_datosPatrones_temp))
    
    lista_senalestemp.recorre_imprimirLista_senal()





def Menu():
    while True:
        print("")
        print("------------------------------------------------------")
        print("Proyecto 1 Introducción a la Programación y Computación")
        print("------------------------------------------------------")
        print("")
        print(">->->->->->->->MENÚ<-<-<-<-<-<-<-<")
        print("")
        print("1. Cargar Archivo")
        print("2. Procesar Archivo")
        print("3. Escribir Archivo de Salida")
        print("4. Mostrar datos del Estudiante")
        print("5. Generar Gráfica")
        print("6. Inicializar sistema")
        print("7. Salida")
        print(">->->->->->->->-><-<-<-<-<-<-<-<-<")
        print()
        opcion= input ("Por favor Ingrese una opción del menú:  ")
    
        if opcion == "1":
            Leer_Xml()
        elif opcion == "2":
           pass
        elif opcion == "3":
            pass
        elif opcion == "4":
            print("")
            print(" -->Leonel Antonio González García \n -->201709088 \n -->Introducción a la Programación y Computación 2 sección D \n -->Cuarto Semestre \n -->Ingenieria en Ciencias y Sistemas")
            print("")
        elif opcion == "5":
            pass
        elif opcion == "6":
            pass
        elif opcion == "7":
            print("")
            print("Saliendo del programa, vuevla pronto")
            break
        else:
            print("")
            print("Indique una opción válida...\n Seleccione una tecla para continuar...")
            print("")

    
Menu() 