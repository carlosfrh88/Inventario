inventario = {
    "Jeringas": 50,
    "Suero": 30,
    "Gaza": 20,
    "Vendas": 40,
    "Antisépticos": 25 
}

def mostrar_inventario():
    print("Inventario de suministros:")
    for item, cantidad in inventario.items():
        print(f"{item}: {cantidad} unidades")

def agregar_suministro(item, cantidad):
    if item in inventario:
        inventario[item] += cantidad
    else:
        inventario[item] = cantidad
    print(f"Se han agregado {cantidad} unidades de {item}.")
    mostrar_inventario()

def usar_suministro(item, cantidad):
    if item in inventario and inventario[item] >= cantidad:
        inventario[item] -= cantidad
        print(f"Se han usado {cantidad} unidades de {item}.")
    else:
        print(f"No hay suficiente {item} en el inventario.")
    mostrar_inventario()

print("Sistema de Gestión de Inventario de Suministros")
print("1. Mostrar inventario")
print("2. Agregar suministro")
print("3. Usar suministro") 


opcion = input("Seleccione una opción (1-3): ")
if opcion == '1':
    mostrar_inventario()
elif opcion == '2':
    item = input("Ingrese el nombre del suministro a agregar: ")
    cantidad = int(input("Ingrese la cantidad a agregar: "))
    agregar_suministro(item, cantidad)
elif opcion == '3':
    item = input("Ingrese el nombre del suministro a usar: ")
    cantidad = int(input("Ingrese la cantidad a usar: "))
    usar_suministro(item, cantidad)
else:
    print("Opción no válida.")
