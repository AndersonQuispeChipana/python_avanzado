# crear una funcion que me permita ingresar nombre y apellido y me retorne unmensaje con ambos datos
def creador(nombre:str):
    def apellido(ap:str):
        return f"tu nombre es: {nombre} y tu  es apellido es {ap}"
    return apellido

alumno1=creador("david") # def apellido(ap): return
alumno2=creador("noemi")
print(alumno1("goliat"))
print (alumno2("maikel"))

# usando closure crear una funcion multiplicador que reciba por parametro el factor que devulva una funcion que 
# permita multiplicar cualquier numero por el factor
def multiplicador(factor):
    def multiplicar(numero):
        return numero * factor

    return multiplicar

multiplicar_por_2 = multiplicador(2)
multiplicar_por_5 = multiplicador(5)

print(multiplicar_por_2(10))  
   
print(multiplicar_por_5(10)) 
