# Lista para almacenar los productos
productos = []

# Función para la carga de los datos desde el archivo
def cargar_datos():
    """Carga los productos desde el archivo productos.txt, si existe."""
    try:
        with open("productos.txt", "r") as file:
            for linea in file:
                nombre, precio, cantidad, descripcion = linea.strip().split(", ")
                productos.append({
                    'nombre': nombre,
                    'precio': float(precio),
                    'cantidad': int(cantidad),
                    'descripcion': descripcion
                })
        print("Datos cargados exitosamente.")
    except FileNotFoundError:
        print("Archivo no encontrado, comenzando con inventario vacío.")

# Función para guardar los datos en el archivo
def guardar_datos():
    """Guarda los productos en el archivo productos.txt."""
    with open("productos.txt", "w") as file:
        for producto in productos:
            file.write(f"{producto['nombre']}, {producto['precio']}, {producto['cantidad']}, {producto['descripcion']}\n")
    print("Datos guardados exitosamente.")

# Función para añadir un producto al programa, anadí también la descripción para los productos5
def añadir_producto():
    """Permite añadir un nuevo producto al inventario."""
    nombre = input("Introduce el nombre del producto: ")
    while True:
        try:
            precio = float(input("Introduce el precio del producto: "))
            cantidad = int(input("Introduce la cantidad disponible del producto: "))
            break
        except ValueError:
            print("Precio y cantidad deben ser numéricos. Inténtalo de nuevo.")
    
    descripcion = input("Introduce la descripción del producto: ")
    
    productos.append({'nombre': nombre, 'precio': precio, 'cantidad': cantidad, 'descripcion': descripcion})
    print(f"Producto '{nombre}' añadido con éxito.")

# Función para ver todos los productos del programa
def ver_productos():
    """Muestra todos los productos en el inventario."""
    if productos:
        print("\nInventario de productos:")
        for idx, producto in enumerate(productos, 1):
            print(f"{idx}. Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}, Descripción: {producto['descripcion']}")
    else:
        print("No hay productos en el inventario.")

# Función para actualizar un producto en el programa
def actualizar_producto():
    """Permite actualizar los detalles de un producto existente."""
    ver_productos()
    nombre = input("Introduce el nombre del producto que deseas actualizar: ")
    
    for producto in productos:
        if producto['nombre'].lower() == nombre.lower():
            print(f"Actualizando '{producto['nombre']}'")
            nuevo_precio = input(f"Nuevo precio ({producto['precio']}): ")
            nueva_cantidad = input(f"Nuevo cantidad ({producto['cantidad']}): ")
            nueva_descripcion = input(f"Nueva descripción ({producto['descripcion']}): ")
            
            if nuevo_precio:
                try:
                    producto['precio'] = float(nuevo_precio)
                except ValueError:
                    print("El precio debe ser un valor numérico.")
            if nueva_cantidad:
                try:
                    producto['cantidad'] = int(nueva_cantidad)
                except ValueError:
                    print("La cantidad debe ser un valor numérico.")
            if nueva_descripcion:
                producto['descripcion'] = nueva_descripcion
                    
            print(f"Producto '{producto['nombre']}' actualizado con éxito.")
            return
    print(f"Producto '{nombre}' no encontrado.")

# Función para eliminar un producto del programa
def eliminar_producto():
    """Elimina un producto basado en su nombre."""
    ver_productos()
    nombre = input("Introduce el nombre del producto que deseas eliminar: ")
    
    for producto in productos:
        if producto['nombre'].lower() == nombre.lower():
            productos.remove(producto)
            print(f"Producto '{nombre}' eliminado con éxito.")
            return
    print(f"Producto '{nombre}' no encontrado.")

# Función para mostrar el menú y manejar las opciones
def menu():
    """Presenta el menú y maneja las opciones del usuario."""
    cargar_datos()  
    while True:
        print("\n--- Menú de Gestión de Productos ---")
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción válida.")

# Iniciar el programa
menu()
