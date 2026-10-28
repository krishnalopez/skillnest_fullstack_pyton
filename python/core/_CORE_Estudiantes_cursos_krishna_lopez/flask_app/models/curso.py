from flask_app.config.mysqlconnection import connectToMySQL

class Curso:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO cursos (nombre) VALUES (%(nombre)s);"
        return connectToMySQL('esquema_estudiantes_cursos').query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cursos;"
        results = connectToMySQL('esquema_estudiantes_cursos').query_db(query)
        cursos = []
        if results:
            for row in results:
                cursos.append(cls(row))
        return cursos

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM cursos WHERE id = %(id)s;"
        results = connectToMySQL('esquema_estudiantes_cursos').query_db(query, data)
        if not results:
            return False
        return cls(results[0])