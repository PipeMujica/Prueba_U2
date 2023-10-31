#MENÚ INTERACTIVO
def agregar_compra(compras, total_gastado):
    monto_compra = float(input("Ingrese el monto de la compra: "))
    compras.append(monto_compra)
    total_gastado += monto_compra
    print("Compra agregada correctamente.")
    return total_gastado

def mostrar_compras(compras):
    if not compras:
        print("No hay compras registradas")
    else:
        for i, compras in enumerate(compras, start=1):
            print(f"{i}. ${compras}")

def mostrar_total(total_gastado):
    print(f"Total gastado: ${total_gastado}")

def main():
    compras = []
    total_gastado = 0

    while True:
        print("\nMenú:")
        print("1. Agregar compra")
        print("2. Mostrar compras")
        print("3. Mostrar total gastado")
        print("4. Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
           total_gastado = agregar_compra(compras, total_gastado)
        elif opcion == 2:
            print("Compras:")
            mostrar_compras(compras)
        elif opcion == 3:
            mostrar_total(total_gastado)
        elif opcion == 4:
            print("¡Hasta luego!")
            exit()
        else:
            print("Seleccione una opción correcta")

main()

