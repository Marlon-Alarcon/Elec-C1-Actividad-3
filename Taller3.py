import os, time

class Empleado():

    def __init__(self):
        self.empleados = {}
        self.cont = 0

    def agregarEmpleado(self):
        self.codigo = input("Ingrese el codigo: ")
        self.nombre = input("Ingrese el nombre: ")
        self.apellido = input("Ingrese el apellido: ")
        self.direccion = input("Ingrese la direccion: ")
        self.telefono = input("Ingrese el telefono: ")
        self.sueldo = float (input("Ingrese el sueldo: "))
        self.alimentacion = 0
        self.transporte = 0

        if (self.sueldo<2000000):
            self.alimentacion = 80000
            self.transporte = 60000
        
        self.pension = (self.sueldo * 0.04)
        self.salud = (self.sueldo * 3.375)/100

        self.devengado = self.alimentacion + self.transporte + self.sueldo

        self.deduccion = (self.sueldo - self.salud - self.pension)

        self.empleados[self.codigo] = (self.nombre, self.apellido, self.direccion, self.telefono, self.sueldo , self.alimentacion, self.transporte, self.pension, self.salud, self.devengado, self.deduccion)        
        #self.cont = self.cont + 1
        print("")
        time.sleep(0.6)
        print(" ------ Datos Agregados ------ ")
        print("")
        time.sleep(0.3)
        input("Presione una tecla para continuar")

    def mostrarEmpleado(self):
        if len(self.empleados) == 0:
            print(" -------- Vacio -------- ")
            print("No hay datos para mostrar")
            print("")
            input("Presione una tecla para continuar")
        
        else:
            for i, v in self.empleados.items():
                print(f"{i}: {v}")
            time.sleep(0.3)
            print("")
            input("Presione una tecla para continuar")
            print("")

    def eliminarEmpleado(self):
        if len(self.empleados) == 0:
            print("No hay nada que eliminar")

    


               

def limpiar():
    os.system ("clear")

def menu():
    men = 0
    em = Empleado()
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
            print("")
            em.agregarEmpleado()
            limpiar()
        
        elif men == 2:
            print("")
            em.mostrarEmpleado()
            limpiar()
           

        elif men == 3:
            print("Opcion 3")
            

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
            limpiar()

if __name__ == "__main__":
    menu()