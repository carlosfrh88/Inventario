inventario ={
    "manzanas": 10,
    "naranjas": 5,
    "platanos": 8  
}

def mostrar_inventario(inventario):
    for fruta, cantidad in inventario.items():
        print(f"{fruta}: {cantidad}")
def agregar_fruta(inventario, fruta, cantidad):
    if fruta in inventario:
        inventario[fruta] += cantidad
    else:
        inventario[fruta] = cantidad
def vender_fruta(inventario, fruta, cantidad):
    if fruta in inventario:
        if inventario[fruta] >= cantidad:
            inventario[fruta] -= cantidad
        else:
            print(f"No hay suficientes {fruta} para vender.")   
def eliminar_fruta(inventario, fruta, cantidad):
    if fruta in inventario:
        if inventario[fruta] >= cantidad:
            inventario[fruta] -= cantidad
        else:
            print(f"No hay suficientes {fruta} para eliminar.")
    else:
        print(f"{fruta} no está en el inventario.")
def main():
    while True:
        print("\nOpciones:")
        print("1. Mostrar inventario")
        print("2. Agregar fruta")
        print("3. Vender fruta")
        print("4. Eliminar fruta")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            mostrar_inventario(inventario)
        elif opcion == "2":
            fruta = input("Ingrese el nombre de la fruta a agregar: ")
            cantidad = int(input("Ingrese la cantidad a agregar: "))
            agregar_fruta(inventario, fruta, cantidad)
        elif opcion == "3":
            fruta = input("Ingrese el nombre de la fruta a vender: ")
            cantidad = int(input("Ingrese la cantidad a vender: "))
            vender_fruta(inventario, fruta, cantidad)
        elif opcion == "4":
            fruta = input("Ingrese el nombre de la fruta a eliminar: ")
            cantidad = int(input("Ingrese la cantidad a eliminar: "))
            eliminar_fruta(inventario, fruta, cantidad)
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")   
if __name__ == "__main__":
    mostrar_inventario(inventario)
