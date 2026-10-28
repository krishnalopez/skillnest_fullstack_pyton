from flask import render_template, redirect, request, url_for, session, flash
from flask_app import app
from flask_app.models.usuario import Usuario
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route("/")
def index():
    if 'usuario_id' in session:
        return redirect(url_for('inicio'))
    return redirect(url_for('mostrar_login'))

@app.route("/iniciar_sesion")
def mostrar_login():
    if 'usuario_id' in session:
        return redirect(url_for('inicio'))
    return render_template("iniciar_sesion.html")

@app.route("/registrar", methods=["POST"])
def registrar():
    if not Usuario.validar_registro(request.form):
        return redirect(url_for('mostrar_login'))
    
    password_hash = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
    
    data = {
        "nombre": request.form["nombre"].strip(),
        "apellido": request.form["apellido"].strip(),
        "email": request.form["email"].strip().lower(),
        "password": password_hash
    }
    
    usuario_id = Usuario.save(data)
    
    if not usuario_id:
        flash("Error al guardar en la base de datos. Intenta de nuevo.", "registro")
        return redirect(url_for('mostrar_login'))
        
    session['usuario_id'] = usuario_id  
    session['nombre'] = data['nombre']
    return redirect(url_for('inicio'))

@app.route("/login", methods=["POST"])
def login():
    usuario = Usuario.get_by_email(request.form['email'].strip().lower())
    
    if not usuario or not bcrypt.check_password_hash(usuario.password, request.form['password']):
        flash("Credenciales inválidas.", "login")
        return redirect(url_for('mostrar_login'))
        
    session['usuario_id'] = usuario.id  
    session['nombre'] = usuario.nombre
    return redirect(url_for('inicio'))

@app.route("/inicio")
def inicio():
    if 'usuario_id' not in session:
        return redirect(url_for('mostrar_login'))
        
    usuario_conectado = Usuario.get_by_id(session['usuario_id'])
    if not usuario_conectado:
        session.clear()
        return redirect(url_for('mostrar_login'))
        
    return render_template("bienvenida.html", usuario=usuario_conectado)

@app.route("/logout")
def logout():
    session.clear()  
    return redirect(url_for('mostrar_login'))