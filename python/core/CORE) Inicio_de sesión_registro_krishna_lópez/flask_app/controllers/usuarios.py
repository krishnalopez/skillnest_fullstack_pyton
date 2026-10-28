from flask import render_template, redirect, request, url_for, session, flash
from flask_app import app
from flask_app.models.usuario import Usuario
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


# --- RUTAS DE VISTAS Y NAVEGACIÓN ---

@app.route("/")
def index():
    if session.get('usuario_id'):
        return redirect(url_for('inicio'))
    return redirect(url_for('mostrar_login'))


@app.route("/registrarse")
def mostrar_registro():
    if session.get('usuario_id'):
        return redirect(url_for('inicio'))
    return render_template("registrarse.html")


@app.route("/iniciar_sesion")
def mostrar_login():
    if session.get('usuario_id'):
        return redirect(url_for('inicio'))
    return render_template("iniciar_sesion.html")


@app.route("/inicio")
def inicio():
    if 'usuario_id' not in session:
        return redirect(url_for('mostrar_login'))
        
    usuario_actual = Usuario.get_by_id(session['usuario_id'])
    return render_template("inicio.html", usuario=usuario_actual)


# --- ACCIONES Y PROCESAMIENTO ---

@app.route("/registrar", methods=["POST"])
def registrar():
    if not Usuario.validar_registro(request.form):
        return redirect(url_for('mostrar_registro'))
    
    # .decode('utf-8') evita guardar un objeto bytes en la base de datos
    clave_encriptada = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
    
    datos = {
        "nombre": request.form.get("nombre", "").strip(),
        "apellido": request.form.get("apellido", "").strip(),
        "email": request.form.get("email", "").strip(),
        "password": clave_encriptada
    }
    
    usuario_id = Usuario.save(datos)
    session['usuario_id'] = usuario_id  
    return redirect(url_for('inicio'))


@app.route("/login", methods=["POST"])
def login():
    email = request.form.get('email', '').strip()
    password = request.form.get('password', '')
    
    usuario = Usuario.get_by_email(email)
    
    if not usuario or not bcrypt.check_password_hash(usuario.password, password):
        flash("Credenciales inválidas.", "login")
        return redirect(url_for('mostrar_login'))
        
    session['usuario_id'] = usuario.id  
    return redirect(url_for('inicio'))


@app.route("/logout")
def logout():
    session.clear()  
    return redirect(url_for('mostrar_login'))