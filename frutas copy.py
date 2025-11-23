from flask import Flask, render_template, request, jsonify, reidrect, url_for
from flas_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://carlos:74097400Cr.@localhost/frutas_db'
db = SQLAlchemy(app)

class Fruta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True, nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)


@app.route('/')
def mostrar_inventario(inventario):
    for fruta, cantidad in inventario.items():
        print(f"{fruta}: {cantidad}")

@app.route('/agregar', methods=['POST'])
def agregar_fruta(inventario, fruta, cantidad):
    if fruta in inventario:
        inventario[fruta] += cantidad
    else:
        inventario[fruta] = cantidad

@app.route('/vender', methods=['POST'])
def vender_fruta(inventario, fruta, cantidad):
    if fruta in inventario:
        if inventario[fruta] >= cantidad:
            inventario[fruta] -= cantidad
        else:
            print(f"No hay suficientes {fruta} para vender.")   

@app.route('/eliminar', methods=['POST'])
def eliminar_fruta(inventario, fruta, cantidad):
    if fruta in inventario:
        if inventario[fruta] >= cantidad:
            inventario[fruta] -= cantidad
        else:
            print(f"No hay suficientes {fruta} para eliminar.")
    else:
        print(f"{fruta} no está en el inventario.")


# # Esta función representa el punto de entrada principal del programa.
# # Proporciona un menú interactivo para que el usuario pueda realizar
# # operaciones en el inventario de frutas.
# def main():
#     while True:
#         # Mostrar las opciones disponibles al usuario.
#         print("\nOpciones:")
#         print("1. Mostrar inventario")
#         print("2. Agregar fruta")
#         print("3. Vender fruta")
#         print("4. Eliminar fruta")
#         print("5. Salir")
        
#         # Solicitar al usuario que seleccione una opción.
#         opcion = input("Seleccione una opción: ")
        
#         # Lógica para manejar cada opción seleccionada.
#         if opcion == "1":
#             # Mostrar el inventario actual.
#             mostrar_inventario(inventario)
#         elif opcion == "2":
#             # Agregar una nueva fruta al inventario.
#             fruta = input("Ingrese el nombre de la fruta a agregar: ")
#             cantidad = int(input("Ingrese la cantidad a agregar: "))
#             agregar_fruta(inventario, fruta, cantidad)
#         elif opcion == "3":
#             # Vender una cantidad específica de una fruta.
#             fruta = input("Ingrese el nombre de la fruta a vender: ")
#             cantidad = int(input("Ingrese la cantidad a vender: "))
#             vender_fruta(inventario, fruta, cantidad)
#         elif opcion == "4":
#             # Eliminar una cantidad específica de una fruta.
#             fruta = input("Ingrese el nombre de la fruta a eliminar: ")
#             cantidad = int(input("Ingrese la cantidad a eliminar: "))
#             eliminar_fruta(inventario, fruta, cantidad)
#         elif opcion == "5":
#             # Salir del programa.
#             print("Saliendo del programa.")
#             break
#         else:
#             # Manejar entradas no válidas.
#             print("Opción no válida. Intente de nuevo.")   

# # Verificar si este archivo se está ejecutando directamente.
# if __name__ == "__main__":
#     main()
