# Gestor de Inventario Orientado a Objetos

## 1. Descripción del proyecto

El Gestor de Inventario es una aplicación de consola desarrollada en Python que permite administrar productos mediante programación orientada a objetos.

El proyecto transforma la forma de almacenar productos, pasando de utilizar diccionarios dentro de una lista a representar cada producto como una instancia de la clase `Producto`. La clase `Inventario` se encarga de administrar la colección de productos y realizar las operaciones correspondientes.

La aplicación está organizada en módulos para separar las responsabilidades y facilitar el mantenimiento del código.

## 2. Objetivo general

Desarrollar una aplicación de consola para gestionar un inventario de productos utilizando clases, objetos, métodos de instancia, encapsulamiento, propiedades, validaciones, funciones e importaciones entre módulos de Python.

## 3. Objetivos específicos

- Crear productos mediante la clase `Producto`.
- Administrar los productos mediante la clase `Inventario`.
- Registrar, listar, buscar, actualizar y eliminar productos.
- Validar los datos para evitar registros incorrectos.
- Generar informes relacionados con el inventario.
- Manejar entradas numéricas inválidas.
- Separar la lógica del programa de la interacción con el usuario.
- Aplicar principios básicos de programación orientada a objetos.

## 4. Tecnologías utilizadas

- **Lenguaje:** Python 3.
- **Paradigma:** programación orientada a objetos.
- **Interfaz:** consola.
- **Dependencias externas:** no requiere instalar librerías adicionales.

## 5. Estructura del proyecto

```text
gestor_inventario/
├── main.py
├── producto.py
├── inventario.py
└── README.md
```

### Descripción de los archivos

**`producto.py`**

Contiene la clase `Producto`, responsable de representar cada artículo, administrar sus atributos, validar sus datos individuales y calcular el valor de sus existencias.

**`inventario.py`**

Contiene la clase `Inventario`, responsable de conservar y administrar la colección de productos. Incluye las operaciones de registro, consulta, búsqueda, actualización, eliminación y generación de informes, según los requisitos de la aplicación.

**`main.py`**

Es el punto de entrada del programa. Contiene las funciones de interacción con el usuario, el menú, la lectura de datos y la presentación de resultados.

**`README.md`**

Documenta el propósito, la estructura, la ejecución y las pruebas del proyecto.

## 6. Funcionalidades del sistema

## Funcionalidades implementadas

- Registro de productos con código, nombre, categoría, precio y cantidad.
- Validación de los datos iniciales mediante la clase Producto.
- Rechazo de códigos duplicados.
- Listado y búsqueda de productos.
- Actualización de existencias, aceptando cero y rechazando cantidades negativas.
- Eliminación de productos por código.
- Consulta de productos sin stock mediante una comprensión de lista.
- Resumen del inventario con productos diferentes, unidades disponibles, valor total y categorías utilizadas.
- Manejo de entradas numéricas incorrectas.
- Menú interactivo que se mantiene hasta seleccionar la opción de salida.

## 7. Principios de diseño

### Programación orientada a objetos

Cada producto se representa mediante un objeto de la clase `Producto`. La clase `Inventario` administra los objetos creados y centraliza las operaciones sobre la colección.

### Encapsulamiento

Los atributos internos se identifican mediante la convención de nombres que comienza con un guion bajo, por ejemplo, `_productos`. Las propiedades y los métodos permiten controlar el acceso y las modificaciones de los datos.

### Separación de responsabilidades

Cada módulo cumple una función específica:

- `producto.py`: datos y reglas individuales del producto.
- `inventario.py`: administración de la colección y operaciones del inventario.
- `main.py`: interacción con el usuario y presentación de resultados.

Las clases `Producto` e `Inventario` no solicitan entradas mediante `input()` ni presentan el menú. Estas tareas corresponden al módulo principal.

### Validación de datos

El sistema debe comprobar que los datos cumplan las reglas definidas antes de registrar o modificar un producto. También debe manejar las entradas numéricas que no puedan convertirse al tipo esperado.

## 8. Requisitos para ejecutar el proyecto

- Tener Python 3 instalado.
- Disponer de una terminal o consola.
- Contar con los archivos del proyecto dentro de la misma carpeta.

No se requieren instalaciones adicionales de paquetes externos.

## 9. Instrucciones de ejecución

1. Abrir PowerShell o una terminal.
2. Ubicarse en la carpeta del proyecto. Por ejemplo:

   ```powershell
   cd C:\Users\PC\Desktop\python-laboratorio-03\gestor_inventario
   ```

   Si el proyecto está guardado en otra ubicación, reemplazar la ruta por la correspondiente.

3. Ejecutar el programa principal:

   ```powershell
   python main.py
   ```

4. Seguir las opciones y las instrucciones que presente el programa en la consola.

## 10. Pruebas del sistema

Para comprobar el funcionamiento del gestor de inventario, se deben realizar pruebas como las siguientes:

- Registrar dos productos con códigos diferentes.
- Intentar registrar un producto con un código que ya existe.
- Consultar la lista de productos.
- Buscar un producto existente.
- Buscar un código que no esté registrado.
- Actualizar un producto con datos válidos.
- Intentar actualizar un producto con datos inválidos.
- Eliminar un producto existente.
- Intentar eliminar un producto inexistente.
- Comprobar los cálculos de valor de existencias y los informes.
- Introducir texto cuando se solicite un número y comprobar que el programa gestione el error.

Los resultados de las pruebas deben registrarse después de ejecutar y verificar el comportamiento real de la aplicación.

