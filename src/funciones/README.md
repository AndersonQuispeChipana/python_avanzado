# funciones en python
las funciones nos permiten ordenar mejor el codigo y reutilizarlo cuando sea necesario
```python
# ejemplo deseamos crear un programa en python que nos permiten sumar dos numeros
numero_uno:int=45
numero_dos:int=70
numero_tres:int=78
numero_cuatro:int=20
suma:int=numero_uno+numero_dos
suma_dos:int=numero_tres+numero_cuatro
print(suma)
print(suma_dos)
```
como hacemos reutilizable el ejercicio anterior y mas lejible.
para eso utilizaremos funciones.
la carateristica de un funcion en python es la siguiente:
1. debe comenzar con la palabra reservda `def`.
2. debe tener un nombre que de a entender que realizara la funcion
3. debera tener parametros estos estaran encerrados en `()` no todas las funciones resistiran parametros aun asi debera tener los `()`
4. las funciones deberan retornar datos atraves de la palabra reservada `return`
```python
# crear un programa que me permita sumar dos numeros
def sumar(a,b):
    return a+b

print(sumar(78,56))
print(sumar(45,5))
```
## funciones avanzadas
existen tres grandes conceptos para poder entender el uso avanzado de las funciones
1. argumentos , parametros posicionales y nominales, *args y +kargs.
2. anotaciones en la salida de una funcion.
3. recursividad.

```python
# anotaciones en una funcion
def suma(a:int,b:float)->int:
    return a+b
# crear solo las anotaciones de una funcion que resiva cuatro numeros enteros y como salida que me muestre los 4 numeros enteros en una lista
def mostrar_numeros(a:int, b:int, c:int, d:int) -> list[int]:
    return[a,b,c,d]
```
**Argumentos parametros**
- **parametros** - los parametros son las variables que se declaran en la definicion de la funcion
- **argumentos** - es el dato concreto enviado en el llamado de la funcion
- **nota** en ambos casos tenemos los posicionales/nominales
```python
# parametros
def suma(a+b): # en este caso tenemos una funcion suma que recibe dos parametros a,b
suma(34,45) # en este caso estoy llamando a la funcion pasandole como argumento pasando los daatos
# en este caso en concreto podemos decir que estamos en frente a una funcion que tiene parametros posicionales eso significa qyue cada valor reemplazara en el orden que le pasemos a las variables,, 34 ->a , 45->b

def login(usuario="",password=""):
    return " acceso correcto"
login(password="12345678",usuario="tupapi")
# esta funcion es una funcion nominal porque para pasar los valores tengo que indicar la variable a la que se le va asociar el parametro de la funcion
```
```python

```
<<<<<<< HEAD
## conocemos mas sobre funciones parametros y argumentos y argumentos
sobre los parametros/argumentos nominales es ampliamente usado para distintos configuraciones ya que se puede pasar solo los argumentos que se usaran y dejar los parametros por defecto si no se va a modificar.
```python
# tenemos un programa que me permite acceder a internet que tiene parametros por defecto, sin embargo si se actualiza uno de los accesos se podra modificar el valor.
## primer caso accesso por defecto
def config(user="admin",pass="1234",port="8080",BSSID="wifi"):
    return "conectado a la red"
config()
#segundo caso l BSSID cambia por el laboratorio1
def config(user="admin",pass="1234",port="8080",BSSID="wifi"):
    return "conectado a la red"
config(BSSID="laboratorio1")
## reyner desea conectarse al wifi de ana luz, pregunta como se llama tu wifi y cual es la contraseña. respuesta le dice el wifi es a56 y su contraseña es 12345678
def config(user="admin",pass="1234",port="8080",BSSID="wifi"):
    return "conectado a la red"
config(BSSID="A56",pass="12345678")
```

### conociendo *args y **kargs (emmpaquetado y desempaquetado de argumentos pposicionales)
### desempaquetando argumentos posicionales
esta tecnica nos permite  empaquetar nuestros argumentos cuando mo sabemos la cantidad de datos que vamos a psar. imaginemos que nos piden una funcion para suma la cantidad de numeros la solucion seria empaquetar los argumentos y lluego desempaquetarlos para ello en la definicion de la funcion dentro de los parametros debemos usar el operador `*` delante del nombre del paramewtro posicional esto hara que todos los argumentos se almacenan en un tupla`()` (lista`[]`) esto nos permite rrecorrer dentro de sus elementos para poder desempaquetar y realizar las operaciones necesarias.
```python
# deseamos crear una funcion que nos permita sumar n cantidad de numeros
#n es un numero variable puede ser 3,7,8......n
def suma(*args):
    #*args =(2,5,7,8,9)
    for i in args:
        acumulado += i
    return acumulado
print(suma(2,,5,7,8,9))
```
#### desempaquetando argumentos nominales
en este caso como en elk anterior utilizaremos el operador `*` la casuistica es el mismo sain embargo para de4sempaquetar argumento nominalñes usaremos `**` delante del nombre del parametro nominal, diferencia del anterio esto se empaqueta en un diccionario (`{clave:valor}`)
```python
# debemos crear una funcion que me permita saber encontrar la persona con mayor calificacion.
def mejor_alumno(**kwargs):
    # **kwargs={clave:valor}
    nota_maxima
    for alumno,nota in kwargs.items():
        if nota > nota_maxima:
            nota_maxima = nota
            mejor_alumno = alumno
        return mejor_alumno
mejor_alumno(noemi=20,eduardo=18,david=19)
```
=======



