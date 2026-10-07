# crear un programa que me permita mostrar mensajes personalizados, crear una funcion similar a la funcion print de python
def mi_print(mensaje:str):
    texto=f"""
    ---------------------------------------------------
    {mensaje}
    ---------------------------------------------------
    """
    print(texto)

mi_print("hola como estas es un nuevo mensaje")