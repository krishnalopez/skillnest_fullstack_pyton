# Crear una función que reciba una lista de números enteros 
# y genere una nueva lista solo con los números pares mayores a 10.
#  Luego debe mostrar la nueva lista y la cantidad de elementos encontrados

def numerosEnteros(lista):
    nueva_lista = []
    cantidad = 0
    for num in range(len(lista)):
        if lista[num] > 10 and lista[num] % 2 == 0:
            nueva_lista.append(lista[num])
            cantidad += 1
    return nueva_lista

def ejercicio1():
    numeros = []
    krishna = int(input("Ingrese un limite: "))
    for i in range(krishna):
        anne = int(input("Ingrese un numero: "))
        if anne != "":
            numeros.append(anne)
    resultado = numerosEnteros(numeros)
    print(f"Los numeros pares mayores a diez son {resultado} y son {len(resultado)}")

ejercicio1()






opcion = int(input("Ingrese una opción: "))
    if opcion == 1: 
        print("Opción 1") 
    elif opcion == 2: 
        print("Opción 2")