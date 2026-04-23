datos = [
    {"nombre": "Carlos", "puntaje": 80},
    {"nombre": "María", "puntaje": 95},
    {"nombre": "Pedro", "puntaje": 70}
]

# 1. Cambiar el puntaje de Pedro a 75
datos[2]["puntaje"] = 75
print(f"Nombre:{datos[2] ["nombre"]} - {datos[2] ["puntaje"]}")
# 2. Crear función que imprima:
#    "Carlos obtuvo 80 puntos"
def cambiarPuntaje():
    print(f"{datos[0] ["nombre"]} obtuvo {datos[0] ["puntaje"]} puntos")
    cambiarPuntaje()
# 3. Crear función que reciba "nombre" o "puntaje" e imprima solo esos valores
def imprimirDatos(nombre):
    if nombre == "María":
        print(f"Nombre: {nombre} - puntaje: {datos[1]["puntaje"]} puntos")
        
imprimirDatos(datos[1]["nombre"])