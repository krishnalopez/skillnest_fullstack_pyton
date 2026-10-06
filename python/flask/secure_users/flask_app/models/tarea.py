from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

class tareas:
    def __init__(self, data):
        self.id_tarea = data["id_tarea"]
        self.titulo = data["titulo"]
        self.categoria_id = data["categoria_id"]
        self.estado = data["estado"]
        self.prioridad = data["prioridad"]
        self.fecha_limite = data["fecha_limite"]
        self.descripcion = data["descripcion"]
        self.usuario_id = data["usuario_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]