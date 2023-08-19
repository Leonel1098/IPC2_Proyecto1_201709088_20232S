import tkinter as tk
from tkinter import Tk
from tkinter import filedialog

def CargarArchivo():
    root = Tk()
    root.withdraw()
    root.attributes("-topmost", True)

    archivo = filedialog.askopenfilename()
    if archivo:
        print("Archivo seleccionado:", archivo)
        print("")
        archivo_texto = open(archivo, "r+", encoding = "utf8")
        array_chars = []
        for line in archivo_texto.readlines():
            
            for char in line.replace(" ",";").split(";"):
                array_chars.append(char) 
        print(array_chars)

        global Data
        Data = archivo_texto
        #print(Data)
        print("")
        print("Carga Exitosa")
        print("")
        
    else:
        print("")
        print("No se seleccionó ningún archivo.")


    




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
        opcion= input ("Por favor Ingrese una opción del menú: ")
    
        if opcion == "1":
            CargarArchivo()
        elif opcion == "2":
           pass
        elif opcion == "3":
            pass
        elif opcion == "4":
            print("")
            print(" Leonel Antonio González García \n 201709088 \n Introducción a la Programación y Computación 2 sección D \n Cuarto Semestre \n Ingenieria en Ciencias y Sistemas")

        elif opcion == "5":
            pass
        elif opcion == "6":
            pass
        elif opcion == "7":
            print("Saliendo del programa, vuevla pronto")
            break
        else:
            print("")
            print("Indique una opción válida...\n Seleccione una tecla para continuar...")

    
Menu() 