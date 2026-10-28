from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.curso import Curso
from flask_app.models.estudiante import Estudiante

@app.route("/")
def index():
    return redirect("/cursos")

@app.route("/cursos")
def mostrar_cursos():
    todos_los_cursos = Curso.get_all()
    return render_template("cursos.html", cursos=todos_los_cursos)

@app.route("/cursos/crear", methods=["POST"])
def crear_curso():
    data = {
        "nombre": request.form["nombre"]
    }
    Curso.save(data)
    return redirect("/cursos")

@app.route("/cursos/<int:id>")
def mostrar_curso(id):
    data = {"id": id}
    curso = Curso.get_by_id(data)
    if not curso:
        return redirect("/cursos")
    
    estudiantes = Estudiante.get_by_curso(data)
    return render_template("mostrar_curso.html", curso=curso, estudiantes=estudiantes)

@app.route("/estudiante")
def nuevo_estudiante():
    todos_los_cursos = Curso.get_all()
    return render_template("nuevo_estudiante.html", cursos=todos_los_cursos)

@app.route("/estudiante/crear", methods=["POST"])
def crear_estudiante():
    data = {
        "nombre": request.form["nombre"],
        "apellido": request.form["apellido"],
        "edad": request.form["edad"],
        "curso_id": request.form["curso_id"]
    }
    Estudiante.save(data)
    return redirect("/cursos")