"""1.-Crear una función que reciba una lista de números enterosy muestre cuál es el número
mayor y cuál es el menor."""
def listaNum(listado):
    menor = min(listado)
    mayor = max(listado)


def ejercicio1():
    limit = int(input("Ingresa un límite de valores: "))
    listNum = []
    i = 1
    while i <= limit:
        num = int(input(f"Ingresa un número entero {i} de {limit}: "))
        listNum.append(num)
        i += 1
    listaNum(listaNum)

"""2.-Crear una función que reciba una cadena de texto y cuente cuántas vocales contiene."""
def es_vocal(letra):
    vocales = "aeiuoAEIOU"
    return letra in vocales #Devuelve True si la letra está dentro de las vocales, si

def contar_vocales(texto):
    contador = 0

    for letra in texto:
        if es_vocal(letra):
            contador += 1
    print(f"La cadena contiene {contador} vocales.")

def ejercicio_contar_vocales():
    texto = input("Ingrese el texto: ")

"""3.-Crear una función que reciba una lista de nombres y muestre únicamente aquellos que
tengan más de 5 letras."""
def listaNombre(lista):
    resultado = []
    for nombre in lista: 
        if len(nombre) > 5:
            resultado.append(nombre)
            return
        
        def mostrar():
            nombres = []
            cantidad = int(input("¿Cuánto nombres quieres ingresar?"))
            for i in range(cantidad):
                nombre = input("Ingrese un nombre: ")

"""4.-Crear una función que reciba una lista de notas (números decimales), calcule el promedio
e indique si el estudiante aprueba (promedio mayor o igual a 4.0)."""
def listaNotas():

# """5.-Crear una función que reciba una lista de precios de productos y aplique un descuento del
# 10%, mostrando el valor original y el nuevo valor."""
    def listaPrecios():
        pass

# """6.-Crear una función que reciba un número entero y determine si es par o impar."""
    def numeroEntero():
        pass

# """"7.-Crear una función que reciba una lista de edades y muestre cuántas personas son mayores
# de edad (18 años o más)."""
    def listaEdades():
        pass

# """8.-Crear una función que reciba una lista de palabras y permita buscar cuántas veces aparece
# una palabra específica ingresada por el usuario."""
    def listaPalabras():
        pass

# """9.-Crear una función que reciba una lista de números y genere una nueva lista que contenga
# únicamente los números positivos."""
    def listaPositivos():
        pass


# """10.-Crear una función que reciba una lista de productos (utilizando diccionarios con nombre
# y stock) y muestre cuáles tienen un stock menor a 5 unidades."""

    def productosDiccionario(): 
        pass


def limpiar_consola():
    os.system('cls')