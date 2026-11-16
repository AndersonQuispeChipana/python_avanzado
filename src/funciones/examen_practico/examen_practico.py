## 1. Funciones Básicas Crea una función llamada calcular_area_rectangulo que reciba la base y la altura de un rectángulo 
# (números enteros o flotantes) y retorne su área calculada. Pruébala llamándola con dos valores distintos e imprime el resultado.

def calcular_area_rectangulo(b, h):
    area = b * h
    return area

b = float(input("Ingresa la base del rectángulo: "))
h = float(input("Ingresa la altura del rectángulo: "))
resultado = calcular_area_rectangulo(b, h)
print("El área del rectángulo es:", resultado)

## 2. Parámetros Nominales y por Defecto Crea una función llamada calcular_precio_final que calcule el precio de un producto aplicando 
# un impuesto y un descuento opcional. ● Parámetros por defecto: impuesto = 0.18 (18%) y descuento = 0.0. ● Utiliza argumentos nominales
#  en su llamada para aplicar solo un descuento del 0.05 (5%) manteniendo el impuesto por defecto.

def calcular_precio_final(precio, impuesto=0.18, descuento=0.0):
    precio_con_impuesto = precio * (1 + impuesto)
    precio_final = precio_con_impuesto * (1 - descuento)
    return precio_final

precio = float(input("Ingresa el precio del producto: "))

resultado = calcular_precio_final(precio, descuento=0.05)

print("El precio final del producto es:", resultado)


#  3. Type-hints (Anotaciones de tipo) Diseña una función llamada obtener_promedio que reciba una lista de números enteros (list[int]) 
# y retorne un número flotante (float) que represente el promedio de los valores. Incluye las anotaciones de tipo estrictas vistas en el 
# apunte. 

def obtener_promedio(numeros: list[int]) -> float:
    promedio = sum(numeros) / len(numeros)
    return promedio

numeros = []

cantidad = int(input("¿Cuántos números deseas ingresar?: "))
for i in range(cantidad):
    numero = int(input(f"Ingresa el número {i + 1}: "))
    numeros.append(numero)
resultado = obtener_promedio(numeros)
print("El promedio es:", resultado)


# 4. Empaquetado Posicional (*args) Crea una función llamada unir_frases(*args) que reciba una cantidad variable de cadenas de texto (str)
#  y las una en una sola oración separadas por un espacio, retornando el resultado final. 

def unir_frases(*args: str) -> str:
    resultado = " ".join(args)
    return resultado

frase1 = input("Ingresa la primera palabra o frase: ")
frase2 = input("Ingresa la segunda palabra o frase: ")
frase3 = input("Ingresa la tercera palabra o frase: ")
resultado = unir_frases(frase1, frase2, frase3)
print("La oración completa es:", resultado)


# 5. Empaquetado Nominal (**kwargs) Diseña una función llamada generar_perfil_usuario(**kwargs) que reciba datos arbitrarios en formato 
# clave-valor (como nombre, edad, país, profesión) y devuelva una cadena de texto descriptiva que recorra el diccionario armado e imprima
#  cada característica del usuario. 

def generar_perfil_usuario(**kwargs) -> str:
    perfil = ""

    for clave, valor in kwargs.items():
        perfil += f"{clave}: {valor}\n"

    return perfil

nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")
pais = input("Ingresa tu país: ")
profesion = input("Ingresa tu profesión: ")

resultado = generar_perfil_usuario(
    nombre=nombre,
    edad=edad,
    pais=pais,
    profesion=profesion
)
print("\nPERFIL DEL USUARIO")
print(resultado)


# 6. Funciones Anónimas (lambda) Crea una función anónima (lambda) asignada a una variable llamada es_par que reciba un número entero 
# y devuelva True si es par y False en caso contrario. Pruébala pasando un número par y uno impar.

es_par = lambda numero: numero % 2 == 0
numero = int(input("Ingresa un número entero: "))

resultado = es_par(numero)
if resultado:
    print("El número es par:", resultado)
else:
    print("El número es impar:", resultado)



#  7. Documentación (docstring) Crea una función llamada calcular_potencia(base: float, exponente: float) -> float que eleve un número a
#  su potencia. Añade un docstring completo que cumpla estrictamente con la advertencia del apunte: 1. Breve explicación. 
# 2. Especificación y tipos de los parámetros. 3. Restricciones (ej. el exponente no debe ser negativo). 
# 4. Características del valor que retorna.

def calcular_potencia(base: float, exponente: float) -> float:
    """
    Calcula la potencia de un número elevado a un exponente.

    Parámetros:
        base (float): Número que se desea elevar.
        exponente (float): Potencia a la que se elevará la base.

    Restricciones:
        El exponente no debe ser negativo.

    Retorna:
        float: El resultado de elevar la base al exponente.
    """

    if exponente < 0:
        raise ValueError("El exponente no debe ser negativo.")

    resultado = base ** exponente
    return float(resultado)

base = float(input("Ingresa la base: "))
exponente = float(input("Ingresa el exponente: "))

resultado = calcular_potencia(base, exponente)

print("El resultado de la potencia es:", resultado)


#  8. Closure (Clausura) Escribe una función externa llamada crear_validador_limite(limite_maximo: int) que retorne una función interior.
#  Esta función interior debe recibir un número y retornar True si es menor o igual al limite_maximo, o False si lo supera. Pon a prueba
#  tu closure creando un validador con límite 100.

def crear_validador_limite(limite_maximo: int):

    def validar(numero: int) -> bool:
        return numero <= limite_maximo

    return validar

limite = int(input("Ingresa el límite máximo: "))

validador = crear_validador_limite(limite)

numero = int(input("Ingresa el número que deseas validar: "))

print("¿El número está dentro del límite?:", resultado)


# 9. Programación Funcional (map()) Dada una lista de precios en dólares: precios: list[float] = [10.5, 20.0, 50.0, 5.99], utiliza la 
# función integrada map() combinada con una función lambda para incrementar todos los precios en un 10% (multiplicarlos por 1.10).
#  Recuerda envolver el resultado en list() para visualizarlo. 

precios: list[float] = [10.5, 20.0, 50.0, 5.99]
precios_incrementados = list(map(lambda precio: precio * 1.10, precios))
print("Precios originales:", precios)
print("Precios con incremento del 10%:", precios_incrementados)

# 10. Programación Funcional (filter()) Dada una lista de palabras: palabras: list[str] = ["sol", "computadora", "luz", "programacion", 
# "ia", "python"], utiliza la función integrada filter() y una función lambda para filtrar y quedarte únicamente con aquellas palabras 
# que tengan más de 4 caracteres. Muestra el resultado convertido en lista. 

# Lista de palabras
palabras: list[str] = [
    "sol", "computadora", "luz",
    "programacion", "ia", "python"
]
palabras_filtradas = list(filter(lambda palabra: len(palabra) > 4, palabras))
print("Palabras originales:", palabras)
print("Palabras con más de 4 caracteres:", palabras_filtradas)
