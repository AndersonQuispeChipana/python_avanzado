# Recursividad en Python
## Definición

La recursividad en Python es una técnica de programación en la que una función se llama a sí misma para resolver un problema, dividiéndolo en problemas más pequeños hasta cumplir una condición de parada.

La recursividad tiene dos elementos principales:

Caso base: condición que detiene las llamadas recursivas.
Caso recursivo: parte de la función que se llama a sí misma.
Ejemplos en código
1. Contar hacia atrás
```python


def contar(n):
    if n == 0:
        print("Fin")
    else:
        print(n)
        contar(n - 1)

contar(5)


Salida:

5
4
3
2
1
Fin

2. Calcular el factorial de un número

El factorial de un número es el producto de todos los números enteros positivos desde ese número hasta 1.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))


Salida:

120

3. Sumar números del 1 hasta n
def suma(n):
    if n == 0:
        return 0
    else:
        return n + suma(n - 1)

print(suma(5))


Salida:

15

4. Calcular la potencia de un número

Este ejemplo calcula la potencia de una base elevada a un exponente entero no negativo.

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

print(potencia(2, 4))


Salida:

16

5. Mostrar números en orden ascendente
def ascendente(n):
    if n == 0:
```