## funciones anonimas
las funciones anonimas en python son llamadas `lamba`,estas funciones tiene las siguientes propiedades:
1. se escribe en una unica sentencia`(linea)`
2. no tiene nombre`(anonima)`
3. su cuerpo conlleva un `return` implicito.
4. puede recibir cualquier numero de parametros.

la estructura para definir una funcion landa `lambda` es la siguiente:
1. escribir la palabra reservada `lambda` 
2. especificar la cantidad de parametros.
3. indicar los datos de retorno
```python
lambda a,b: a+b
```
> [!TIP] puesto que esta funcion es anonima para ejecutarla debemos almacenar la funcion en una variable
 ```python
suma=lambda a,b: a+b
suma(3,6)
```
## Documemntacion
python nos permite documentar una funcion con el objetivo de explicar mejor determinadas zonas de nuestro codigo, para esto uzamos una cadena de texto despues de la difinicion de una funcion, a esta cadena de texrto se le conoce como `docstring` y esta delimitado por triples comillas `"""aqui el texto"""`
```python
def suma(a,b):
    """
    funcion para realizar la suma de dos numeros
    """
# los docstring tambien nos permite explixcvar los parametros que recibe los datos de salida
def resta(a,b):
    """
    a= un numero entero.
    b= un numero entero.
    en ambos casos a,b deben recibir valores menores 0.
    retronara un dato entero <int> positivo
    """
    return a-b
```
> [!WARNING] en el proceso de documentacion tener en cuenta de incluir a lop menos lo siguiente: 
>1. breve explicacion sobre que hace la funcion  
>2. especificaciones y caracteristicas de los parametros incluyendo sus tipos . 
>3. restricciones de la funcion.  
>4. el valor que retorna y sus caracteristicas

## type-hints (anotaciones de tipo)
nos permite indicar que tipo de datos recibiran una variable, parametro y el valor de retorno de una funcion.
para utilizarlos debemos indicar el tipo de dato despues del separador`:`, en el caso del valor de retorno usaremos `->` luego el tipo de dato y finalmente el separador`:` que indica el inicio del bloque de codigo de la funcion.
las `anotacines tipo` son una herramienta que nos perite complementar la documentacion de nuestro codigo
**tenemos los siguientes**
- **simple**
- int -> numeros enteros
- float -> decimales
- bool -> datos boleanos (verdad o falso)
- str -> datos de tipo texto o cadena
- list -> listas `[]`
- tuple -> tuplas `()`
- dict -> diccionarios `{}`
-**compouestos**
existen casos en os que necesitamos mas exprecividad en la *anotacion de tipos*  ¿que ocurre si queremos indicar una *lista de cadenas* o un *conjunto de enteros*.?
- list[str] -> lista de cadenas de texto
- list[int] -> lista de numeros enteros
-dict[str,float] -> diccionario domnde las claves son cadenas de texto y los valores son flotantes/decimales
-**multiples**
 en el caso que queramoa indicar que un determinado parmetro puede ser de un `tipo o de otro` tenemos que espicificarlo usando el operador `|`
 - tuple|dict -> puede ser datos de tipo tupla o diccionario
 - list[srt|int] -> lista cuuyos elementos pueden ser cadenas de texto o enteros
 - dict[srt|int,float|int] -> diccionario
 
 closure
una closure o clausura son funciones que establececn una funcion interioi, o retornan una funcion estas funciones se caracterizan por recrear el valor de los argumentos que se le pasa.
```python
def multiplicando(n):
    def multiplicador(m):
        return n*m
    return multiplicador
```
## programacion funcional

Python usa tres map(), filter(), reduce(), pero nosotros solo usaremos map() y filter().

Estas funciones integradas de python sirven para procesar y transformar colecciones de datos(listas,diccionarios) de manera muy eficiente:

> [!tip] Importante:
> Las funciones map() y filter() reciben dos parámetros primero la funcion a ejecutar y segundo el iterable en que va actuar. La funcion que recibe como parametro puede ser normal (def) o puede ser anonima(lambda).

### 1. map()
map aplica una funcion especifica a cada un de los elementos de una coleccion(iterable) y devuelve un nuevo iterable con los resultados.
```python
# de una lista de numeros deseamos calcular la potencia de 2 de cada numero
numero:list[int]=[2,4,6,7]
def f(x):
    return x**2
## una ves creada pasamos la funcion como parametro
map(f,numeros)
## cuando deseamo trabajar ccon funciones anonimas usamos lambda dentro del parametro
map(lambda x:x**2,numeros)
```
### 2. filter()
filter pasa cada elemento de una coleccion por una funcion y solo se queda con aquellos elementos donde la funcion devuleva true(es decir filtra los datos segun una condicion)
```python
# imagina que tienes  una lista de numeros y solo quieres quedarte con los numeros pares.
numeros:list[int]=[2,7,8,20,4,3,912,11,16,17]
filter(lamb n:n %2==0,numeros)
```
> [!WARNING] Nta importante
> tanto `map()` como `filter` no devuelven listas directamente,sino iteradores. esto es para ahorrar memoria(evaluacion perezoza p lazy evaluation). si quieres ver el resultado como una lista tradicional, siempre debes envolveren `list()`.