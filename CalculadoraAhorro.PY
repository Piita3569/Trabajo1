ingresos = []
gastos = []

def registrar_ingreso():
    print("\n--- Función 'registrar_ingresos()' aún no implementada ---")

# Función a completar por Pablo
def registrar_gasto():
    print("\n--- Función 'registrar_gasto()' aún no implementada ---")

# Función a completar por María Pía
def ver_resumen_mensual():
    print("\n--- Función 'ver_resumen_mensual()' aún no implementada ---")

# Función a completar por Luis
def eliminar_ingreso_o_gasto():
    print("\n--- Función 'eliminar_ingreso_o_gasto()' aún no implementada ---")


def menu():
    while True:
        print("\n===== CALCULADORA DE AHORRO MENSUAL =====")
        print("1. Registrar ingreso")
        print("2. Registrar gasto")
        print("3. Ver resumen mensual")
        print("4. Eliminar ingreso o gasto")
        print("5. Salir")
        opcion = input("Elige una opción (1-5): ")

        try:
            opcion = int(opcion)
            if opcion == 1:
                registrar_ingreso()
            elif opcion == 2:
                registrar_gasto()
            elif opcion == 3:
                ver_resumen_mensual()
            elif opcion == 4:
                eliminar_ingreso_o_gasto()
            elif opcion == 5:
                print("👋 ¡Gracias por usar la calculadora!")
                break
            else:
                print("Opción fuera de rango. Debe ser un número del 1 al 5.")
        except ValueError:
            print("Entrada inválida. Debes ingresar un número del 1 al 5.")

menu()
