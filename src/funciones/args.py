# ejercicio usando la tecnica *args crear una funcion quje me permita identificar numeros pares de n cantidad de 
#numeros la funcion debera retornar una lista con los numeros partes identificados
def numeros_pares(*args):
    pares = []

    for numero in args:
        if numero % 2 == 0:
            pares.append(numero)

    return pares


# Llamada a la función
resultado = numeros_pares(1, 2, 3, 4, 5, 6, 7, 8, 10, 12)

print("Los números pares son:", resultado)