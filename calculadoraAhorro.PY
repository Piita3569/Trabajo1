ingresos = []
gastos = []

def registrar_ingreso():
    print("\n--- Registrar ingreso ---")
    nombre = input("Nombre del ingreso: ").strip()
    if nombre == "":
        print("El nombre no puede estar vacío.")
        return
    try:
        monto = float(input("Monto del ingreso: "))
        if monto <= 0:
            print("El monto debe ser mayor que cero.")
            return
    except ValueError:
        print("Debes ingresar un número válido.")
        return

    ingresos.append({"nombre": nombre, "monto": monto})
    print(f"Ingreso '{nombre}' por ${monto} registrado correctamente.")

def registrar_gasto():
    print("\n---registrar_gasto ---")
    nombre = input("Nombre del gasto: ").strip()
    if nombre == "":
        print("El nombre no puede estar vacío.")
        return
    try:
        monto = float(input("Monto del gasto: "))
        if monto <= 0:
            print("El monto debe ser mayor que cero.")
            return
    except ValueError:
        print("Debes ingresar un número válido.")
        return
    gastos.append({"nombre":nombre, "monto":monto})
    print(f"Gastos '{nombre}' por ${monto:.2f} registrado correctamente.")

def ver_resumen_mensual():
    total_ingresos = 0
    total_gastos = 0
    saldos = 0
    print("\n--- Ver_resumen_mensual ---")
    if not ingresos and not gastos:
        print("No hay datos registrados")
        return

    total_ingresos = sum(item["monto"] for item in ingresos) 
    total_gastos = sum(item["monto"] for item in gastos)
    saldos = total_ingresos - total_gastos
    print(f"El total de ingreso mensual es :{total_ingresos}")
    print(f"El total de gastos mensual es: {total_gastos}")
    print(f"\nSu monto de ahorro total es: {saldos}")

def eliminar_ingreso_o_gasto():
    tipo = input("Eliminar ingreso (i) o gasto (g): ").lower()
    if tipo == "i":
        for i, ingreso in enumerate(ingresos, 1):
            print(f"{i}. {ingreso['nombre']} - ${ingreso['monto']}")
        num = int(input("Número a eliminar: "))
        if num> len(ingreso):
            print(f"El numero del registro no existe, existen registrados: {len(ingreso)}")
        else:
            ingresos.pop(num - 1)
            print("Ingreso eliminado.")
    elif tipo == "g":
        for i, gasto in enumerate(gastos, 1):
            print(f"{i}. {gasto['nombre']} - ${gasto['monto']}")
        num = int(input("Número a eliminar: "))
        if num> len(gasto):
            print(f"El numero del registro no existe, existen registrados: {len(gasto)}")
        else:
            gastos.pop(num - 1)
            print("Gasto eliminado.")
    else:
        print("Opción inválida.")


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
                print("¡Gracias por usar la calculadora!")
                break
            else:
                print("Opción fuera de rango. Debe ser un número del 1 al 5.")
        except ValueError:
            print("Entrada inválida. Debes ingresar un número del 1 al 5.")

menu()
