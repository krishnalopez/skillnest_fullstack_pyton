# 1. Números Pares Dinámicos
# Desarrolla un programa que solicite al usuario cuántos números pares desea ver ($n$).
# El programa debe imprimir los primeros $n$ números pares positivos.
def numerosDinamicos():
    n = int(input("¿Cuántos números pares desea ver?"))#pedir un número al usuario
    pares = []
    for i in range (1, (n * 2) + 1):
        if i % 2 == 0:
            pares.append(i)
    print(f"Mostrando pares: {pares}")
# 2. Verificador de Edad y Acceso
# Pide al usuario su año de nacimiento. Calcula su edad y muestra si es mayor de edad (18+).
# Si tiene menos de 18, indica cuántos años le faltan para la mayoría de edad.
def verificador_edad():
    campo = input("Ingrese su año de nacimiento: ")
    edad = 2026 - int(campo)
    if campo == "":
        print("Error")
    elif edad >= 18:
        print(f"Tienes acceso ya que tu edad es: {edad}")
    elif edad > 0 and edad < 18:
        print(f"No tines acceso: te falta {18 - edad} años.")
    else:
        print("Ingresa valores válidos")

# 3. Calculadora de Descuentos
# Solicita el precio de un producto y la cantidad comprada.
# Si el total supera los $100, aplica un 15% de descuento. 
# Muestra el subtotal, el descuento aplicado y el total final.
def aplicarDescuento():
    precio = float(input("Ingresa el precio del producto: "))
    cantidad = int(input("Ingresar cantidad: "))
    producto = precio * cantidad
    if producto >= 100: 
        descuento = producto * 0.15
    else:
        descuento = 0
    total = producto - descuento
    print(f"El subtotal es: {producto}. El descuento aplicado es: {descuento}. Y el total del producto ahoar es: {total} ")
# 4. Clasificador de Números
# Pide un número al usuario e indica si es: Positivo-Par, Positivo-Impar, Negativo-Par, Negativo-Impar o Cero.
def  clasificadorNum():
    num = int(input("Ingrese un número"))
    if num > 0 :
        if num % 2 == 0:
            print("Positivo - Par")
        elif num % 2 == 1:
            print("Postivo - Impar")
    elif num < 0:
        if num % 2 == 0:
            print("Negativo-Par")
        elif num % 2 == 1:
            print("Negativo-Impar")
    else:
        print("Es 0")
# 5. Tabla de Multiplicar Personalizada
# Solicita un número entero y muestra su tabla de multiplicar del 1 al 12,
# pero solo muestra los resultados que sean múltiplos de 3.
def tablaMultiplicar():
    num= int(input("Ingresar numero a trabajar: "))
    for i in range (1, 13):
        resultado = num * i
        if resultado % 3 == 0:
            print(f"Del {num} números son divisibles por 3 : {resultado}")

# 6. Sumatoria con Centinela
# Crea un programa que pida números continuamente y los sume. 
# El ciclo debe terminar cuando el usuario ingrese un número negativo.
# Al final, muestra la suma total (sin incluir el negativo).
def sumatoriaCentinela():
    suma_total = 0
    while True:
        n = float(input("Ingresa un número(negativo para salir):"))
        if n < 0:
            break
        suma_total += n
    print(f"La suma total es: {suma_total}")
#Ejercicio 7: Contador de Vocales
'''Pide al usuario una frase o palabra. Utiliza un bucle para recorrer
la cadena y contar cuántas vocales tiene en total.'''
def contadorVocales():
    texto = input("Ingresa una frase o palabra: ").lower()
    vocales = 0
    for i in range(len(texto)):
        #Detectar vocales
        if texto[i] == "a" or texto[i] == "e" or texto[i] == "i" or texto[i] == "o" or texto[i] == "u":
            vocales += 1
        #Detectar vocales sin tilde
        elif texto[i] == "á" or texto[i] == "é" or texto[i] == "í" or texto[i] == "ó" or texto[i] == "ú":
            vocales += 1
    print(f"Hay {vocales} vocales en total en el string '{texto}'")

