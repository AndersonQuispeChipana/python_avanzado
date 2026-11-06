#en la siguiente funcion deberan escribir la documentacion segun la convencion para el docstring de funciones.
def area_rectangulo(b,h):
   """ calcula el area del rectangulo
   Args:
      b(int|float)= un numero entero: base el retangulo
      h=(int|float) un numero entero: haltura del rectangulo
   Restriccion:
      los argumentos no podran ser igual o mneor a 0

   Returns:
       int|float: el resultado de la operacion b*h (base*altura)

    """
   return b*h

# funcion para hallar la potencia de un numero
def potencia(n:int,p:int)->int:
    """funcion de potencia

    Args:
        n (int): numero base
        p (int): numero de potencia

    Returns:
        int: el resultado del numero base potencia
    """
    resultado:int=1
    for _ in range(p):
        resultado *-n
    return resultado