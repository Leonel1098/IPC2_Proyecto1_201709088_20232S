def mostrar_menu():
    print("")
    print("")
    print("-------Menú-----------")
    print("1. Registrar Paciente")
    print("2. Registrar Doctor")
    print("3. Ver pacientes en el sistema")
    print("4. Ver doctores en el sistema")
    print("5. Agendar Cita")
    print("6. salir")
    opcion=input("Ingrese una opción del menú: ")
    while True:
        if opcion=="1":
            registrar_paciente()
        elif opcion=="2":
            registrar_doctor()
        elif opcion=="3":
            ver_los_pacientes()
        elif opcion=="4":
            ver_los_doctores()
        elif opcion=="5":
            agendar_una_cita()
        elif opcion=="6":
            print("Saliendo del programa, vuevla pronto")
            break
        else:
            print("Indique una opción válida")
        mostrar_menu()
            

mostrar_menu() 