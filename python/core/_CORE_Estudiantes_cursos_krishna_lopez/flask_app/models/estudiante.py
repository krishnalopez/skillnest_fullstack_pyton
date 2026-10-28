from flask_app.config.mysqlconnection import connectToMySQL

class Estudiante:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.edad = data['edad']
        self.curso_id = data['curso_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO estudiantes (nombre, apellido, edad, curso_id) 
            VALUES (%(nombre)s, %(apellido)s, %(edad)s, %(curso_id)s);
        """
        return connectToMySQL('esquema_estudiantes_cursos').query_db(query, data)

    @classmethod
    def get_by_curso(cls, data):
        query = "SELECT * FROM estudiantes WHERE curso_id = %(curso_id)s;"
        results = connectToMySQL('esquema_estudiantes_cursos').query_db(query, data)
        estudiantes = []
        if results:
            for row in results:
                estudiantes.append(cls(row))
        return estudiantes