#Ejercicio 8: Validación de Contraseña
'''Define una contraseña en una variable. Pide al usuario que la intente adivinar.
Tienes un máximo de 3 intentos; si falla los 3, bloquea el acceso.'''
def validarContrasena():
    acceso = False
    contrasena = "hola123"
    for i in range(3):
        contrasenaInput = input("Ingresa la contraseña: ")
        if contrasenaInput == contrasena:
            acceso = True
            break
        else:
            print("Contraseña incorrecta.")
    if acceso == True:
        print("Acceso permitido.")
    else:
        print("Acceso bloqueado.")

#Ejercicio 9: Registro de Nombres
'''Crea un arreglo vacío. Pide al usuario que ingrese 5 nombres. Guárdalos en el arreglo y,
al final, imprímelos en orden inverso al que fueron ingresados.'''
def registroNombres():
    registro = []
    for i in range(5):
        nombre = input("Ingresa un nombre: ")
        registro.append(nombre)
    registro.reverse()
    for i in range(len(registro)):
        print(registro[i])

#Ejercicio 10: Promedio de Notas
'''Solicita al usuario cuántas notas desea ingresar. Almacena cada nota en un arreglo.
Al finalizar, calcula y muestra el promedio, la nota más alta y la más baja.'''
def promedioNotas():
    notasLimit = int(input("Ingresa la cantidad límite de notas: "))
    notas = []
    valido = True
    for i in range(notasLimit):
        nota = float(input("Ingresa una nota: "))
        if nota >= 1.0 and nota <= 7.0:
            notas.append(nota)
        else:
            valido = False
            break
    if valido == True:
        promedio = sum(notas) / len(notas)
        alta = max(notas)
        baja = min(notas)
        print(f"El promedio final del alumno es de {promedio}, la nota más alta fue {alta} y la más baja fue {baja}")
    else:
        print("Ingresa una nota válida.")
# 11. Filtro de Arreglos
# Dado un arreglo de números generado por el usuario, crea un nuevo arreglo que contenga solo los
# números que sean mayores a 50.
# Muestra ambos arreglos.
def filtroArreglos ():
    cantidad = int(input("¿Cuantos números deseas ingresar?: "))
    mayor50 = []
    nUser = []
    for i in range(1, cantidad + 1):
        arrayUsuario = int(input("Ingrese un número: "))
        if arrayUsuario > 50:
            mayor50.append(arrayUsuario)
        else:
            nUser.append(arrayUsuario)
            print(f"Valores ingresados por el usuario: {nUser} \nValores mayor a 50: {mayor50}")
# 12. Buscador de Elementos
# Crea una lista de 10 ciudades. Pide al usuario que ingrese el nombre de una ciudad y 
# el programa debe decir si la ciudad se encuentra en la lista y en qué índice (posición) está.
def buscadorElemento():
    ciudades = ["Nairobi", "Tokio" , "Santiago", "Lima", "Caracas", "Rio", "Barlin", "Seul", "Buenos Aires"],
    ciudad = input("Ingresar ciudad (con mayuscula al principio): ").capitalize()
    esta = ciudades.index(ciudad)
    if esta < len(ciudades):
        print(f"Tu cuidad está en el arreglo, en la posicion {esta}")
    else:
        print("Tu ciudad no está en el arreglo")
# 13. Simulación de Inventario
# Crea dos arreglos: uno para nombres_productos y otro para precios. 
# Permite al usuario ingresar 3 productos con sus precios. 
# Luego, muestra una lista formateada: Producto: [Nombre] - Precio: $[Valor].
def inventario():
    nombres_productos = []
    precios = []
    for i in range(3):
        nombre = input("Nombre del producto:")
        precio = float(input("Precio: "))
        nombres_productos.append(nombre)
        precios.append(precio)
    print("\nInventario:")
    for i in range(3) :
        print(f"Producto: {nombres_productos[i]} - Precio {precio[i]}")
