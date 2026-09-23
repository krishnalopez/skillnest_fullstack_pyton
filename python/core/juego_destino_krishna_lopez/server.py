from flask import Flask, render_template, request, session, redirect, url_for, flash
import random

app = Flask(__name__)
app.secret_key = "clave_secreta_oraculo"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/enviar", methods=["POST"])
def enviar():
    nombre = request.form.get("nombre")
    edad_str = request.form.get("edad")
    color = request.form.get("color")
    animal = request.form.get("animal")

    # Validación e integración con las alertas flash del HTML
    if not nombre or not edad_str or not color or not animal:
        flash("Por favor, completa todos los campos del formulario.", "warning")
        return redirect(url_for("index"))

    try:
        edad = int(edad_str)
    except ValueError:
        flash("Ingresa una edad válida.", "danger")
        return redirect(url_for("index"))

    session["nombre"] = nombre
    session["edad"] = edad
    session["color"] = color
    session["animal"] = animal

    return redirect(url_for("futuro"))

@app.route("/futuro")
def futuro():
    if "nombre" not in session:
        return redirect(url_for("index"))

    nombre = session["nombre"]
    edad = session["edad"]
    color = session["color"]
    animal = session["animal"]

    # Mensajes personalizados por edad
    if edad < 18:
        edad_comentario = "Aunque eres joven, tu madurez te permitirá tomar decisiones acertadas."
    elif edad < 30:
        edad_comentario = "Estás en una etapa de crecimiento y aprendizaje; aprovecha cada oportunidad."
    elif edad < 50:
        edad_comentario = "Tienes experiencia y sabiduría, ahora es momento de cosechar frutos."
    else:
        edad_comentario = "Tu larga trayectoria te ha dado una perspectiva única; sigue compartiendo tu conocimiento."

    # Mensajes por color
    color_mensajes = {
        "rojo": "tu pasión y energía te impulsarán a lograr grandes metas.",
        "azul": "tu serenidad y sabiduría te guiarán en momentos importantes.",
        "verde": "tu conexión con la naturaleza te dará equilibrio y salud.",
        "morado": "tu espiritualidad y creatividad te abrirán nuevos caminos.",
        "amarillo": "tu alegría y optimismo atraerán el éxito."
    }
    mensaje_color = color_mensajes.get(color, "tu personalidad es única y especial.")

    # Mensajes por animal
    animal_mensajes = {
        "perro": "la lealtad y la amistad te harán rodear de personas valiosas.",
        "gato": "la independencia y la astucia te llevarán a resolver problemas con ingenio.",
        "águila": "la visión y la perspectiva te permitirán ver más allá de lo común.",
        "león": "la valentía y el liderazgo inspirarán a otros a seguirte.",
        "delfín": "la inteligencia y la sociabilidad te abrirán puertas en el ámbito social."
    }
    mensaje_animal = animal_mensajes.get(animal, "tu espíritu te guiará por buen camino.")

    # Selección aleatoria de destino base
    mensajes_positivos = [
        " Tendrás un futuro brillante lleno de éxitos",
        " La suerte estará de tu lado en todos tus proyectos",
        " Grandes oportunidades te esperan en el amor y el trabajo ",
        " Tu creatividad te llevará a lugares increíbles",
        " Superarás todos los obstáculos con valentía "
    ]
    mensajes_negativos = [
        " Cuidado con las decisiones impulsivas, podrían traerte problemas ",
        " Se avecinan días difíciles, pero todo pasará",
        " Alguien cercano podría traicionarte, mantén los ojos abiertos",
        " No todo lo que brilla es oro, analiza bien las ofertas",
        " Evita los viajes largos en los próximos meses"
    ]

    destino_base = random.choice(mensajes_positivos) if random.choice([True, False]) else random.choice(mensajes_negativos)
    destino_final = f"{destino_base} {mensaje_color} {mensaje_animal} {edad_comentario}"

    numero_suerte = random.randint(1, 99)

    return render_template(
        "futuro.html",
        nombre=nombre,
        edad=edad,
        color=color,
        animal=animal,
        destino=destino_final,
        numero_suerte=numero_suerte,
        mensaje_color=mensaje_color,
        mensaje_animal=mensaje_animal
    )

if __name__ == "__main__":
    app.run(debug=True, port=5000)