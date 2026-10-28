import re
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

# Constante para el nombre del esquema/base de datos
BASE_DATOS = 'esquema_usuarios'

# Expresión regular para validación de formato de correo
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class Usuario:
    def __init__(self, datos):
        self.id = datos.get('id')
        self.nombre = datos.get('nombre')
        self.apellido = datos.get('apellido')
        self.email = datos.get('email')
        self.password = datos.get('password')
        self.created_at = datos.get('created_at')
        self.updated_at = datos.get('updated_at')

    @classmethod
    def save(cls, datos):
        query = """
            INSERT INTO usuarios (nombre, apellido, email, password) 
            VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s);
        """
        return connectToMySQL(BASE_DATOS).query_db(query, datos)

    @classmethod
    def get_by_email(cls, email):
        query = "SELECT * FROM usuarios WHERE email = %(email)s;"
        datos = {'email': email}
        resultados = connectToMySQL(BASE_DATOS).query_db(query, datos)
        
        if not resultados:
            return False
            
        return cls(resultados[0])

    @classmethod
    def get_by_id(cls, usuario_id):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        datos = {'id': usuario_id}
        resultados = connectToMySQL(BASE_DATOS).query_db(query, datos)
        
        if not resultados:
            return False
            
        return cls(resultados[0])

    @staticmethod
    def validar_registro(datos):
        es_valido = True
        
        # Extracción segura de datos para evitar KeyError
        nombre = datos.get('nombre', '').strip()
        apellido = datos.get('apellido', '').strip()
        email = datos.get('email', '').strip()
        password = datos.get('password', '')
        confirm_password = datos.get('confirm_password', '')

        # Validar Nombre