#Ejercicio 14: Generador de Lista de Compras
'''Usa un bucle while para que el usuario agregue artículos a una lista de compras.
El proceso termina cuando el usuario escribe "terminar".
Al final, muestra la lista ordenada alfabéticamente.'''
def listaCompras():
    carrito = []
    aniadiendoCarrito = True
    while aniadiendoCarrito:
        articulo = input("Agrega un articulo (o escribre 'terminar' para salir): ")
        if articulo.lower() == "terminar":
            break
        elif articulo.strip() == "":
            print("No puede estar vacío")
        else:
            carrito.append(articulo)
    if len(carrito) > 0:
        carrito.sort()
        print(f"Carrito de compras: {carrito}")

#Ejercicio 15: Análisis de Temperaturas
'''Solicita las temperaturas de los 7 días de la semana y guárdalas en un arreglo. Muestra:
El promedio semanal.
Cuántos días la temperatura fue superior a 25 grados.
El día con la temperatura más baja (asumiendo que el índice 0 es Lunes).'''
def analisisTemp():
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    tempSemanal = []
    superior25 = 0
    for i in range(len(dias)):
        temperatura = int(input(f"Ingresa la temperatura del día {dias[i]}: "))
        tempSemanal.append(temperatura)
        if temperatura > 25:
            superior25 += 1
    print(f"El promedio semanal fue de: {sum(tempSemanal) / len(tempSemanal)}°")
    if superior25 > 1:
        print(f"{superior25} días tuvieron una temperatura superior a 25°")
    elif superior25 == 1:
        print(f"Solo {superior25} día tuvo una temperatura superior a 25°")
    else:
        print("Ningún día tuvo una temperatura superior a 25°")
    print(f"La temperatura más baja registrada fue de {min(tempSemanal)}°")
#Menu de navegación para ejercicios
continuar = True
while continuar:
    print
    print("---Ejercicio 1---")
    print("---Ejercicio 2---")
    print("---Ejercicio 3---")
    print("---Ejercicio 4---")
    print("---Ejercicio 5---")
    print("---Ejercicio 6---")
    print("---Ejercicio 7---")
    print("---Ejercicio 8---")
    print("---Ejercicio 9---")
    print("---Ejercicio 10---")
    print("---Ejercicio 11---")
    print("---Ejercicio 12---")
    print("---Ejercicio 13---")
    print("---Ejercicio 14---")
    print("---Ejercicio 15---")
    opcion = input("\n---- Elige una opción: (1-15) (0 para salir) =")
    if opcion == "1":
        print("\nEjecutando ejercicio 1: ")
        print(numerosDinamicos())
    elif opcion == "2":
        print("\nEjecutando ejercicio 2: ")
        print(verificador_edad)
    elif opcion == "3":
        print("\nEjecutando ejercicio 3: ")
        print(aplicarDescuento())
    elif opcion == "4":
        print("\nEjecutando ejercicio 4: ")
        print(clasificadorNum())
    elif opcion == "5":
        print("\nEjecutando ejercicio 5: ")
        print(tablaMultiplicar())
    elif opcion == "6":
        print("\nEjecutando ejercicio 6: ")
        print(sumatoriaCentinela())
    elif opcion == "7":
        print("\nEjecutando ejercicio 7: ")
        print(contadorVocales())
    elif opcion == "8":
        print("\nEjecutando ejercicio 8: ")
        print(validarContrasena())
    elif opcion == "9":
        print("\nEjecutando ejercicio 9: ")
        print(registroNombres())
    elif opcion == "10":
        print("\nEjecutando ejercicio 10: ")
        print(promedioNotas())
    elif opcion == "11":
        print("\nEjecutando ejercicio 11: ")
        print(filtroArreglos ())
    elif opcion == "12":
        print("\nEjecutando ejercicio 12: ")
        print(buscadorElemento())
    elif opcion == "13":
        print("\nEjecutando ejercicio 13: ")
        print(inventario())
    elif opcion == "14":
        print("\nEjecutando ejercicio 14: ")
        print(listaCompras())
    elif opcion == "15":
        print("\nEjecutando ejercicio 15: ")
        print(analisisTemp())
    elif opcion == "0":
        print("Saliendo...")
        continuar = False
    else:
        print("Opción no válida, intenta otra vez")
