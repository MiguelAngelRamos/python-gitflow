def agregar_categoria(categorias: set, nueva: str) -> None:
    """Agrega una nueva categoría al conjunto.

    El método .add() solo añade si el elemento no existe,
    ya que los conjuntos no admiten duplicados.
    """
    if nueva in categorias:
        print(f"La categoría '{nueva}' ya existe en el conjunto.")
        return

    categorias.add(nueva)
    print(f"Categoría '{nueva}' agregada correctamente.")


def eliminar_categoria(categorias: set, nombre: str) -> None:
    """Elimina una categoría del conjunto.

    Usamos .discard() en lugar de .remove() porque
    .discard() NO lanza error si el elemento no existe,
    lo que hace el código más robusto.
    """
    if nombre not in categorias:
        print(f"La categoría '{nombre}' no existe en el conjunto.")
        return

    categorias.discard(nombre)
    print(f" Categoría '{nombre}' eliminada correctamente.")


def unir_categorias(principales: set, temporada: set) -> set:
    """Realiza la unión de dos conjuntos de categorías.

    La unión (|) combina todos los elementos de ambos conjuntos
    sin repetir ninguno. Es equivalente a principales.union(temporada).
    """
    catalogo_completo = principales | temporada

    print("\n Unión de categorías (catálogo completo):")
    print("-" * 40)
    for categoria in sorted(catalogo_completo):
        print(f"   • {categoria}")
    print()

    return catalogo_completo


def buscar_categoria(categorias: set, nombre: str) -> bool:
    """Verifica si una categoría existe en el conjunto.

    La búsqueda en conjuntos es muy eficiente (O(1) en promedio)
    gracias a su implementación interna con tablas hash.
    """
    encontrada = nombre in categorias

    if encontrada:
        print(f"'{nombre}' SÍ está en las categorías principales.")
    else:
        print(f" '{nombre}' NO está en las categorías principales.")

    return encontrada


def imprimir_categorias(categorias: set, titulo: str = "Categorías") -> None:
    """Muestra todas las categorías del conjunto ordenadas alfabéticamente."""
    print(f"\n  {titulo}:")
    print("-" * 40)
    for categoria in sorted(categorias):
        print(f"   • {categoria}")
    print()