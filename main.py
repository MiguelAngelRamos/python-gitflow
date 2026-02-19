from coffe_and_code.datos_iniciales import (
    productos,
    datos_inventario,
    categorias_principales,
    categoria_temporada,
)
from coffe_and_code.productos import (
    agregar_producto,
    modificar_producto,
    buscar_producto,
    imprimir_productos,
)
from coffe_and_code.inventario import (
    crear_inventario,
    consultar_producto,
    imprimir_inventario,
)
from coffe_and_code.categorias import (
    agregar_categoria,
    eliminar_categoria,
    unir_categorias,
    buscar_categoria,
    imprimir_categorias,
)


def main() -> None:
    """Punto de entrada del programa. Ejecuta cada paso del ejercicio."""

    print("=" * 60)
    print("   ☕  SISTEMA DE GESTIÓN DE INVENTARIO - Coffee & Code  ☕")
    print("=" * 60)

    # ==========================================================
    # 1. CREAR LISTA DE PRODUCTOS Y AGREGAR UNO NUEVO
    # ==========================================================
    # La lista 'productos' ya viene definida en datos_iniciales.py
    # con 5 elementos: Espresso, Latte, Capuchino, Muffin, Té Verde.
    print("\n>>> PASO 1: Lista de productos base y nuevo producto")
    imprimir_productos(productos)

    # Agregamos un nuevo producto con .append() a través de nuestra función
    agregar_producto(productos, "Chocolate Caliente")

    # ==========================================================
    # 2. MODIFICAR LA LISTA DE PRODUCTOS
    # ==========================================================
    # Cambiamos el tercer producto (índice 2) de "Capuchino" a "Flat White"
    print("\n>>> PASO 2: Modificar el tercer producto")
    modificar_producto(productos, indice=2, nuevo_nombre="Flat White")

    # ==========================================================
    # 3 y 4. CREAR DICCIONARIO DE INVENTARIO CON TUPLAS
    # ==========================================================
    # Cada producto se asocia a una tupla (stock, precio, reorden).
    # Los datos base vienen de datos_iniciales.py; la función
    # crear_inventario() los combina con la lista actualizada.
    print("\n>>> PASOS 3 y 4: Diccionario de inventario con tuplas")

    inventario_detalle = crear_inventario(productos, datos_inventario)

    # Consultamos la información de un producto concreto
    consultar_producto(inventario_detalle, "Espresso")

    # ==========================================================
    # 5. USO DE CONJUNTOS – CATEGORÍAS PRINCIPALES
    # ==========================================================
    # Partimos del conjunto definido en datos_iniciales.py y
    # realizamos operaciones de adición y eliminación.
    print("\n>>> PASO 5: Conjuntos de categorías")
    imprimir_categorias(categorias_principales, "Categorías principales (original)")

    # Agregamos una categoría nueva
    agregar_categoria(categorias_principales, "Snacks Salados")

    # Eliminamos una que ya no se utiliza
    eliminar_categoria(categorias_principales, "Accesorios")

    imprimir_categorias(categorias_principales, "Categorías principales (actualizada)")

    # ==========================================================
    # 6. OPERACIÓN ENTRE CONJUNTOS – UNIÓN
    # ==========================================================
    # Unimos las categorías principales con las de temporada
    # para obtener el catálogo completo sin duplicados.
    print("\n>>> PASO 6: Unión de conjuntos")
    imprimir_categorias(categoria_temporada, "Categorías de temporada")

    catalogo_completo = unir_categorias(categorias_principales, categoria_temporada)

    # ==========================================================
    # 7. COMPROBACIONES DE PERTENENCIA
    # ==========================================================
    # Verificamos si ciertos elementos existen en nuestras
    # estructuras de datos usando el operador 'in'.
    print("\n>>> PASO 7: Comprobaciones")

    # ¿Está "Espresso" en la lista de productos?
    buscar_producto(productos, "Espresso")

    # ¿Está "Bollería" en las categorías principales?
    buscar_categoria(categorias_principales, "Bollería")

    # Probamos también con un elemento que NO existe
    buscar_producto(productos, "Mojito")
    buscar_categoria(categorias_principales, "Accesorios")

    # ==========================================================
    # 8. IMPRESIÓN FINAL DE TODAS LAS ESTRUCTURAS
    # ==========================================================
    print("\n>>> PASO 8: Impresión final de todas las estructuras")
    print("=" * 60)

    # Lista de productos actualizada
    imprimir_productos(productos)

    # Diccionario de inventario completo
    imprimir_inventario(inventario_detalle)

    # Conjunto final de categorías
    imprimir_categorias(catalogo_completo, "Catálogo completo de categorías")

    print("=" * 60)
    print("   ✅  Ejercicio completado con éxito.")
    print("=" * 60)


# --- Punto de entrada estándar de Python ---
# Esta condición asegura que main() solo se ejecute cuando
# el archivo se lance directamente, y no cuando se importe
# como módulo desde otro archivo.
if __name__ == "__main__":
    main()