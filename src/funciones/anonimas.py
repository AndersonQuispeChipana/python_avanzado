# haciendo uso de lambda crear una funcion que me  muestre un mensaje personalizado

mensaje = lambda nombre:print( f"¡Hola, {nombre}! Bienvenido al programa.")
mensaje("jajaja")

# crear una funcion para calcular el area de un rectangulo siendo la formula la siguiente area=b*h
area= lambda b,h:b*h
b = float(input("Ingrese la base del rectangulo: "))
h = float(input("Ingrese la altura del rectangulo: "))
print("el area del rectángulo es:", area(b, h))

# crear una funcion que verifique si un numero es par o impar

verificar = lambda numero: "Es par" if numero % 2 == 0 else "Es impar"
numero = int(input("Ingrese un número: "))
print("El número", numero, verificar(numero))