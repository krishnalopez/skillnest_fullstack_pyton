from flask import Flask

# INICIALIZACIÓN DE LA APLICACIÓN FLASK
app = Flask(__name__)

# CLAVE SECRETA (Para manejo de sesiones y flash messages)
app.secret_key = "clave-secreta"