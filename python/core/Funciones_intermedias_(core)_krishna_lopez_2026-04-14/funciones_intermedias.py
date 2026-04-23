
# Ranking de puntajes de un torneo de eSports -
puntajes = [ [1000, 1500, 2000], [300, 700, 1400] ]
puntajes[1][0] = 600

# Lista de creadores de contenido en una plataforma de streaming
streamers = [
    {"nombre": "GameNinjaPro", "seguidores": 250000},
    {"nombre": "PixelWarrior", "seguidores": 180000}
]
streamers[0]["nombre"] = "EliteGamerX"

# Eventos en distintas ciudades del mundo 
eventos = {
    "Estados Unidos": ["Los Ángeles", "Nueva York", "Las Vegas"],
    "España": ["Madrid", "Barcelona", "Valencia"]
}
eventos["Estados Unidos"][2] = "San Francisco"

# Coordenadas de la sede de un torneo internacional
ubicacion = [
    {"latitud": 34.052235, "longitud": -118.243683}
]
ubicacion[0]["latitud"] = 40.712776

# 2) Creacion de funciones 


def iterar_diccionario(lista):
    inte = input("Ingresa un numero (0/1):_")
    
    if inte == "0":
        print(f"nombre - {lista[0]["nombre"]}, seguidores - {lista[0]["seguidores"]}")
    elif inte == "1":
        print(f"nombre - {lista[1]["nombre"]}, seguidores - {lista[1]["seguidores"]}")
    else:
        print("Por favor ingresar valor valido")


def obtenervalores(clave, lista):
    for i in range(len(lista)):
        actual = lista[i]
        if actual in lista:
            print(lista[i][clave])
        else:
            pass


def mostrar_informacion(diccionario):
    for categoria, lista in diccionario.items():
        print(f"{len(lista)} {categoria.upper()}")
        for item in lista:
            print(item)