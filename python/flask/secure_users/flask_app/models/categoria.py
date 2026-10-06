from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

class categorias:
    def __init__(self, data):
        self.id_categoria = data["id_categoria"]
        self.nombre = data["nombre"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]