# Modularidad
la `modularidad` consiste en dividir un programa grande en archivos pequeños y reutilizables llamados `modulos` cada modulo es simplemente u n archivo `.py`
**ventajas:**
- `reutilizacion` escribes el coldigo una vces y lo usas en muchos programas.
- `organizacion` cada archivo tiene una responsabilidad clara.
- `matenimiento` es mas facil encontrar y corregir errores
- `trabajo en equipo` cada persona puede dasarrollar su propio modulo.

## 1. crear un  modulo
basta con crear un archivo con la extesion `.py` por ejemplop `matematicas.py`.
## 2. importar uyn modulo completo
la manera de como reutilizamos los modulos es haciendo uso de la palabra resrvada `import` esto se debe declarar en el archivo donde reutilizaremos ciertas funciones de variables de un modulo.
para importar un modulo completo usamos `import nombre_archivo`
`matematicas.py`
```python
def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
```
`main.py`
```python
import matematicas
## para hacer uso de una de las funciones tengo que acceder al archivo luego un punto y el nombre de dato, funcion que deseamos utilizar
matematicas.resta(5,8)
```