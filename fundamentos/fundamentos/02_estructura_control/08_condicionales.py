num = 15
if num > 20:
    print("Número mayor a 20")
else:
    print("Número menor a 20")
'''
La variable num es menor a 20, por lo que el bloque de código de else será ejecutado.
Es decir que vamos a imprimir "Número menor a 20"
'''
#Estructura IF-ELIF-ELSE
num = 101
if num > 50:
    print("Número mayor a 50")
elif num > 100:
    print("Número mayor a 100")
else:
    print("Número menor a 10")
'''
A pesar de que num es mayor que 50 y 100, la primera condicional que se cumpla es la única que se ejecutará.
Es por eso que solo imprimirá: "Número mayor a 50"
'''
if num < 60:
    print("Número menor a 60")
    
#No se cumple con la condicional, por lo que no se ejecuta el bloque de código
#Desafío
# Ingresar 3 números por teclado e identificar al mayor y el menor mostrando ambos
num1 = int(input("Ingresa un número: "))
num2 = int(input("Ingresa otro número: "))
num3 = int(input("Ingresa otro número: "))
mayor = ""
menor = ""
if num1 == num2 and num2 == num3:
    print("Todos los números son iguales.")
elif num1 < num2 and num1 < num3:
    menor = num1
    if num2 < num3:
        mayor = num3
    elif num3 < num2:
        mayor = num2
    print(f"El número mayor es {mayor} y el número menor es {menor}")
elif num2 < num1 and num2 < num3:
    menor = num2
    if num1 < num3:
        mayor = num3
    elif num3 < num1:
        mayor = num1
    print(f"El número mayor es {mayor} y el número menor es {menor}")
elif num3 < num1 and num3 < num2:
    menor = num3
    if num1 < num2:
        mayor = num2
    elif num2 < num1:
        mayor = num1
    print(f"El número mayor es {mayor} y el número menor es {menor}")