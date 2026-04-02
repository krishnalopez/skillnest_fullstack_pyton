"""
Este archivo demuestra varios conceptos básicos en Python.
Completa los comentarios en cada línea para relacionarlos
con los conceptos enumerados en 'reconocer.md'.
"""


import random #Importación de libreria para procesos aleateorios 
nombre = "Frida Kahlo" # Se declara una variable tipo string y se asigna valor ""
print(type(nombre)) #type = método  de python para mostrar el tipo de variable 
print(len(nombre)) # Devulve el largo de una variable (CUENTA EL LARGO DE LA VARIABLE)


edad = 25 #Creación de variable tipo númerico tipo(int).


if edad < 18: #Se establece una condición if 
    print("Eres menor de edad.") #Imprime un mensaje
elif edad == 18: #Se establece subcondición elif(else i¿f)
    print("Tienes 18 años.") #Imprime un mensaje
else: # Cierre de condición (Si no se cumplen condiciones anteriores)
    print("Eres mayor de edad.") #Imprime un mensaje


frutas = ["manzana", "pera", "fresa"] #Creación de array con valores ya asignados 
print(frutas[0]) #Mostramos la primera posición del arreglo
frutas[0] = "banana" # A la posición 0 del arreglo se le asigna el valor "banana"
frutas.append("uva") # Se le agrega "uva" al final del arreglo 
frutas.remove("pera") # Se remueve la palabra "pera" del arreglo 


dimensiones = (200, 50) # Creamos una variable tipo tupla (variable inmutable )
print(dimensiones[0]) # Imprime la posición 0 de la variable creada (tupla)


persona = { # Variable tipo objeto 
    "nombre": "Carlos", # Se establece un item y su respectivo valor 
    "edad": 30 # Se establece un item y su respectivo valor 
}
print(persona["nombre"]) #Imprime el valor del item(ej: "Carlos")
persona["edad"] = 31 #Se modifica el valor del item edad a 31
persona["ciudad"] = "Santiago" #Se agrega un nuevo item con un valor 
del persona["ciudad"] #Se elimina el item completo 

for i in range(5): # for range: Se crea bucle en rango 5 
    if i == 2: # Se establece condición if == 2
        continue # continue ignora el proceso y continua.
    if i == 4: # Se establece condicón if i == 4
        break # Si i = 4 se rempe el bucle entero
    print(i) # Imprime el valor de i en cada iteración(hasta 4)


contador = 0 # Se crea una variable contador tipo númerico(int)
while contador < 3: #Se crea bucle while con una condición 
    print(f"while contador es: {contador}") # Imprime el contador en un mensaje concatenado con f"" string
    contador += 1 # Incrementa el valor en 1 en cada iteración 


def saludar_usuario(nombre): # def - Palabra reservada para xcrear una función
    return f"Hola, {nombre}" # Devuelve un valor de la función.


print(saludar_usuario("Francisca")) # Se imprime "hola fransisca" - return de la función
