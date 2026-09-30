from flask_app import app
from flask_app.controllers import usuarios

# ==========================================================
# PUNTO DE ENTRADA DE LA APLICACIÓN
# ==========================================================
if __name__ == "__main__":
    app.run(debug=True)