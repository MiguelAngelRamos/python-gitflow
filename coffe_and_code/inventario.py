
def crear_inventario(productos: list, datos: dict) -> dict:
    """Construye el diccionario de inventario a partir de los productos
    y los datos iniciales.

    Si un producto no tiene datos previos, se le asigna
    una tupla por defecto (0, 0.0, 0) indicando que aún
    no se ha configurado.
    """
    inventario = {}

    for producto in productos:
        # .get() devuelve un valor por defecto si la clave no existe
        inventario[producto] = datos.get(producto, (0, 0.0, 0))
    

    return inventario


def consultar_producto(inventario: dict, nombre: str) -> None:
    """Imprime la información detallada de un producto del inventario.

    Desestructuramos la tupla en sus tres componentes para
    mostrar cada dato de forma clara y legible.
    """
    """
        inventario = {
            "Espresso": (120, 1.50, 30),
            "Latte": (80, 2.50, 20),
            "Cappuccino": (60, 3.00, 15),
            "Muffin": (50, 2.00, 25),
            "Té Verde": (100, 1.00, 40)
        }
    """
    if nombre not in inventario:
        print(f" '{nombre}' no existe en el inventario.")
        return

    # Desempaquetado de tupla: asignamos cada valor a una variable descriptiva
    cantidad, precio, reorden = inventario[nombre]

    print(f"\n Información de '{nombre}':")
    print(f"   - Cantidad en stock : {cantidad} unidades")
    print(f"   - Precio unitario   : {precio:.2f} €")
    print(f"   - Nivel de reorden  : {reorden} unidades")
    print()


def imprimir_inventario(inventario: dict) -> None:
    """Muestra el inventario completo en formato tabla."""
    print("\n Inventario completo:")
    print("-" * 60)
    print(f"   {'Producto':<15} {'Stock':>6} {'Precio':>8} {'Reorden':>8}")
    print("-" * 60)
    
    """
        inventario = {
            "Espresso": (120, 1.50, 30),
            "Latte": (80, 2.50, 20),
            "Cappuccino": (60, 3.00, 15),
            "Muffin": (50, 2.00, 25),
            "Té Verde": (100, 1.00, 40)
        }
    """
    [("Espresso", (120, 1.50, 30)), ("Latte", (80, 2.50, 20)), ("Cappuccino", (60, 3.00, 15)), ("Muffin", (50, 2.00, 25)), ("Té Verde", (100, 1.00, 40))]
    
    for producto, (cantidad, precio, reorden) in inventario.items():
        print(f"   {producto:<15} {cantidad:>6} {precio:>7.2f}€ {reorden:>8}")

    print()