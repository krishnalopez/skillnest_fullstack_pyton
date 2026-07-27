from flask import Flask, render_template

app = Flask(__name__)

# Base de datos de Pokémon
pokedex = [
    {"id": 1, "nombre": "Bulbasaur", "tipo": "Planta/Veneno", "imagen": "Bulbasaur.png", "poder": 45, "altura": "0.7m", "peso": "6.9kg"},
    {"id": 4, "nombre": "Charmander", "tipo": "Fuego", "imagen": "Charmander.png", "poder": 39, "altura": "0.6m", "peso": "8.5kg"},
    {"id": 7, "nombre": "Squirtle", "tipo": "Agua", "imagen": "Squirtle.png", "poder": 44, "altura": "0.5m", "peso": "9.0kg"},
    {"id": 25, "nombre": "Pikachu", "tipo": "Eléctrico", "imagen": "Pikachu.png", "poder": 35, "altura": "0.4m", "peso": "6.0kg"},
    {"id": 39, "nombre": "Jigglypuff", "tipo": "Normal/Hada", "imagen": "Jigglypuff.png", "poder": 115, "altura": "0.5m", "peso": "5.5kg"},
    {"id": 52, "nombre": "Meowth", "tipo": "Normal", "imagen": "Meowth.png", "poder": 40, "altura": "0.4m", "peso": "4.2kg"},
    {"id": 54, "nombre": "Psyduck", "tipo": "Agua", "imagen": "Psyduck.png", "poder": 50, "altura": "0.8m", "peso": "19.6kg"},
    {"id": 94, "nombre": "Gengar", "tipo": "Fantasma/Veneno", "imagen": "Gengar.png", "poder": 60, "altura": "1.5m", "peso": "40.5kg"},
    {"id": 95, "nombre": "Onix", "tipo": "Roca/Tierra", "imagen": "Onix.png", "poder": 35, "altura": "8.8m", "peso": "210.0kg"},
    {"id": 143, "nombre": "Snorlax", "tipo": "Normal", "imagen": "Snorlax.png", "poder": 160, "altura": "2.1m", "peso": "460.0kg"}
]

# Mapa de clases CSS según el tipo de Pokémon
colores = {
    "planta": "planta",
    "veneno": "veneno",
    "fuego": "fuego",
    "agua": "agua",
    "eléctrico": "electrico",
    "normal": "normal",
    "hada": "hada",
    "fantasma": "fantasma",
    "roca": "roca",
    "tierra": "tierra"
}

# 1. Ruta principal para mostrar todos los Pokémon
@app.route("/")
@app.route("/pokemon")
def listar_todos():
    return render_template("pokemon.html", poke=pokedex, colores=colores, titulo="Todos los Pokémon")

# 2. Ruta para mostrar una cantidad específica de Pokémon
@app.route("/pokemon/cantidad/<int:cantidad>")
def obtener_limite(cantidad):
    return render_template("pokemon.html", poke=pokedex[:cantidad], colores=colores, titulo=f"Primeros {cantidad} Pokémon")

# 3. Ruta para buscar Pokémon por ID
@app.route("/pokemon/<int:id>")
def ver_detalle_pokemon(id):
    for p in pokedex:
        if p["id"] == id:
            return render_template("pokemon.html", poke=[p], colores=colores, titulo=f"Pokémon: {p['nombre']}")
    return pokemon_no_encontrado(f"ID #{id}")

# 4. Ruta para buscar Pokémon por Nombre
@app.route("/pokemon/<string:name>")
def buscar_por_nombre(name):
    for p in pokedex:
        if p["nombre"].lower() == name.lower():
            return render_template("pokemon.html", poke=[p], colores=colores, titulo=f"Pokémon: {p['nombre']}")
    return pokemon_no_encontrado(name)

# Handler/Función para error 404
@app.errorhandler(404)
def pokemon_no_encontrado(error_or_message):
    mensaje = error_or_message if isinstance(error_or_message, str) else "página no encontrada"
    return render_template("404.html", mensaje=mensaje), 404

if __name__ == "__main__":
    app.run(debug=True)