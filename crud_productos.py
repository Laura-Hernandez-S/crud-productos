
productos = []
siguiente_id = 1


def validar_datos(nombre, descripcion, precio, cantidad):
    if nombre.strip() == "":
        raise ValueError("El nombre no puede estar vacío.")
    if descripcion.strip() == "":
        raise ValueError("La descripción no puede estar vacía.")
    if precio < 0:
        raise ValueError("El precio no puede ser negativo.")
    if cantidad < 0:
        raise ValueError("La cantidad no puede ser negativa.")


def buscar_producto(id_producto):
    for producto in productos:
        if producto["id"] == id_producto:
            return producto
    return None


def crear_producto(nombre, descripcion, precio, cantidad):
    global siguiente_id

    validar_datos(nombre, descripcion, precio, cantidad)

    producto = {
        "id": siguiente_id,
        "nombre": nombre,
        "descripcion": descripcion,
        "precio": precio,
        "cantidad": cantidad,
    }
    productos.append(producto)
    siguiente_id += 1
    return producto


def listar_productos():
    return productos


def consultar_producto(id_producto):
    producto = buscar_producto(id_producto)
    if producto is None:
        raise ValueError("No existe un producto con el ID " + str(id_producto))
    return producto


def actualizar_producto(id_producto, nombre, descripcion, precio, cantidad):
    producto = consultar_producto(id_producto)
    validar_datos(nombre, descripcion, precio, cantidad)

    producto["nombre"] = nombre
    producto["descripcion"] = descripcion
    producto["precio"] = precio
    producto["cantidad"] = cantidad
    return producto


def eliminar_producto(id_producto):
    producto = consultar_producto(id_producto)
    productos.remove(producto)
    return producto


def mostrar_producto(producto):
    print("ID:", producto["id"])
    print("Nombre:", producto["nombre"])
    print("Descripción:", producto["descripcion"])
    print("Precio:", producto["precio"])
    print("Cantidad:", producto["cantidad"])
    print("-" * 20)


def pedir_datos():
    nombre = input("Nombre: ")
    descripcion = input("Descripción: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    return nombre, descripcion, precio, cantidad


def menu():
    opcion = ""
    while opcion != "6":
        print("\n--- REGISTRO DE PRODUCTOS ---")
        print("1. Crear producto")
        print("2. Listar productos")
        print("3. Consultar producto")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Salir")
        opcion = input("Elija una opción: ")

        try:
            if opcion == "1":
                nombre, descripcion, precio, cantidad = pedir_datos()
                producto = crear_producto(nombre, descripcion, precio, cantidad)
                print("Producto creado con ID", producto["id"])
            elif opcion == "2":
                if len(listar_productos()) == 0:
                    print("No hay productos registrados.")
                for producto in listar_productos():
                    mostrar_producto(producto)
            elif opcion == "3":
                id_producto = int(input("ID del producto: "))
                mostrar_producto(consultar_producto(id_producto))
            elif opcion == "4":
                id_producto = int(input("ID del producto a actualizar: "))
                nombre, descripcion, precio, cantidad = pedir_datos()
                actualizar_producto(id_producto, nombre, descripcion, precio, cantidad)
                print("Producto actualizado.")
            elif opcion == "5":
                id_producto = int(input("ID del producto a eliminar: "))
                eliminar_producto(id_producto)
                print("Producto eliminado.")
            elif opcion != "6":
                print("Opción no válida.")
        except ValueError as error:
            print("Error:", error)

    print("Programa terminado.")


if __name__ == "__main__":
    menu()