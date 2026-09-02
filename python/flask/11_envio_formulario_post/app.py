from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def pagina_inicio():
    return render_template("index.html")


@app.route('/crear_usuario', methods=['POST'])
def registrar_usuario():
    # Obtener datos del formulario
    dato_nombre = request.form.get("nombre")
    dato_email = request.form.get("email")
    dato_edad = request.form.get("age")
    dato_ciudad = request.form.get("ciudad")

    # Redirigir a una ruta GET que muestre el resultado
    # Pasamos los datos como parámetros en la URL
    return redirect(url_for(
        'usuario',
        nombre=dato_nombre,
        email=dato_email,
        age=dato_edad,
        ciudad=dato_ciudad
    ))


@app.route('/usuario')
def ver_usuario():
    # Recibir los datos desde la URL
    dato_nombre = request.args.get("nombre")
    dato_email = request.args.get("email")
    dato_edad = request.args.get("age")
    dato_ciudad = request.args.get("ciudad")

    return render_template(
        "user.html",
        nombre=dato_nombre,
        email=dato_email,
        age=dato_edad,
        ciudad=dato_ciudad
    )


if __name__ == "__main__":
    app.run(debug=True)

