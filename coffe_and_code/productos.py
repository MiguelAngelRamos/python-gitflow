
def agregar_producto(productos: list, nuevo_producto: str) -> None:
    """Agrega un nuevo producto al final de la lista.

    Utiliza el método .append() que es la forma estándar
    de añadir un elemento al final de una lista en Python.
    """
    # Verificamos que no exista ya para evitar duplicados
    if nuevo_producto in productos:
        print(f" '{nuevo_producto}' ya existe en la lista de productos.")
        return

    productos.append(nuevo_producto)
    print(f"Producto '{nuevo_producto}' agregado correctamente.")


def modificar_producto(productos: list, indice: int, nuevo_nombre: str) -> None:
    """Reemplaza el producto en la posición indicada por un nuevo nombre.

    Las listas en Python son mutables, por lo que podemos
    cambiar un elemento accediendo directamente a su índice.
    """
    # Validamos que el índice esté dentro del rango de la lista
    if indice < 0 or indice >= len(productos):
        print(f" Índice {indice} fuera de rango (0-{len(productos) - 1}).")
        return

    producto_anterior = productos[indice]
    productos[indice] = nuevo_nombre
    print(f"Producto '{producto_anterior}' cambiado a '{nuevo_nombre}' (posición {indice}).")


def buscar_producto(productos: list, nombre: str) -> bool:
    """Comprueba si un producto existe en la lista.

    Usa el operador 'in' de Python, que recorre internamente
    la lista para verificar la pertenencia del elemento.
    """
    encontrado = nombre in productos

    if encontrado:
        print(f"'{nombre}' SÍ se encuentra en la lista de productos.")
    else:
        print(f"'{nombre}' NO se encuentra en la lista de productos.")

    return encontrado


def imprimir_productos(productos: list) -> None:
    """Muestra por pantalla todos los productos numerados."""
    print("\n Lista de productos actualizada:")
    print("-" * 40)
    for i, producto in enumerate(productos, start=1):
        print(f"   {i}. {producto}")
    print()