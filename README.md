# Sistema de Gestión de Inventario - Coffee & Code

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-stable-brightgreen.svg)

##  Descripción

**Coffee & Code** es un sistema educativo de gestión de inventario para una cafetería, diseñado para practicar la manipulación de estructuras de datos fundamentales en Python: **listas, tuplas, diccionarios y conjuntos**.

Este proyecto simula el control de stock y productos de una cafetería, permitiendo gestionar granos de café, proveedores, precios y categorías de productos.

---

## Objetivos 

- ✅ Dominar operaciones con **listas** (agregar, modificar, buscar)
- ✅ Comprender la inmutabilidad de las **tuplas**
- ✅ Trabajar con **diccionarios** (claves-valores, consultas)
- ✅ Utilizar **conjuntos** (unión, intersección, eliminación de duplicados)
- ✅ Aplicar **buenas prácticas** de código limpio (Clean Code)
- ✅ Estructurar proyectos Python de forma profesional

---

##  Estructura del Proyecto

```
Ejercicio/
│
├── main.py                          # Orquestador principal (ejecuta los 8 pasos)
│
├── coffee_and_code/                 # Paquete principal
│   ├── __init__.py                  # Marca la carpeta como paquete Python
│   ├── datos_iniciales.py           # Datos de partida (listas, tuplas, conjuntos)
│   ├── productos.py                 # Funciones para gestionar productos (lista)
│   ├── inventario.py                # Funciones para el diccionario de inventario
│   └── categorias.py                # Funciones para conjuntos de categorías
│
├── .gitignore                       # Archivos ignorados por Git
├── README.md                        # Este archivo
└── GITFLOW_GUIDE.md                 # Guía completa de GitFlow para el proyecto
```

---

## Instalación y Uso

### Prerrequisitos
- Python 3.8 o superior

### Clonar el repositorio (si aplica)
```bash
git clone https://github.com/tu-usuario/coffee-and-code.git
cd coffee-and-code
```

### Ejecutar el programa
```bash
python main.py
```

### Salida esperada
El programa ejecutará 8 pasos que demuestran:
1. Creación y manipulación de listas
2. Modificación de elementos por índice
3. Uso de tuplas para datos estructurados
4. Diccionarios con claves-valores
5. Operaciones con conjuntos
6. Unión de conjuntos
7. Comprobaciones de pertenencia
8. Impresión final de todas las estructuras

---

## Funcionalidades

### Gestión de Productos (Listas)
- Agregar nuevos productos
- Modificar productos existentes
- Buscar productos en el catálogo
- Mostrar lista completa de productos

### Gestión de Inventario (Diccionarios + Tuplas)
- Asociar productos con datos de stock
- Consultar información detallada (cantidad, precio, nivel de reorden)
- Visualizar inventario completo en formato tabla
- Tuplas inmutables para garantizar integridad de datos

### Gestión de Categorías (Conjuntos)
- Agregar y eliminar categorías
- Operaciones de unión entre conjuntos
- Búsqueda eficiente (O(1))
- Eliminación automática de duplicados

---

## Principios Aplicados

Este proyecto sigue los principios de **Clean Code** y buenas prácticas de Python:

- 🔹 **Separación de responsabilidades**: Cada módulo tiene una función específica
- 🔹 **Datos separados de lógica**: Los datos iniciales están en un archivo independiente
- 🔹 **Funciones pequeñas**: Cada función hace una sola cosa y la hace bien
- 🔹 **Type hints**: Anotaciones de tipo para mayor claridad
- 🔹 **Validaciones**: Verificación de índices, duplicados y existencia de elementos
- 🔹 **Documentación**: Docstrings y comentarios explicativos en español
- 🔹 **Nombres descriptivos**: Variables y funciones autoexplicativas

---

## Contenido Educativo

### Conceptos Cubiertos

#### Listas
```python
productos = ["Espresso", "Latte", "Capuchino"]
productos.append("Muffin")           # Agregar
productos[2] = "Flat White"          # Modificar
"Espresso" in productos              # Buscar
```

#### Tuplas
```python
# Inmutables: representan datos fijos
inventario_espresso = (120, 1.50, 30)  # (stock, precio, reorden)
cantidad, precio, reorden = inventario_espresso  # Desempaquetado
```

#### Diccionarios
```python
inventario = {
    "Espresso": (120, 1.50, 30),
    "Latte": (80, 2.00, 20)
}
inventario["Espresso"]               # Consulta O(1)
```

#### Conjuntos
```python
categorias = {"Bebidas Calientes", "Bollería", "Granos"}
categorias.add("Snacks")             # Agregar
categorias.discard("Accesorios")     # Eliminar
cat1 | cat2                          # Unión
"Bollería" in categorias             # Búsqueda O(1)
```

---

## GitFlow

Este proyecto está diseñado para aprender y aplicar la metodología GitFlow. Consulta [GITFLOW_GUIDE.md](GITFLOW_GUIDE.md) para:

- 🔹 Entender el flujo de ramas (main, develop, feature, release, hotfix)
- 🔹 Integrar el código paso a paso
- 🔹 Crear versiones con tags semánticos
- 🔹 Aplicar buenas prácticas de control de versiones

---

##  Ejercicio Original

Este código resuelve el ejercicio **"Sistema de Gestión de Inventario - Coffee & Code"**, que incluye:

1. Crear lista de productos y agregar uno nuevo
2. Modificar el tercer producto
3. Crear tuplas de inventario
4. Asociar productos con datos usando diccionarios
5. Crear y modificar conjuntos de categorías
6. Realizar unión de conjuntos
7. Comprobaciones de pertenencia
8. Impresión final de todas las estructuras

---

##  Contribuciones para el proyecto

Este es un proyecto educativo. Si deseas contribuir:

1. Fork el repositorio
2. Crea una rama feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -m 'feat: agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

---

## Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

---

## Autor

Desarrollado Miguel Ramos como material educativo para aprender Python y estructuras de datos.

