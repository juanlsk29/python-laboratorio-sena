# Python – Laboratorio 01

Primer laboratorio de Python del programa de formación del SENA.

| Dato | Valor |
|------|-------|
| **Aprendiz** | Juan Manuel Quintero Murcia |
| **Ficha** | 3388087 |
| **Laboratorio** | Python-laboratorio01 |
| **Repositorio** | https://github.com/juanlsk29/python-laboratorio-sena.git |

## Descripción del proyecto

Este repositorio reúne los programas desarrollados durante el primer laboratorio de Python. El objetivo fue practicar los fundamentos del lenguaje: salida por consola, variables y tipos de datos, entrada de datos con `input()`, conversión de tipos, operadores aritméticos, depuración de errores y construcción de un **cotizador de compras** que integra todo lo anterior.

Las pruebas realizadas, los resultados esperados y las respuestas a las preguntas de cada actividad se encuentran documentados como **comentarios dentro de cada archivo `.py`**.

## Contenido

### Primeros pasos
| Archivo | Descripción |
|---------|-------------|
| `hola_python.py` | Primer programa: imprime un encabezado y datos del aprendiz. |
| `presentacion.py` | Presentación personal y respuestas conceptuales sobre Python (extensión, comando, salida y errores). |
| `saludo.py` | Pide el nombre con `input()` y saluda. |

### Variables y tipos de datos
| Archivo | Descripción |
|---------|-------------|
| `datos_basicos.py` | Variables `str`, `int`, `float` y `bool`; uso de `type()` y f-strings. |
| `perfil_aprendiz.py` | Perfil del aprendiz y reasignación de variables (cambio de valor y de tipo). |
| `inventario.py` | Variables de un producto de inventario con f-strings. |
| `error_variables.py` | Ficha de producto con constante `IMPUESTO` y verificación de tipos. |
| `tipo_entrada.py` | `input()` devuelve texto; conversión con `int()` y `float()`. |
| `datos_usuario.py` | Captura de nombre, ciudad, edad y estatura. |

### Operadores y cálculos
| Archivo | Descripción |
|---------|-------------|
| `operadores.py` | Operadores `+ - * / // % **` y cálculo de horas/minutos. |
| `suma_interactiva.py` | Operaciones aritméticas entre dos números ingresados por el usuario. |
| `conversion_tiempo.py` | Minutos a horas y minutos con `//` y `%`; precedencia de operadores. |
| `conversion_unidades.py` | Kilómetros a metros, centímetros y millas. |
| `conversor_temperatura.py` | Grados Celsius a Fahrenheit. |
| `calculo_promedio.py` | Promedio de tres notas. |
| `calculo_compra.py` | Subtotal, descuento y total de una compra. |
| `calculo_salario.py` | Pago total y aporte de un trabajador; descuento sobre unidades. |
| `salario_interactivo.py` | Cálculo de pago con datos ingresados por el usuario. |
| `factura_simple.py` | Factura con descuento e impuesto. |

### Depuración e integración
| Archivo | Descripción |
|---------|-------------|
| `programa_incompleto.py` | Programa de compra completado con entrada de datos. |
| `retodepuracion.py` | Reto de depuración: error de sintaxis, variable inexistente y error lógico, con su corrección. |
| `cotizador_compra.py` | **Programa integrador**: cotización con vendedor, cliente, producto, descuento, impuesto y envío. |

## Requisitos

- [Python 3.8 o superior](https://www.python.org/downloads/) (se probó con Python 3).
- Una terminal (PowerShell, CMD, Terminal de macOS/Linux o la terminal integrada de VS Code).
- [Git](https://git-scm.com/) para clonar el repositorio.

No se necesitan librerías externas: todo usa la biblioteca estándar de Python.

## Instrucciones de ejecución

1. **Clonar el repositorio**

   ```bash
   git clone https://github.com/juanlsk29/python-laboratorio-sena.git
   cd python-laboratorio-sena
   ```

2. **Verificar la instalación de Python**

   ```bash
   python --version
   ```

   En macOS/Linux puede ser necesario usar `python3`.

3. **Ejecutar un programa**

   ```bash
   python nombre_del_archivo.py
   ```

   Ejemplo:

   ```bash
   python hola_python.py
   ```

4. **Programas interactivos**: los que usan `input()` (por ejemplo `saludo.py`, `suma_interactiva.py` o `cotizador_compra.py`) se detienen a esperar datos. Escribe el valor y presiona **Enter**. Los campos numéricos deben ingresarse como números (por ejemplo `50000` o `12.5`), de lo contrario Python mostrará un `ValueError`.

### Ejemplo: cotizador de compra

```bash
python cotizador_compra.py
```

```
Código de cotización: COT-001
Nombre del vendedor: Juan
Nombre del cliente: Ana
Producto: Teclado
Precio unitario: 85000
Cantidad: 3
Descuento (%): 10
Impuesto (%): 19
Costo de envío: 15000
```

El programa muestra el resumen con subtotal, descuento, base, impuesto, costo de envío y **TOTAL**.

## Estructura del repositorio

```
python-laboratorio-sena/
├── README.md
├── hola_python.py
├── presentacion.py
├── saludo.py
├── datos_basicos.py
├── perfil_aprendiz.py
├── inventario.py
├── error_variables.py
├── tipo_entrada.py
├── datos_usuario.py
├── operadores.py
├── suma_interactiva.py
├── conversion_tiempo.py
├── conversion_unidades.py
├── conversor_temperatura.py
├── calculo_promedio.py
├── calculo_compra.py
├── calculo_salario.py
├── salario_interactivo.py
├── factura_simple.py
├── programa_incompleto.py
├── retodepuracion.py
└── cotizador_compra.py
```

## Autor

**Juan Manuel Quintero Murcia** – Ficha 3388087 – SENA
