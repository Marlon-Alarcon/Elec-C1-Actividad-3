
def menu():
    men = 0
    while men != 4:
        print("")
        print("  ╔════════════════════════╗")
        print("  ║    ----  MENÚ  ----    ║")
        print("  ╚════════════════════════╝")
        print("  ║ 1. AGREGAR EMPLEADO    ║")
        print("  ║ 2. MOSTRAR EMPLEADO    ║")
        print("  ║ 3. ELIMINAR EMPLEADO   ║")
        print("  ║ 4. Salir               ║")
        print("  ╚════════════════════════╝")
        print("")
        men = int(input(" Ingrese una opcion por favor "))

        if men == 1:
            print("OPCION 1")
        
        elif men == 2:
            print("OPCION 2")
            print("prueba")
           

        elif men == 3:
            print("OPCION 3")

        elif men == 4:
            print("")
            print(" -----   Has salido   -----")
            print(" ***** Muchas Gracias *****")
        
        else:
            print("")
            print(" -----  Opcion no valida  -----")
            print(" ----- Intente Nuevamente -----")
            print("")
            input(" -- Presione una tecla para continuar")
            print("")

if __name__ == "__main__":
    menu()