#crear una funcion que reciba 5 numeros eneteros y que retornen solo una lista de numeros pares, tener en cuenta las anotaciones
def numeros_pares(a:int, b:int, c: int, d: int, e: int) -> list[int]:
    numeros:list[int]=[a,b,c,d,e]
    numeros_pares:list[int]=[]
    for i in numeros:
        if i%2==0:
            numeros_pares.append(i)
    return numeros_pares
print(numeros_pares(4,2,6,8,5))

def suma(a:int,b:int)->int:
    return a+b
print(suma(34))

def login(usuario="",password=""):
    return " bienbenido al sistema"
print(login(passw="1111",user="hol"))