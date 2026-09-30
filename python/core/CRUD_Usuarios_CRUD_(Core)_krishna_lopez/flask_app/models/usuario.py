from flask_app.config.mysqlconnection import connectToMySQL

# ==========================================================
# MODELO USUARIO
# ==========================================================
class Usuario:
    BASE_DATOS = "esquema_usuarios"

    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    # CREAR USUARIO (INSERT)
    @classmethod
    def save(cls, datos):
        query = """
            INSERT INTO usuarios (nombre, apellido, email)
            VALUES (%(nombre)s, %(apellido)s, %(email)s);
        """
        return connectToMySQL(cls.BASE_DATOS).query_db(query, datos)

    # OBTENER TODOS LOS USUARIOS (SELECT)
    @classmethod
    def get_all(cls):
        query = """
            SELECT id, nombre, apellido, email, created_at, updated_at
            FROM usuarios
            ORDER BY id;
        """
        resultados = connectToMySQL(cls.BASE_DATOS).query_db(query)
        
        usuarios = []
        if resultados:
            for fila in resultados:
                usuarios.append(cls(fila))
        return usuarios

    # OBTENER UN USUARIO POR ID (SELECT)
    @classmethod
    def get_one(cls, datos):
        query = """
            SELECT id, nombre, apellido, email, created_at, updated_at
            FROM usuarios
            WHERE id = %(id)s;
        """
        resultado = connectToMySQL(cls.BASE_DATOS).query_db(query, datos)

        if not resultado:
            return None

        return cls(resultado[0])

    # ACTUALIZAR USUARIO (UPDATE)
    @classmethod
    def update(cls, datos):
        query = """
            UPDATE usuarios
            SET nombre = %(nombre)s,
                apellido = %(apellido)s,
                email = %(email)s
            WHERE id = %(id)s;
        """
        return connectToMySQL(cls.BASE_DATOS).query_db(query, datos)

    # ELIMINAR USUARIO (DELETE)
    @classmethod
    def delete(cls, datos):
        query = """
            DELETE FROM usuarios
            WHERE id = %(id)s;
        """
        return connectToMySQL(cls.BASE_DATOS).query_db(query, datos)