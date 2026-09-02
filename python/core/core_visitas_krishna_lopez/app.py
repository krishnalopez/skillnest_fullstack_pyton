# ==========================================================
# VISITAS - SESIONES EN FLASK
# ==========================================================

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session
)


# ==========================================================
# CREACIÓN DE LA APLICACIÓN
# ==========================================================

app = Flask(__name__)

app.secret_key = "clave-secreta-visitas"


# ==========================================================
# RUTA PRINCIPAL
# ==========================================================

@app.route("/")
def index():
    """
    Muestra la cantidad de visitas del usuario.

    Una visita directa a esta ruta aumenta el contador en uno.
    Si se llega mediante una acción de los botones, no se suma
    una visita adicional.
    """

    # Comprobar si la ruta fue llamada después de una acción.
    no_contar_visita = session.pop("no_contar_visita", False)

    if not no_contar_visita:
        if "visitas" in session:
            session["visitas"] += 1
        else:
            session["visitas"] = 1

    # Inicializar el contador de reinicios.
    if "reinicios" not in session:
        session["reinicios"] = 0

    return render_template(
        "index.html",
        visitas=session["visitas"],
        reinicios=session["reinicios"]
    )


# ==========================================================
# AUMENTAR VISITAS EN 2
# ==========================================================

@app.route("/sumar_dos")
def sumar_dos():
    """
    Aumenta el contador de visitas exactamente en dos unidades.
    """

    if "visitas" not in session:
        session["visitas"] = 0

    session["visitas"] += 2

    # Evitar que el redirect a index sume otra visita.
    session["no_contar_visita"] = True

    return redirect(url_for("index"))


# ==========================================================
# REINICIAR CONTADOR
# ==========================================================

@app.route("/reiniciar")
def reiniciar():
    """
    Reinicia el contador de visitas y registra el reinicio.
    """

    if "reinicios" not in session:
        session["reinicios"] = 0

    session["reinicios"] += 1
    session["visitas"] = 0

    # Evitar que el redirect a index convierta 0 en 1.
    session["no_contar_visita"] = True

    return redirect(url_for("index"))


# ==========================================================
# SUMAR UNA CANTIDAD PERSONALIZADA
# ==========================================================

@app.route("/sumar", methods=["POST"])
def sumar():
    """
    Agrega al contador la cantidad enviada desde el formulario.
    """

    try:
        cantidad = int(request.form.get("cantidad", 0))
    except ValueError:
        cantidad = 0

    # Solo aceptar cantidades positivas.
    if cantidad < 1:
        return redirect(url_for("index"))

    if "visitas" not in session:
        session["visitas"] = 0

    session["visitas"] += cantidad

    # Evitar que el redirect a index sume otra visita.
    session["no_contar_visita"] = True

    return redirect(url_for("index"))


# ==========================================================
# DESTRUIR TODA LA SESIÓN
# ==========================================================

@app.route("/destruir_sesion")
def destruir_sesion():
    """
    Elimina completamente la sesión del usuario.
    """

    session.clear()

    # Después de destruir la sesión, el acceso a index
    # debe contar como una nueva visita.
    return redirect(url_for("index"))


# ==========================================================
# EJECUTAR APLICACIÓN
# ==========================================================

if __name__ == "__main__":
    app.run(debug=True)