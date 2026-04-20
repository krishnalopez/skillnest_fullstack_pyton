"""
En este archivo pondrás en práctica el uso de bucles 'for' en Python,
usando ejemplos inspirados en videojuegos y situaciones atractivas.
"""

# 1. Generador de niveles
# Imprime todos los niveles del 0 al 100 (incluyendo el 100).
# (Tu código aquí)
def generadorNiveles():
    print("Niveles del 0 al 100")
    for i in range(0, 101):
        print(f"nivel actual es {i}")
# 2. Potenciadores de energía (Múltiplos de 2)
# Imprime los números múltiplos de 2 desde 2 hasta 500 (incluyendo el 500).
# (Tu código aquí)
def potenciadorEnergia():
    print("Númreos múltiplos de 2 desde 2 hasta 500 ")
    for i in range(2, 501):
        if i % 2 == 0:
            print(f"Potenciador en la casilla {i}")
# 3. Trampa de emojis
# Recorre los puntos del 1 al 100.
# - Si el número es divisible por 5, imprime ""
# - Si es divisible por 10, imprime ""
# ¡Cuidado con la prioridad en tus condicionales!
# (Tu código aquí)
def trampaEmojis():
    print("Recorre los puntos del 1 al 100. ")
    for i in range(1, 101):
        if i % 10 == 0:
            print(f"Hay un 💎 en el punto {i}")
        elif i % 5 == 0:
            print(f"Hay un 🌵 en el punto {i}")
# 4. Suma colosal
# Suma todos los números pares del 0 al 500,000 e imprime la suma total.
# (Tu código aquí) 
def sumaColosal():
    print("Imprime la suma total del 0 al 500,000 pares")
    suma = 0
    for i in range(0, 500001):
        if i % 2 == 0:
            suma +=  i
    print(f"La suma al final es de {suma}")
# 5. Retroceso temporal
# Desde 2024, retrocede de 3 en 3 hasta 0 o menos.
# Imprime cada valor en la cuenta regresiva.
# (Tu código aquí)
def retrocesoTemporal():
    print("Imprime cada valor en la cuenta regresiva")
    anioPresente = 2024
    while anioPresente > 0:
        anioPresente -= 3
        print(f"Año presente es {anioPresente}")
# 6. Contador dinámico
# Declara las variables inicio, fin, y salto (por ejemplo: inicio=3, fin=10, salto=2).
# Imprime los números en el rango que sean múltiplos de 'salto'.
# (Tu código aquí)
def contadorDinamico():
    print("Imprime los números en el rango que sean múltiplos de salto")
    inicio = int(input("Ingresa un número inicial: "))
    fin = int(input("Ingresa un número final: "))
    salto = int(input("Ingresa un número de salto: "))
    print("Calculando")
    for i in range(inicio, fin + 1):
        if i % salto == 0:
            print(f"Número: {i}")
# Ejemplo: si inicio = 3, fin = 10, y salto = 2
# Se imprimiría: 4, 6, 8, 10

#Menu de navegación para ejercicios
continuar = True
while continuar:
    print("\n---Ejercicios core---")
    print("---Ejercicio 1---")
    print("---Ejercicio 2---")
    print("---Ejercicio 3---")
    print("---Ejercicio 4---")
    print("---Ejercicio 5---")
    print("---Ejercicio 6---")
    opcion = input("\n---- Elige una opción: (1-6) (0 para salir) =")
    if opcion == "1":
        print("\nEjecutando ejercicio 1: ")
        generadorNiveles()
    elif opcion == "2":
        print("\nEjecutando ejercicio 2: ")
        potenciadorEnergia()
    elif opcion == "3":
        print("\nEjecutando ejercicio 3: ")
        trampaEmojis()
    elif opcion == "4":
        print("\nEjecutando ejercicio 4: ")
        sumaColosal()
    elif opcion == "5":
        print("\nEjecutando ejercicio 5: ")
        retrocesoTemporal()
    elif opcion == "6":
        print("\nEjecutando ejercicio 6: ")
        contadorDinamico()
    elif opcion == "0":
        break